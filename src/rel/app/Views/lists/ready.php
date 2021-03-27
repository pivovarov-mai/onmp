<?php foreach ($list as $row): ?>
	<li data-icon="edit">
		<a href='/download/<?= $row['idcard'] ?>/<?= $row['order'] ?>' target='_blank'>
			<h2><?= $row['order']?></h2>
			<p class="ui-li-aside"><strong><?= rus_date($row['date']) ?></strong></p>
		</a>
		<a href='#UpdatePage' onclick="cardLoad('<?= $row['idcard'] ?>')">
			<?= $row['order'] ?>
		</a>
	</li>
<?php endforeach ?>
