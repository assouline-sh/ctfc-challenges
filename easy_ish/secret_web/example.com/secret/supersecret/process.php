<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
	$ans = $_POST["ans"];
	if (preg_match('/<script>alert\(.*\)<\/script>/', $ans)) {
		echo "<script>alert('CTF{traversing_new_paths}');</script>";
	}
	else {
		echo "Hmm. Not what I was looking for. If you want to be alerted of the flag, try something else...";
	}
}
?>
