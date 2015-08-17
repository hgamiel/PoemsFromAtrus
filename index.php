<html>
<!-- By Hannah Gamiel -->
<head>
<title>Moments With Atrus</title>
</head>
<body>

	<?php 

	$command = escapeshellcmd('/usr/custom/test.py');
	$output = shell_exec($command);
	echo $output;

	?>

</body>
</html>
