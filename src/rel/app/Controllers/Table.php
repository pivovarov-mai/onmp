<?php namespace App\Controllers;
  
use CodeIgniter\Controller;
  
class Table extends Controller
{
	
	public function index()
	{
    $data['property'] = json_decode(file_get_contents("../tables/Glasgo.json"));
    $data['title'] = "Шкала";
		
    echo view("templates/html_header");
    echo view("pages/table", $data);
    echo view("templates/html_header");
	}

  public function result()
  {
    
  }
} 
