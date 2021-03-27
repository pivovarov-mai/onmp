<div data-role="page" id="NewPasswordPage">
	<div data-role="header" data-position="fixed">
		<h1>Сохранение пароля</h1>
	</div>
	<div role="main" class="ui-content">
		<form action="/update_password/<?= $verificationText ?>" method="post">

		<label for="InputForPassword">Введите новый пароль:</label>
		<input type="password" name="password" id="InputForPassword">
		<?php if(isset($validation) && $validation->hasError('password')):?>
		<div class="alert alert-danger"><?= $validation->getError('password') ?></div>
		<?php endif;?>
		
		<label for="InputForConfPassword">Повторите новый пароль:</label>
		<input type="password" name="confpassword" id="InputForConfPassword">
		<?php if(isset($validation) && $validation->hasError('confpassword')):?>
		<div class="alert alert-danger"><?= $validation->getError('confpassword') ?></div>
		<?php endif;?>

		<button type="submit">Сохранить пароль</button>
		
		<?php if(session()->getFlashdata('register_complete')):?>
		<div class="success"><?= session()->getFlashdata('register_complete') ?></div>
		<?php endif;?>

		</form>
	</div>
	<div data-role="footer"  data-position="fixed">
		<div data-role="navbar" >
			<ul>
				<li><a href="#LoginPage" data-icon="home">Вход</a></li>
				<li><a href="#RegisterPage" data-icon="user" class="ui-btn-active">Регистрация</a></li>
				<li><a href="#AboutPage" data-icon="info">Информация</a></li>
			</ul>
		</div>
	</div>
</div>