<?php namespace App\Models;
  
use CodeIgniter\Model;
  
class UserModel extends Model{
    protected $table = 'users';
    protected $allowedFields = [
		'iduser',
		'email',
		'password',
		'registered_at',
		'paid_before'];
	/*protected $validationRules    = [
        'email'        => 'required|valid_email|is_unique[users.email]',
    ];
	protected $validationMessages = [
        'email'        => [
            'is_unique' => 'Пользователь с таким адресом электронной почты уже зарегистрирован.'
        ]
    ];*/
	protected $primaryKey = 'iduser';
	
	public function verify($verificationText, $password)
	{
		$db = \Config\Database::connect();
		$builder = $db->table('users');
		$builder->where('verification_text', $verificationText);
		$builder->set('verificationText', NULL);
		$builder->set('password', password_hash($password, PASSWORD_DEFAULT));
		$builder->update();
	}
  public function changePassword($password, $verificationText)
  {
		$db = \Config\Database::connect();
		$builder = $db->table('users');
		$builder->where('verification_text', $verificationText);
		$builder->set('password', password_hash($password, PASSWORD_DEFAULT));
		$builder->set('verification_text', NULL);
	  return $builder->update();
  }

  public function sendMail($email, $message, $verificationText)
  {
      $from = "onmp.ru@yandex.ru";
      $to = "onmp.ru@yandex.ru";
      $subject = "ONMP.RU - регистрация";
      $site = base_url();
      $link = $site."/verify/".$verificationText;
      $mail = <<<END
From:$from
To:$to
Subject:$subject
$message

END;
      $filename = "/home/pivovar/mp/writable/logs/reg_mail.txt";
      file_put_contents($filename,$mail);
      $result = shell_exec("/usr/bin/msmtp --logfile /home/pivovar/mp/writable/logs/msmtp.log -C /home/pivovar/onmp.msmtprc -t < $filename");
  }
	
	
	public function verifyPasswordReset($email)
	{
		$verificationText = random_string('alnum',20);
		
		$db = \Config\Database::connect();
		$builder = $db->table('users');
		$builder->set('verification_text', $verificationText);
		$builder->where('email', $email);
	  $builder->update();
    $from = "onmp.ru@yandex.ru";
    $to = "onmp.ru@yandex.ru";
    $subject = "ONMP.RU - смена пароля";
    $site = base_url();
    $link = $site."/verify/".$verificationText;
    $message = <<<END

Уважаемый пользователь!

Вы запросили изменение пароля. Для введения нового пароля пройдите по ссылке (или скопируйте ее в адресную строку браузера):
$link

Если Вы не запрашивали изменение пароля, то можете проигнорировать это сообщение.


C уважением,
Команда разработчиков
$site
END;
      $mail = <<<END
From:$from
To:$to
Subject:$subject
$message

END;
      $filename = "/home/pivovar/mp/writable/logs/passwd_mail.txt";
      file_put_contents($filename,$mail);
      $result = shell_exec("/usr/bin/msmtp --logfile /home/pivovar/mp/writable/logs/msmtp.log -C /home/pivovar/onmp.msmtprc -t < $filename");
    return true;
	}

	public function verifyEmailAddress($email, $mp)
	{
		$verificationText = random_string('alnum',20);
		
		$db = \Config\Database::connect();
		$builder = $db->table('users');
		$builder->set('verification_text', $verificationText);
		$builder->set('email', strtolower($email));
		$builder->set('mp', $mp);
		if($builder->insert()) {
      $from = "onmp.ru@yandex.ru";
      $to = "onmp.ru@yandex.ru";
      $subject = "ONMP.RU - регистрация";
      $site = base_url();
      $link = $site."/verify/".$verificationText;
      $message = <<<END

Уважаемый пользователь, $email!
      
Для завершения процедуры регистрации придумайте и введите пароль, пройдя по следующей ссылке (или скопируйте ее в адресную строку браузера):
$link
      
Если Вы не регистрировались на сайте $site, то можете проигнорировать это сообщение.
    
    
C уважением,
Команда разработчиков
$site
END;
      $mail = <<<END
From:$from
To:$to
Subject:$subject
$message

END;
      $filename = "/home/pivovar/mp/writable/logs/reg_mail.txt";
      file_put_contents($filename,$mail);
      $result = shell_exec("/usr/bin/msmtp --logfile /home/pivovar/mp/writable/logs/msmtp.log -C /home/pivovar/onmp.msmtprc -t < $filename");
    } else
      return false;
	}
}
