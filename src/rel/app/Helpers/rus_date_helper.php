<?php

use CodeIgniter\I18n\Time;

function rus_date($date)
{
	$result = new Time($date);
	return $result->format('d.m.y');
}
