<div data-role="page" id="RequestPasswordPage">
	<div data-role="header" data-position="fixed">
		<h1>Забыли пароль</h1>
	</div>
	<div role="main" class="ui-content">
		<form action="/request_password" data-ajax="false" method="post">

		<label for="email_for_password_request">Введите адрес электронной почты, указанный при регистрации:</label>
		<input type="text" name="email" id="email_for_password_request" placeholder="Email" value="<?= set_value('email') ?>">
		<?php if(session()->getFlashdata('wrong_email')):?>
		<div class="alert"><?= session()->getFlashdata('wrong_email') ?></div>
		<?php endif;?>

		<button type="submit">Получить ссылку</button>
		
		<?php if(session()->getFlashdata('valid_email')):?>
		<div class="success"><?= session()->getFlashdata('valid_email') ?></div>
		<?php endif;?>

		</form>
	</div>
	<div data-role="footer" data-position="fixed">
		<div data-role="navbar">
			<ul>
				<li><a href="#LoginPage" data-icon="home">Вход</a></li>
				<li><a href="#RegisterPage" data-icon="user">Регистрация</a></li>
				<li><a href="#AboutPage" data-icon="info">Информация</a></li>
			</ul>
		</div>
	</div>
</div>
