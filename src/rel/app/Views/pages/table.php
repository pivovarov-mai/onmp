<form active="/table/">
<?php for ($i=0; $i<count($property); $i++): ?>
<div data-role="page" id="Page<?= $i ?>">
	<div data-role="header" data-position="fixed">
  <h1><?= $title ?></h1>
	</div>
	<div role="main" class="ui-content">
    <fieldset class="form-group" data-role="controlgroup">
      <legend><?= $property[$i]->title ?></legend>
      <?php foreach ($property[$i]->reaction as $prop): ?>
      <label>
      <input type="radio" class="form-check-input <?= $i+1 != count($property) ? "next-input" : "last-input" ?>" name="<?= $property[$i]->title ?>" id="<?= $i."-".$j ?>" value="<?= $prop->mark ?>">
      <?= $prop->name ?></label>
      <?php endforeach; ?>
	  </fieldset>
	</div>
	<div data-role="footer" data-position="fixed">
		<div data-role="navbar">
		</div>
	</div>
</div>
<?php endfor; ?>  
</form>
