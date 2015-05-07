<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		

		<title>Sagoland</title>
		<link href="style.css" rel="stylesheet" type="text/css">
		<script src="javascript.js" type="text/javascript"></script>
	</head>
	
	<body>
		<div id="wrapper">
		
		
		<header>
			<img src="banner4.jpg" alt="Logga Sagoland" width="100%">
		</header>
			
			<div id='cssmenu'>
				<ul> 	
					
						<li><a href="contact1.html">Kontakta Oss</a></li>
						<li><a href="loggin.html">Skriv Saga</a></li>
						<li><a href="read.html">Läs Saga</a></li>
						<li class='active'><a href="index.html">Startsida</a></li>
					
				</ul>
			</div>
			
			
				<section id="content">
				
					
					
				<!--Dessa sektioner är vänster respektive höger del av sagoboksbilden-->
				<section class="left"><p></p></section>
					<form action = "/update" method = "POST">
				
						<p><label for "username">Användarnamn:</label></p>
						<p><input type = "text" name = "username"></p>
		
						<p><label for "mejl">E-postadress:</label></p>
						<p><input type = "text" name = "mejl"></p>

						<p><label for "password">Lösenord:</label></p>
						<p><input type = "text" name = "password"></p>

						<p><input type = "submit" value = "Spara"></p>		


								
				<section class="right"><p></p></section>
				
					
				</section>
			
		</div>
	</body>
</html>
