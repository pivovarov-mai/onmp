<div data-role="page" id="CreatePage">
	<div data-role="header" data-position="fixed">
		<a href="#HomePage" data-role="button" data-icon="home" data-iconpos="notext"></a>	
		<h1>Создание</h1>
	</div>
	<div role="main" class="ui-content">
		<form id="form_create">
			
			<div class="ui-field-contain">
				<label for="order">Название:</label>
				<input type="text" name="order" id="order" placeholder="Номер наряда или имя шаблона" value="">
			</div>
				
			<!--<div class="ui-field-contain">
				<fieldset data-role="controlgroup" data-type="horizontal">
					<legend></legend>
					<input type="radio" name="status" id="status-draft" value="draft" checked="checked">
					<label for="status-draft">Черновик</label>
					<input type="radio" name="status" id="status-template" value="template">
					<label for="status-template">Шаблон</label>
				</fieldset>
			</div>-->
				
			<!--<div class="ui-field-contain">
				<label for="date">Дата:</label>
				<input type="date" name="date" id="date"></input>
			</div>-->
				
			<!--<div class="ui-field-contain">
				<div class="ui-field-contain">
					<label for="select-template">Шаблон</label>
					<select name="template" id="select-template" data-native-menu="false" class="filterable-select">
						<option value="">Пример 1</option>
						<option value="">Пример 2</option>
					</select>
				</div>
			</div>-->
				
			<div class="ui-field-contain">
				<label for="comment">Комментарий:</label>
				<input type="text" name="comment" id="comment" placeholder="" value="">
			</div>
			
			<a href="#ZhalobyPage" id="create_button" class="ui-btn">Создать</a>
			
		</form>
	</div>
</div>