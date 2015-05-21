<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		

		<title>Sagoland</title>
		<link href="/static/style.css" rel="stylesheet" type="text/css">
		<script src="/static/javascript.js" type="text/javascript"></script>
	</head>
	
	<body>
		<div id="wrapper">
		
			<header>
	
				<img src="/static/banner4.jpg" alt="Logga Sagoland" width="100%">
				
				
			</header>
			
			<div id='cssmenu'>
				<ul> 	
					<li><a href="/contact1/">Kontakta Oss</a></li>
					<li><a href="/">Skriv Saga</a></li>
					<li><a href="/read/">Läs Saga</a></li>
					<li class='active'><a href="/sagoland/">Startsida</a></li>	
					
				</ul>
			
			</div>
		



			<section id="content">


				<!--Dessa sektioner är vänster respektive höger del av sagoboksbilden-->
				<section class="left"><p></p></section>
								
				<section class="right"><p></p></section>


				<!--Dessa sektioner är vänster respektive höger innehåll i sagoboken-->
				<section id="contentleft">
					<h2>Hej!</h2>
					<p>
						För att kunna skriva en saga och publicera den måste du vara inloggad på Sagoland. Vill du endast testa att skriva en saga utan att publicera den så klicka <a href="xxxlänk till skriva-sidanxxx">här</a>.
					</p>

					<h3>Logga in</h3>
					<form action = "/update" method = "POST">
						<p>
							<label for "username">Användarnamn:</label>
							<input type = "text" name = "username">
						</p>
						<p>
							<label for "password1">Lösenord:</label>
							<input type = "text" name = "password1">
						</p>
						<p><input type = "submit" value = "Logga in"></p>
					
				</section>

				<section id="contentright">
					
					<h3>Ändra din information</h3>
					<form action = "/update" method = "POST">
						<p>
							<label for "username">Användarnamn:</label>
							<input type = "text" name = "username">
						</p>
						<p>
							<label for "mejl">E-postadress:</label>
							<input type = "text" name = "mejl">
						</p>
						<p>
							<label for "password1">Lösenord:</label>
							<input type = "text" name = "password1">
						</p>
						<p>
							<label for "password2">Bekräfta lösenord:</label>
							<input type = "text" name = "password2">
						</p>

						<p>
							<label for "password2"> </label>
							
						</p>
						<p><input type = "submit" value = "Ändra information"></p>	


				</section>	
				

			</section>



		</div>
	</body>
</html>