<?php
function addtext($text)
{
	$output = str_replace("%","\%",$text);
	return "\\addtext{" . $output ."}\n";
}

function tex_from_post($post, $tex_file, $mp_tex)
{
	$tex_content = "\\documentclass{medkarta}\n";
//	foreach ($post as $parameter) 
//		$tex_content .= "\\addtext{$parameter}\n";
						$comma = "";
            $status_locales = "";
	for($i=1;$i<=134;$i+=1) {
		if(!isset($post[$i]))
			$post[$i] = "";
	}
	for($i=1;$i<=134;$i+=1) {
	/*if(array_key_exists("$i", $post))
						$tex_content .= addtext($post["$i"]);
					else
						$tex_content .= addtext("");*/
		switch ($i) {
			case 59:	if(($post["55"])!="" && ($post["58"])!="")
							$tex_content .= addtext($post["55"]-$post["58"]);
						else
							$tex_content .= addtext("");
			    		break;
			case 78:	
							if (isset($post['79']) && $post['79'] == "отрицательные")
								$tex_content .= addtext("");
							else
								if (isset($post['78']))
									$tex_content .= addtext($post['78']);
			    		break;
      case 103:	
          if(isset($post['103']) && $post['103']!=""){
						$status_locales .= "Вес=".$post['103']."кг";
						$comma = ", ";
					}
					break;
			case 104:	if(isset($post['104']) && $post['104']!="") {
							$status_locales .= $comma . "Рост=".$post['104']."см";
              $comma = ", ";
        }
					if(isset($post['104']) && isset($post['103']) && $post['104']!="" && $post['103']!=""){
            if(is_numeric($post['104']) && is_numeric($post['104'])) {
              $imt = round($post['103']*10000/($post['104']*$post['104']),0);
              $status_locales .= $comma . "ИМТ=" . $imt;
            }
					}
					break;
			case 105:	if(isset($post['105']) && $post['105']!="")
						$tex_content .= addtext($status_locales . $comma . $post['105']);
					else
						$tex_content .= addtext($status_locales);
					break;
      case 106:	
        $instruments = "";
        $comma = "";
      if(isset($post['106']) && $post['106']!="") {
        $instruments .= $post['106'];
        $comma = "; ";
      }
      if(isset($post['107']) && $post['107']!="") {
        $instruments .= $comma . "SpO2 " . $post['107'];
        $comma = "; ";
      }
      if(isset($post['108']) && $post['108']!="") {
        $instruments .= $comma . " " . $post['108'];
        $comma = "; ";
      }
        $tex_content .= addtext($instruments);
        $tex_content .= addtext($post['109'] . "{\par}" . $post['110'] . "{\par}" . $post['111'] . "{\par}" . $post['112'] . "{\par}" . $post['113']);
					$i = 113;
					break;
			case 133: if(isset($post['133']))	
					$tex_content .= addtext($post['133']);
					break;
			case 134: if(isset($post['134']))	
					$tex_content .= addtext($post['134']);
					break;
			default: 	if(array_key_exists("$i", $post))
						$tex_content .= addtext($post["$i"]);
					else
						$tex_content .= addtext("");
		}
	}
	$document = file_get_contents($mp_tex);
	$tex_content .= "\\begin{document}\n".$document ."\n\\end{document}\n";
	return file_put_contents($tex_file, $tex_content);
}
?>
