<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Sagoland</title>
		<link href="/static/stylewrite.css" rel="stylesheet" type="text/css">
		<script src="jquery-1.11.2..js"></script>
		<script src="jquery-ui.js"></script>
		<script src="javascriptwrite.js"></script>

		
		
	</head>
	
	<body>
		<div id="wrapper">
			
			<header>
				<img class="full" src="/static/banner4.jpg" alt= "Logga Sagoland">
			</header>
	
			<!--meny-->
			<div id='cssmenu'>
				<ul> 	
					
					<li><a href="/contact1/">Kontakta Oss</a></li>
					<li class='active'><a href="/">Skriv Saga</a></li>
					<li><a href="/read/">Läs Saga</a></li>
					<li><a href="/sagoland/">Startsida</a></li>	
					
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

												<li><img class= "color_size" src="picturewrite/bildcolorchoose/black.png" alt="Färgen svart" onclick="set_color_black();"></li>

												<li><img class= "color_size" src="picturewrite/bildcolorchoose/red.png" alt="Färgen röd" onclick="set_color_red();"></li>

												<li><img class= "color_size" src="picturewrite/bildcolorchoose/blue.png" alt="Färgen blå" onclick="set_color_blue();"></li>

												<li><img class= "color_size" src="picturewrite/bildcolorchoose/orange.png" alt="Färgen orange" onclick="set_color_orange();"></li>

												<li><img class= "color_size" src="picturewrite/bildcolorchoose/pink.png" alt="Färgen rosa" onclick="set_color_pink();"></li>

												<li><img class= "color_size" src="picturewrite/bildcolorchoose/green.png" alt="Färgen grön" onclick="set_color_green();"></li>

											</ul>
										</li>

													<!-- Innehåller de olika font alternativen(bild) & knappar för funktionen -->
							<li class="list_button" onclick="toggle_div_fun('font_text');">
							<p>Ändra uteseende på din text</p>
							</li>
												<li>
													<ul id="font_text">

														<li><img src="picturewrite/bildfonttext/impact.png" alt="typsnitt-Impact" onclick="set_font_impact();"></li>

														<li><img src="picturewrite/bildfonttext/georgia.png" alt="typsnitt-Georgia" onclick="set_font_georgia();"></li>

														<li><img src="picturewrite/bildfonttext/algerian.png" alt="typsnitt-Algerian" onclick="set_font_algerian();"></li>

														<li><img src="picturewrite/bildfonttext/comic.png" alt="typsnitt-Comic" onclick="set_font_ComicSansMS();"></li>
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
								
								<img class="move_image" src="picturewrite/bildpicturebox/girl.png" alt="Bild på Anja">

								<img class="move_image" src="picturewrite/bildpicturebox/boy.png" alt="Bild på en pojke">

								<img class="move_image" src="picturewrite/bildpicturebox/Bull.png" alt="Bild på en tjur">

								<img class="move_image" src="picturewrite/bildpicturebox/tree.png" alt="Bild på ett träd">

								<img class="move_image" src="picturewrite/bildpicturebox/cat.png" alt="Bild på en katt">

								<img class="move_image" src="picturewrite/bildpicturebox/car.png" alt="Bild på en bil">

								<img class="move_image" src="picturewrite/bildpicturebox/firetruck.png" alt=" Bild på en brandbil">

								<img class="move_image" src="picturewrite/bildpicturebox/witch.png" alt=" Bild på en häxa">

								<img class="move_image" src="picturewrite/bildpicturebox/sun.png" alt=" Bild på en sol">

								<img class="move_image" src="picturewrite/bildpicturebox/house.png" alt=" Bild på ett hus">

							</div>	
			</section>					
		</div>
	</body>
</html>