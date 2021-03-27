<?php namespace App\Controllers;
  
use CodeIgniter\Controller;
  
class About extends Controller
{
    public function index()
    {
		helper('form');
        echo view('templates/html_header');
		echo view('pages/about');
        echo view('pages/register');
        echo view('pages/login');
        echo view('templates/html_footer');
    }
}
