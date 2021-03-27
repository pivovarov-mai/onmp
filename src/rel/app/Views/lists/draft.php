<?php foreach ($list as $row): ?>
	<li data-icon="edit">
		<a href='#UpdatePage' onclick="cardLoad('<?= $row['idcard'] ?>')">
			<h2><?= $row['order']?></h2>
			<p class="ui-li-aside"><strong><?= rus_date($row['date']) ?></strong></p>
		</a>
	</li>
<?php endforeach ?>
