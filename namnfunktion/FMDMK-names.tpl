<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Sagoland</title>
		<link href="/static/style.css" rel="stylesheet" type="text/css">
		<script src="javascript.js" type="text/javascript"></script>
	</head>
	
<body>
	<div id="wrapper">
		<header>
	
			<img src="/static/banner4.jpg" alt="Logga Sagoland" width="100%">
								
		</header>
		
<!--Navigations Meny-->			
			<div id='cssmenu'>
				<ul> 	
					
						<li><a href="../contact1.html">Kontakta Oss</a></li>
						<li><a href="../loggin.html">Skriv Saga</a></li>
						<li class='active'><a href="../read.html">Läs Saga</a></li>
						<li ><a href="../index.html">Startsida</a></li>
					
				</ul>
			
			</div>
		


			<section id="content">


				<!--Dessa sektioner är vänster respektive höger del av sagoboksbilden-->
				<a href="FMDMK-front" id="content"><section class="left"><p></p></section></a>
								
				<section class="right"><p></p></section>


				<!--Dessa sektioner är vänster respektive höger innehåll i sagoboken-->
				<section id="contentleft">
					<h2>Vill du byta namn på huvudkaraktärerna?</h2>
					<p><b>Ja!</b></p>
					<p>Fyll i nya namn och klicka på 'Starta äventyret' med dina egna påhittade namn på huvudkaraktärerna! </p>
					<p><b>Nej!</b></p>
					<p>Klicka direkt på 'Starta äventyret'.</p>	
					
				</section>

				<section id="contentright">
					<p>
						<img src="/static/emma-name.png" alt="Flickan Emma" class="storyimages">
						<img src="/static/Kattis-name.png" alt="Katten Kattis" class="storyimages">
					</p>
					<form action = "/FMDMK-1" method = "POST">
						<p><label for "name1">Namn på flickan:</label></p>
						<input type="text" name="name1">
						<p><label for "name1">Namn på katten:</label></p>
						<input type="text" name="name2">
						<input type="submit" value= "Starta äventyret!">
					</form>
					
				</section>	
				

			</section>



			<footer>
				<p> Hemsidan är skapad som ett projekt i kursen Systemutveckling på Malmö Högskola</p>
				<p>Coypright 2015</p>
				
			</footer>
		</div>
	</body>
</html>