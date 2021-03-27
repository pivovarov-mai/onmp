<div data-role="page" id="LoginPage">
	<div data-role="header" data-position="fixed">
		<h1>Вход</h1>
	</div>
	<div role="main" class="ui-content">
		<form action="/auth" data-ajax="false" method="post">

		<label for="account">Email:</label>
		<input type="text" name="email" id="account" value="<?= set_value('email') ?>">
		<?php if(session()->getFlashdata('wrong_email')):?>
		<div class="alert"><?= session()->getFlashdata('wrong_email') ?></div>
		<?php endif;?>

		<label for="passwd">Пароль (<a href="/forget_password">забыли?</a>):</label>
		<input type="password" name="password" id="passwd" value="" autocomplete="off">
		<?php if(session()->getFlashdata('wrong_passwd')):?>
		<div class="alert"><?= session()->getFlashdata('wrong_passwd') ?></div>
		<?php endif;?>

		<button type="submit">Войти</button>

		</form>
	</div>
	<div data-role="footer" data-position="fixed">
		<div data-role="navbar">
			<ul>
				<li><a href="#LoginPage" data-icon="home" class="ui-btn-active">Вход</a></li>
				<li><a href="#RegisterPage" data-icon="user">Регистрация</a></li>
				<li><a href="#AboutPage" data-icon="info">Информация</a></li>
			</ul>
		</div>
	</div>
</div>