<?php
$dir = scandir("cards_backup");
$i=1;
foreach ($dir as $dir_from) {
  $dir_to = sprintf("%09d",$i);
  $i++;
  mkdir("cards/$dir_to");
  copy("cards_backup/$dir_from/card.json", "cards/$dir_to/card.json");
}
?>
