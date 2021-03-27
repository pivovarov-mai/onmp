<?php foreach ($list as $row): ?>
	<li>
		<a href='#CreatePage' onclick="templateLoad('<?= $row['idcard'] ?>')">
			<h2><?= $row['order']?></h2>
		</a>
		<a href='#UpdatePage' onclick="cardLoad('<?= $row['idcard'] ?>')">Редактировать</a>
	</li>
<?php endforeach ?>
