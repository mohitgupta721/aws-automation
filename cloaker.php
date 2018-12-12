<?php

//$array_of_urls = file($file, FILE_IGNORE_NEW_LINES);
$array_of_urls=fopen("members.txt", "r");

while (!feof($array_of_urls))
{
	$urls_to_cloak=fgets($array_of_urls);
	$api_url='https://client.justcloakit.com/nimda/urltocloakapi.php'; //to debug and see all POST data as justcloakit get it, send request to api-debug.php

$data = array(
	'call' => 'api', // DO NOT CHANGE
	'id'  => '268140', // YOUR CAMPAIGN ID
	'user_id' => 'wwsuugea4eupc0npcnwv3il3a', // YOUR USER ID
	'username' => 'ankushgupta.delhi', // YOUR USERNAME
	'password' => 'Miti@kapoor@12',  // YOUR PASSWORD
	'url_to_cloak' => $urls_to_cloak, // THE URL TO CLOAK
	'mobile_url' => '',  // THE MOBILE URL TO CLOAK (if you have mobile url set, add it here)
	'tablet_url' => '',  // THE TABLET URL TO CLOAK (if you have tablet url set, add it here)
	'mac_url' => '',   // THE MAC URL TO CLOAK (if you have mac url set, add it here)
	'submit' => true // DO NOT CHANGE

);

/*
Start cURL
=====================
*/
$ch = curl_init();
curl_setopt($ch,CURLOPT_URL, $api_url);
curl_setopt($ch,CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch,CURLOPT_POST, true);
curl_setopt($ch,CURLOPT_POSTFIELDS, http_build_query($data));
$result = curl_exec($ch);
curl_close($ch); // response
echo $result;
sleep(900);


}


  ?>

