<?php namespace App\Filters;
use CodeIgniter\HTTP\RequestInterface;
use CodeIgniter\HTTP\ResponseInterface;
use CodeIgniter\Filters\FilterInterface;
use App\Models\UserModel;

class Auth implements FilterInterface
{
public function before(RequestInterface $request, $arguments = null)
{
  if(! session()->get('logged_in'))
      return redirect()->to('/login'); 
  $email = session()->get('email');
  $model = new UserModel();
  $data = $model->where('email', $email)->first();
  $paid_before = $data['paid_before'];
  $ses_data = [
      'paid_before'  => $data['paid_before']
  ];
  session()->set($ses_data);
  $today = \CodeIgniter\I18n\Time::yesterday();
  $deadline = \CodeIgniter\I18n\Time::parse($paid_before);
  if($deadline <= $today) 
      return redirect()->to('/block'); 
}
//--------------------------------------------------------------------
public function after(RequestInterface $request, ResponseInterface $response, $arguments = null)
{
// Do something here
}
}
