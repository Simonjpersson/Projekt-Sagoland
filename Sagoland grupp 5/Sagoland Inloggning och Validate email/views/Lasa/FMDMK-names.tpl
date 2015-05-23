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
			<img class= "full" src="commondesign/banner4.jpg" alt="Logga Sagoland">
		</header>
		
<!--Navigations Meny-->			
			<div id='cssmenu'>
				<ul> 	
					
						<li><a href="../contact1.html">Kontakta Oss</a></li>
						<li><a href="../loggain.html">Skriv Saga</a></li>
						<li class='active'><a href="../read.html">Läs Saga</a></li>
						<li ><a href="../index.html">Startsida</a></li>
					
				</ul>
			
			</div>
		


			<section id="content">


				<!--Dessa sektioner är vänster respektive höger del av sagoboksbilden-->
				<a href="FMDMK-front.tpl#content"><section class="left"><p></p></section></a>
								
				<a href="FMDMK-1.tpl#content"><section class="right"><p></p></section></a>


				<!--Dessa sektioner är vänster respektive höger innehåll i sagoboken-->
				<section id="contentleft">
					<h2>Vill du byta namn på huvudkaraktärerna?</h2>
					<p><b>Ja!</b></p>
					<p>Fyll i nya namn och klicka på Okej-knappen. Sagan kommer nu starta med dina egna påhittade namn på huvudkaraktärerna! </p>
					<p><b>Nej!</b></p>
					<p>Klicka dig vidare på sidan så startar sagan med deras riktiga namn.</p>	
					
				</section>

				<section id="contentright">
					<p>
						<img src="FMDMK/emma-name.png" alt="Flickan Emma" class="storyimages">
						<img src="FMDMK/Kattis-name.png" alt="Katten Kattis" class="storyimages">
					</p>
					<form>
						<input type="text" name="name1" value= "">
						<input type="text" name="name2" value= "">
						<img src="FMDMK/Okej-knapp.png" alt="Okej" class="storyimages" id="okej-knapp">
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