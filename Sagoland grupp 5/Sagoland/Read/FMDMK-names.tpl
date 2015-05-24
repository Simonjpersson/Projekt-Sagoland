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
	
			<img src="../static/banner4.jpg" alt="Logga Sagoland" width="100%">
								
		</header>
		
<!--Navigations Meny-->			
			<div id='cssmenu'>
				<ul> 	
					
						<li><a href="/contact">Kontakta Oss</a></li>
						<li><a href="/loggain">Skriv Saga</a></li>
						<li class='active'><a href="/read">Läs Saga</a></li>
						<li ><a href="/">Startsida</a></li>
					
				</ul>
			
			</div>
		


			<section id="content">


				<!--Dessa sektioner är vänster respektive höger del av sagoboksbilden-->
				<section class="left"><p></p></section>
								
				<section class="right"><p></p></section>


				<!--Dessa sektioner är vänster respektive höger innehåll i sagoboken-->
				<section id="contentleft">
					<h2>Vill du byta namn på huvudkaraktären?</h2>
					<p><b>Ja!</b></p>
					<p>Fyll i nytt namn och klicka på 'Starta äventyret' med ditt eget påhittade namn på huvudkaraktären! </p>
					<p><b>Nej!</b></p>
					<p>Klicka direkt på 'Starta äventyret'.</p>	
					
				</section>

				<section id="contentright">
					<p>
						<img src="../static/emma-name.png" alt="Flickan Emma" class="storyimages">
						<img src="../static/Kattis-name.png" alt="Katten Kattis" class="storyimages">
					</p>
					<form action="FMDMK-front" method="POST">
						<p><label for "name">Namn på flickan:</label></p>
						<input type="text" name="name" value="Emma">
						
						<input type="submit" value= "Starta äventyret!"></a>
					</form>
					
				</section>	
				

			</section>



			
		</div>
	</body>
</html>