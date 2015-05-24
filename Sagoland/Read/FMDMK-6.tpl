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
				<a href="FMDMK-5" id="content"><section class="left"><p></p></section></a>
								
				<section class="right"><p></p></section>


				<!--Dessa sektioner är vänster respektive höger innehåll i sagoboken-->
				<section id="contentleft">
					{{text}}
					
				</section>

				<section id="contentright">
					<p>
						<a href="FMDMK-7" id="content"><img src="../static/sida6-strand.png" alt="Flickan ritar en strand" class="storyimages"></a>
						<a href="FMDMK-8" id="content"><img src="../static/sida6-hund.png" alt="Flickan ritar en hund" class="storyimages"></a>
					</p>
					<p>
						<a href="FMDMK-9" id="content"><img src="../static/sida6-paris.png" alt="Flickan ritar Eiffeltornet" class="storyimages"></a>
						<a href="FMDMK-10" id="content"><img src="../static/sida6-gunga.png" alt="Flickan en gunga" class="storyimages"></a>
					</p>
				</section>	
				

			</section>



			
		</div>
	</body>
</html>