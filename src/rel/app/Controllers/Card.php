<?php namespace App\Controllers;
  
use CodeIgniter\Controller;
use App\Models\CardModel;
use CodeIgniter\I18n\Time;
  
class Card extends Controller
{
    public function index()
    {
		$session = session();
		$iduser = $session->get('iduser');
		$paid_before = $session->get('paid_before');
		$date = new Time($paid_before);
		$data['paid_before'] = $date->format('d.m.Y');;
		
		$model = new CardModel();
		$data['cards'] = $model->where('iduser', $iduser);
		
		$interval = 1;
		
		if($interval>0) {
			helper('element');
			echo view('templates/html_header');
			echo view('pages/home', $data);
			echo view('pages/create');
			echo view('pages/update');
			echo view('pages/form');
			echo view('pages/toc');
			echo view('pages/feedback');
			echo view('templates/html_footer');
		}
		else
			echo view('pages/block');
    }
	
	public function create()
	{
		// update DB
		$session = session();
		$iduser = $session->get('iduser');
		$model = new CardModel();
		$data = [
			'iduser'	=> $iduser,
			'order'		=> $this->request->getPost('order'),
			'comment'	=> $this->request->getPost('comment')
		];
		$model->insert($data);
		
		// update disk storage
		$idcard = $model->getInsertID();
		$session->set(['current_card' => $idcard]);
		$json_file = "card.json";
		$tex_file = "card.tex";
		$folder = CARD_STORAGE.sprintf("/%09d",$idcard);
		if(!file_exists($folder))
			mkdir($folder);
		file_put_contents("$folder/$json_file", json_encode($_POST, JSON_UNESCAPED_UNICODE));
	}
	
	public function update()
	{
		$session = session();
		$iduser = $session->get('iduser');
		$idcard = $session->get('current_card');
		$mp = $session->get('mp');
		$model = new CardModel();
		$data = [
			'order'		=> $this->request->getPost('order'),
			'status'	=> $this->request->getPost('status'),
			'comment'	=> $this->request->getPost('comment'),
			'date'		=> $this->request->getPost('date')
		];
		$result = $model->update($idcard, $data);
		
		helper(['save_tex','rus_date']);
		$json_file = "card.json";
		$tex_file = "card.tex";
		$folder = CARD_STORAGE.sprintf("/%09d",$idcard);
		if(!file_exists($folder))
			mkdir($folder);
    file_put_contents("$folder/$json_file", json_encode($_POST, JSON_UNESCAPED_UNICODE));
		$_POST['133']=rus_date($data['date']);
		$_POST['134']=$data['order'];
		if($data['status'] === "ready" && tex_from_post($_POST, "$folder/$tex_file", "$mp.tex"))
			shell_exec("cd $folder; /usr/bin/pdflatex $tex_file; /usr/bin/pdflatex $tex_file &");
	}
	
	public function delete($idcard)
	{
		$model = new CardModel();
		//$result = $model->delete($idcard);
		$data = [
			'status'	=> 'deleted',
		];
		$result = $model->update($idcard, $data);
		/* $folder = CARD_STORAGE.sprintf("/%09d",$idcard); */
		/* foreach (glob("$folder/*") as $filename) { */
            /* unlink($filename); */
        /* } */
		/* rmdir($folder); */
	}
	
	public function list($type)
	{
		helper('rus_date');
		$session = session();
		$iduser = $session->get('iduser');
		$model = new CardModel();
		$card_type = ['draft' => 'Черновики','ready' => 'Готовые', 'template' => 'Шаблоны', 'archive' => 'Архивные'];
		$data['type'] = $type;
		$data['card_type'] = $card_type[$type];
		$data['list'] = $model->where(['iduser' => $iduser, 'status' => $type])->findAll();
		echo view('lists/'.$type, $data);
	}
	
	public function download($idcard, $order)
	{
		$session = session();
		$iduser = $session->get('iduser');
		
		$model = new CardModel();
		$result = $model->where(['iduser' => $iduser, 'idcard' => $idcard])->findAll();
		
		if(sizeof($result)) {
			$path = CARD_STORAGE.sprintf("/%09d/card.pdf",$idcard);
			if(is_file($path)) {
				header('Content-Type: application/pdf'); 
				header('Content-Disposition: inline; filename="'.$order.'.pdf"');
				// OR header('Content-Disposition: attachment); to open in current browser tab
				header('Content-Transfer-Encoding: binary');
				header('Content-Length: '.filesize($path));
				header('Connection: close');
				readfile($path); 
				die();
			} else {
				echo view("templates/html_header");
				echo view("errors/html/error_404");
				echo view("templates/html_header");
			}
		} else {
			echo view("templates/html_header");
			echo view("errors/html/error_403");
			echo view("templates/html_header");
		}
	}
	
	public function json($idcard)
	{
		$session = session();
		$iduser = $session->get('iduser');
		
		$model = new CardModel();
		$result = $model->where(['iduser' => $iduser, 'idcard' => $idcard])->findAll();
		
		if(sizeof($result)) {
			$path = CARD_STORAGE.sprintf("/%09d/card.json",$idcard);
			if(readfile($path)) {
				header('Content-Type: application/json');
				$session->set(['current_card' => $idcard]);
			}
			else {
				echo view("templates/html_header");
				echo view("errors/html/error_404");
				echo view("templates/html_header");
			}
		} else {
			echo view("templates/html_header");
			echo view("errors/html/error_403");
			echo view("templates/html_header");
		}
	}
} 
