

<?php
$file = fopen("members.txt", "r");
$members = array();

while (!feof($file)) {
   $members[] = fgets($file);
}

echo $members.length
fclose($file);

//var_dump($members);
?>

