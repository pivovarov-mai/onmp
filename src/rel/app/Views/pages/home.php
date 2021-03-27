<div data-role="page" id="HomePage">
	<div data-role="header">
		<a href="/exit" rel="external" data-role="button" data-icon="power" data-iconpos="notext"></a>
		<h1>Мои карты</h1>
		<a href="#CreatePage" id="create_card_button" onclick="formEmpty()" data-role="button" data-icon="plus" data-iconpos="notext"></a>
	</div>
	<div role="main" class="ui-content">
		<div data-role="collapsibleset" data-inset="false">
			<div data-role="collapsible">
				<h3>Черновики</h3>
				<ul data-role="listview" data-inset="false" id="draft_listview">
				</ul>
			</div>
			<div data-role="collapsible">
				<h3>Готовые</h3>
				<ul data-role="listview" data-split-icon="edit" data-inset="false" id="ready_listview">
				</ul>
			</div>
			<div data-role="collapsible">
				<h3>Шаблоны</h3>
				<ul data-role="listview" data-split-icon="edit" data-inset="false" id="template_listview">
				</ul>
			</div>
			<div data-role="collapsible">
				<h3>Архив</h3>
				<ul data-role="listview" data-split-icon="delete" data-inset="false" id="archive_listview">
				</ul>
			</div>
		</div>
		
		<a href="#FeedbackPage" class="ui-btn ui-icon-mail ui-btn-icon-left">Письмо разработчику</a>
	</div>
	<div data-role="footer" data-position="fixed">
		<h1>Оплачен до <?= $paid_before ?></h1>
	</div>
</div>
