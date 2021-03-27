<div data-role="page" id="RegisterPage">
	<div data-role="header" data-position="fixed">
		<h1>Регистрация</h1>
	</div>
	<div role="main" class="ui-content">
		<form action="/register" data-ajax="false" method="post">
		
		<label for="InputForEmail">Email:</label>
		<input type="text" name="email" id="InputForEmail" value="<?= set_value('email') ?>">
		<?php if(isset($validation) && $validation->hasError('email')):?>
		<div class="alert alert-danger"><?= $validation->getError('email') ?></div>
		<?php endif;?>

    <fieldset data-role="controlgroup" data-type="horizontal">
      <input type="radio" name="mp" id="mp-onmp" value="onmp" checked="checked">
      <label for="mp-onmp">ОНМП</label>
      <input type="radio" name="mp" id="mp-smp" value="smp">
      <label for="mp-smp">СМП</label>
    </fieldset>

		<button type="submit">Зарегистрировать</button>
		
		<?php if(session()->getFlashdata('valid_email')):?>
		<div class="success"><?= session()->getFlashdata('valid_email') ?></div>
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
