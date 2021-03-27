<?php foreach ($list as $row): ?>
	<li>
		<a href='#UpdatePage' onclick="formLoad('<?= $row['idcard'] ?>')">
			<h2><?= $row['order']?></h2>
			<p class="ui-li-aside"><strong><?= $row['date'] ?></strong></p>
		</a>
		<a href='/card/download/<?= $row['idcard'] ?>' target='_blank'><?= $row['order'] ?></a>
	</li>
<?php endforeach ?>
