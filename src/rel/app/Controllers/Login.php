<?php namespace App\Controllers;
  
use CodeIgniter\Controller;
use App\Models\UserModel;
use Config\Services;
  
class Login extends Controller
{
    public function enter_form()
    {
      helper('form');
      $data = [];
      echo view('templates/html_header');
      echo view('pages/login', $data);
      echo view('pages/register', $data);
      echo view('pages/about');
      echo view('templates/html_footer');
    } 
  
    public function auth()
    {
        helper('form');
        $session = session();
        $model = new UserModel();
        $email = $this->request->getVar('email');
        $password = $this->request->getVar('password');
        $data = $model->where('email', $email)->first();
        if($data){
            $pass = $data['password'];
            $verify_pass = password_verify($password, $pass);
            if($verify_pass){
                $ses_data = [
                    'iduser'       => $data['iduser'],
                    'email'        => $data['email'],
                    'paid_before'  => $data['paid_before'],
                    'logged_in'    => TRUE,
                    'current_card' => "",
                    'mp'           => $data['mp']
                ];
                $session->set($ses_data);
                return redirect()->to('/');
            }else{
                $session->setFlashdata('wrong_passwd', 'Неверный пароль');
                return redirect()->to('/login');
            }
        }else{
            $session->setFlashdata('wrong_email', 'Незарегистрированный email');
            return redirect()->to('/login');
        }
    }
	
	public function request_password_form()
  {
      helper('form');
      $data = [];
      echo view('templates/html_header');
      echo view('pages/forget', $data);
      echo view('pages/login', $data);
      echo view('pages/register', $data);
      echo view('pages/about');
      echo view('templates/html_footer');
  } 
	
	public function new_password_request()
	{
		helper(['form','text']);
		$session = session();
		$email = $this->request->getPost('email');
    $model = new UserModel();
    if($model->where('email',$email)->first()){
      if($model->verifyPasswordReset($email))
        $session->setFlashdata('valid_email', 'На указанный почтовый ящик отправлена ссылка для смены пароля.');
      else
        $session->setFlashdata('valid_email', 'Что-то пошло не так.');
    } else
    $session->setFlashdata('wrong_email', 'Незарегистрированный email');
		return redirect()->to('/forget_password');
	}
	
  public function logout()
  {
    $session = session();
    $session->destroy();
    return redirect()->to('/login');
  }
	
	public function send_feedback()
	{
    helper('form');
		$session = session();
		$email = $session->get('email');
		
    $mail = \Config\Services::email();
		$mail->setTo("no-reply@onmp.ru");
    $mail->setSubject('ONMP.RU - feedback');
    $mail->setMessage($email."\n\n".$this->request->getPost("feedback_message"));
    $result = shell_exec("/usr/bin/msmtp --logfile /home/pivovar/mp/writable/logs/msmtp.log -C /home/pivovar/onmp.msmtprc -t < $filename");
		//$mail->send();  
		
    return redirect()->to('/');
	}

	public function sendmail()
	{
    helper('form');
		$session = session();
		$email = $session->get('email');
    $from = "onmp.ru@yandex.ru";
    $to = "onmp.ru@yandex.ru";
    $subject = "ONMP.RU - feedback";
    $message = $email."\n\n".$this->request->getPost("feedback_message");
    $mail = <<<END
From:$from
To:$to
Subject:$subject
Сообщение от $email

$message

END;
    $filename = "/home/pivovar/mp/writable/logs/mail.txt";
    file_put_contents($filename,$mail);
    $result = shell_exec("/usr/bin/msmtp --logfile /home/pivovar/mp/writable/logs/msmtp.log -C /home/pivovar/onmp.msmtprc -t < $filename");
    return redirect()->to('/');
		/* $mail->setFrom("pivovar.de@yandex.ru"); */
		/* $mail->setTo("pivovarovd@mail.ru"); */
    /* $mail->setSubject('ONMP.RU - feedback'); */
    /* $mail->setMessage("hello 2"); */
    /* if ($result) */
    /*   echo "good"; */
    /* else */
    /*   echo "bad"; */
      //$mail->print_debugger();
    /* if($mail->send()) { */
    /*   show_error($mail->printDebugger()); */
    /*   echo "отправлено"; */  
    /* } else { */
    /*   show_error($mail->printDebugger()); */
    /*   echo "ошибка"; */
    /* } */
		
    //return redirect()->to('/');
	}

  public function block()
  {
		$session = session();
    echo view('templates/html_header');
    echo view('pages/block',[ 'paid_before' => $session->get('paid_before') ]);
    echo view('templates/html_footer');
  }
  
} 
