<div data-role="page" id="UpdatePage">
	<div data-role="panel" id="ZhalobyPanelUpdate" data-position="left">
		<h2>Жалобы</h2>
		<div class="zhaloby_content"></div>
		<a href="#ZhalobyPage" class="ui-btn ui-btn-inline">Изменить</a>
		<a data-rel="close" class="ui-btn ui-btn-inline">Отмена</a>
	</div>
	<div data-role="panel" id="AnamnezPanelUpdate" data-position="left">
		<h2>Анамнез</h2>
		<div class="anamnez_content"></div>
		<a href="#AnamnezPage" class="ui-btn ui-btn-inline">Изменить</a>
		<a data-rel="close" class="ui-btn ui-btn-inline">Отмена</a>
	</div>
	<div data-role="header" data-position="fixed">
		<a href="#HomePage" data-role="button" data-icon="home" data-iconpos="notext"></a>
		<h1>Изменение</h1>
		<a href="#ZhalobyPage" data-role="button" data-icon="carat-r" data-iconpos="notext"></a>
	</div>
	<div role="main" class="ui-content">
		<form id="form_update">
		
			<div class="ui-field-contain">
				<label for="update_order">Название:</label>
				<input type="text" name="order" id="update_order" placeholder="Номер наряда или имя шаблона" value="">
			</div>
			
			<div class="ui-field-contain">	
				<fieldset data-role="controlgroup" data-type="horizontal" data-mini="false">
					<legend for="update_status">Статус:</legend>
					<input type="radio" name="update_status" id="update_status_draft" value="draft" checked="checked">
					<label for="update_status_draft">Черновик</label>
					<input type="radio" name="update_status" id="update_status_ready" value="ready">
					<label for="update_status_ready">Заполнена</label>
					<input type="radio" name="update_status" id="update_status_template" value="template">
					<label for="update_status_template">Шаблон</label>
					<input type="radio" name="update_status" id="update_status_archive" value="archive">
					<label for="update_status_archive">Архивная</label>
				</fieldset>
			</div>
			
			<div class="ui-field-contain">
				<label for="update_date">Дата:</label>
				<input type="date" name="date" id="update_date"></input>
			</div>
			
			<div class="ui-field-contain">
				<label for="update_comment">Комментарий:</label>
				<input type="text" name="comment" id="update_comment" placeholder="" value="">
			</div>
			
			<a href="#HomePage" id="update_button" class="ui-btn">Сохранить</a>
			
		</form>
	</div>
	<div data-role="footer" data-position="fixed">
		<div data-role="navbar" >
			<ul>
				<li><a href="#ZhalobyPanelUpdate" data-icon="comment">Жалобы</a></li>
				<li><a href="#AnamnezPanelUpdate" data-icon="calendar">Анамнез</a></li>
				<li><a href="#TocPage" data-icon="bullets">Карта</a></li>
				<li><a href="#UpdatePage" data-icon="edit" class="ui-btn-active">Сохранить</a></li>
			</ul>
		</div>
	</div>
</div>
