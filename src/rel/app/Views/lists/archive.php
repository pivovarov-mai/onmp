<?php foreach ($list as $row): ?>
	<li>
		<a href='#UpdatePage' onclick="cardLoad('<?= $row['idcard'] ?>')">
			<h2><?= $row['order']?></h2>
			<p class="ui-li-aside"><strong><?= rus_date($row['date']) ?></strong></p>
		</a>
		<a onclick="cardDelete('<?= $row['idcard'] ?>')" class="delete"><?= $row['order'] ?></a>
	</li>
<?php endforeach ?>
