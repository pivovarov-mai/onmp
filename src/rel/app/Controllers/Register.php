<?php namespace App\Controllers;
  
use CodeIgniter\Controller;
use App\Models\UserModel;
  
class Register extends Controller
{
    public function add_email_form()
    {
      helper('form');
      echo view('templates/html_header');
      echo view('pages/register');
      echo view('pages/login');
      echo view('pages/about');
      echo view('templates/html_footer');
    }
	
    public function register_email()
    {
		helper(['form','text']);
		$session = session();
		$data = [];
        $rules = [
            'email' => 'required|min_length[6]|max_length[50]|valid_email|is_unique[users.email]',
        ];
        if($this->validate($rules)){
            $email = $this->request->getVar('email');
            $mp = $this->request->getVar('mp');
            $model = new UserModel();
            $model->verifyEmailAddress($email, $mp);
            $session->setFlashdata('valid_email', 'Для окончания регистрации пройдите по ссылке в письме, отправленном на указанный адрес электронной почты.');
        } else {
            $session->setFlashdata('valid_email', '');
                  $data['validation'] = $this->validator;
		}
		echo view('templates/html_header');
		echo view('pages/register', $data);
		echo view('pages/login');
		echo view('pages/about');
		echo view('templates/html_footer');
    }
	
	public function new_password_form($verificationText)
	{
		helper('form');
    $data['verificationText'] = $verificationText;
		echo view('templates/html_header');
		echo view('pages/password', $data);
		echo view('pages/register');
    echo view('pages/login');
		echo view('pages/about');
    echo view('templates/html_footer');
	}
	
	public function update_password($verificationText)
	{
		helper('form');
    $session = session();
		$rules = [
			'password'      => 'required|min_length[4]|max_length[200]',
			'confpassword'  => 'matches[password]'
		];
		  
		if($this->validate($rules)){
      $password = $this->request->getPost('password');
      $model = new UserModel();
			if($model->changePassword($password, $verificationText)) {
				$session->setFlashdata('register_complete', 'Новый пароль сохранен.');
				//return redirect()->to('/login');
			} else {
				$session->setFlashdata('register_complete', 'Ссылка не работает.');
			}
		} else {
      $data = [];
			$data['validation'] = $this->validator;
		}
    $data['verificationText'] = $verificationText;
    echo view('templates/html_header');
    echo view('pages/password', $data);
    echo view('pages/register');
    echo view('pages/login');
    echo view('pages/about');
    echo view('templates/html_footer');
	}
}
