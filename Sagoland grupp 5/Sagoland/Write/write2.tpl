<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Sagoland</title>
		<link href="/static/style.css" rel="stylesheet" type="text/css">
		<script src="/static/jquery-1.11.2..js"></script>
		<script src="/static/jquery-ui.js"></script>
		<script src="/static/javascriptwrite.js"></script>

		
		
	</head>
	
	<body>
		<div id="wrapper">
			
			<header>
				<img src="/static/banner4.jpg" alt="Logga Sagoland" width="100%">
			</header>
	
			<!--meny-->
			<div id='cssmenu'>
				<ul> 	
					<li><a href="/contact">Kontakta Oss</a></li>
					<li class='active'><a href="/loggain">Skriv Saga</a></li>
					<li><a href="/read">Läs Saga</a></li>
					<li><a href="/">Startsida</a></li>	
					
				</ul>
			
			</div>
			<section class="content">

					<div id="function_button">
						<!--knapparna som gör att elementen med "bilder", "text-färg" & "typsnitt" blir synliga/gömda.-->
						<ul id="meny_button">

							<li class="list_button" onclick="toggle_div_fun('picturebox');">
							<p>Bilder till Sagan</p>
							</li>

															<!--Innehåller olika färgval för texten -->
							<li class="list_button" onclick="toggle_div_fun('colorchoose');">
							<p>Ändra färg på din text</p> 
							</li>
										
										<li>
											<ul id="colorchoose">

												<li><img class= "color_size" src="../static/black.png" alt="Färgen svart" onclick="set_color_black();"></li>

												<li><img class= "color_size" src="../static/red.png" alt="Färgen röd" onclick="set_color_red();"></li>

												<li><img class= "color_size" src="../static/blue.png" alt="Färgen blå" onclick="set_color_blue();"></li>

												<li><img class= "color_size" src="../static/orange.png" alt="Färgen orange" onclick="set_color_orange();"></li>

												<li><img class= "color_size" src="../static/pink.png" alt="Färgen rosa" onclick="set_color_pink();"></li>

												<li><img class= "color_size" src="../static/green.png" alt="Färgen grön" onclick="set_color_green();"></li>

											</ul>
										</li>

													<!-- Innehåller de olika font alternativen(bild) & knappar för funktionen -->
							<li class="list_button" onclick="toggle_div_fun('font_text');">
							<p>Ändra uteseende på din text</p>
							</li>
												<li>
													<ul id="font_text">

														<li><img src="../static/impact.png" alt="typsnitt-Impact" onclick="set_font_impact();"></li>

														<li><img src="../static/georgia.png" alt="typsnitt-Georgia" onclick="set_font_georgia();"></li>

														<li><img src="../static/algerian.png" alt="typsnitt-Algerian" onclick="set_font_algerian();"></li>

														<li><img src="../static/comic.png" alt="typsnitt-Comic" onclick="set_font_ComicSansMS();"></li>
													</ul>
												</li>	

									<!--Spara sagan och kunna ladda den genom javascript/blob/-->
							<li class="list_button" onclick="saveTextAsFile()">
							<p>Spara din Saga</p>
							</li>						
					</div>

						<!--namnger din saga !-->
						<input id="Title" type="text" maxlength="55" value="Vad heter din saga?">
		
						<!--Hela bokens element!-->

						<div id="book">

								<!--Textarea som du skriver din text i, på bokens vänstra sida-->

								<textarea id="story_text" placeholder="Skriv din Saga här!" rows="24" cols="55" maxlength="500"></textarea>
									
									<!--Dropp elementet på bokens högrasida! enbart ett tomt div element-->

									<div id="dropbox"></div>	
						</div>

							<!-- Elementet som innehåller alla bilder och gör det möjligt att dra ifrån -->
							 <div id="arrowright"><a href="read.html"></a></div>
							
							<div id="picturebox">
								
								<img class="move_image" src="../static/girl.png" alt="Bild på Anja">

								<img class="move_image" src="../static/boy.png" alt="Bild på en pojke">

								<img class="move_image" src="../static/Bull.png" alt="Bild på en tjur">

								<img class="move_image" src="../static/tree.png" alt="Bild på ett träd">

								<img class="move_image" src="../static/cat.png" alt="Bild på en katt">

								<img class="move_image" src="../static/car.png" alt="Bild på en bil">

								<img class="move_image" src="../static/firetruck.png" alt=" Bild på en brandbil">

								<img class="move_image" src="../static/witch.png" alt=" Bild på en häxa">

								<img class="move_image" src="../static/sun.png" alt=" Bild på en sol">

								<img class="move_image" src="../static/house.png" alt=" Bild på ett hus">

							</div>	
			</section>					
		</div>
	</body>
</html>