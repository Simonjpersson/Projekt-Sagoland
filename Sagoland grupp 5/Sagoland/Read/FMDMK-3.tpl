<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Sagoland</title>
		<link href="../static/style.css" rel="stylesheet" type="text/css">
		<script src="../static/javascript.js" type="text/javascript"></script>
	</head>
	
<body>
	<div id="wrapper">
		<header>
			<img class= "full" src="../static/banner4.jpg" alt="Logga Sagoland">
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
				<a href="FMDMK-2" id="content"><section class="left"><p></p></section></a>
								
				<a href="FMDMK-4" id="content"><section class="right"><p></p></section></a>


				<!--Dessa sektioner är vänster respektive höger innehåll i sagoboken-->
				<section id="contentleft">
					<p><img src="../static/sida3.png" alt="Flickan fått kritor och hoppar upp och ner." class="storyimages"></p>	
				</section>

				<section id="contentright">
					{{text}}
				</section>	
				

			</section>



			
		</div>
	</body>
</html>