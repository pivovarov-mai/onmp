<?php namespace App\Models;
  
use CodeIgniter\Model;
  
class CardModel extends Model{
    protected $table = 'cards';
    protected $allowedFields = [
      'idcard',
	  'iduser',
      'date',
      'order',
	  'status',
	  'comment'];
	protected $primaryKey = 'idcard';
}
