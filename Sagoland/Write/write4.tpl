<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Sagoland</title>
		<link href="/static/style.css" rel="stylesheet" type="text/css">
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
					<li><a href="/loggain">Skriv Saga</a></li>
					<li class='active'><a href="/read">Läs Saga</a></li>
					<li><a href="/">Startsida</a></li>	
					
				</ul>
			
			</div>
				<!--Hela bokens innehåll!-->

				<section>

					<!--Input text till Sagans namn-->
					
					<input type="text" id="Titel" value="Vad heter din saga?">
						
						<!--Hela bokens element!-->

						<div id="book">

							<img src="../static/book.png" alt="En bok">

								<!--Textarea som du skriver din text i, på bokens vänstra sida-->

								<textarea id="story_text" rows="24" cols="55" maxlength="500">Skriv din text här!</textarea>
									
									<!--Dropp elementet på bokens högrasida! enbart ett tomt div element-->

									<div id="dropbox" ondrop="drop(event)" ondragover="allowDrop(event)">

									</div>	
						</div>

						<!--knapparna som gör att elementen med "bilder", "text-färg" & "typsnitt" blir synliga/gömda.-->

							<button onclick="toggle_div_fun('picturebox');">Här finns bilder</button>

							<button onclick="toggle_div_fun('textchoose');">Välj färg på din text</button>

							<button onclick="toggle_div_fun('font_text');">Ändra stil på din text</button>

							<!-- Elementet som innehåller alla bilder och gör det möjligt att dra ifrån -->
							
							<div id="picturebox" ondrop="drop(event)" ondragover="allowDrop(event)">

								<img id="Girl" src="../static/girl.png" draggable="true" ondragstart="drag(event)">

								<img id="boy" src="../static/boy.png" draggable="true" ondragstart="drag(event)" >

								<img id="Bull" src="../static/Bull.png" draggable="true" ondragstart="drag(event)" >

								<img id="tree" src="../static/tree.png" draggable="true" ondragstart="drag(event)">

								<img id="cat" src="../static/cat.png" draggable="true" ondragstart="drag(event)">

								<img id="car" src="../static/car.png" draggable="true" ondragstart="drag(event)">

								<img id="firetruck" src="../static/firetruck.png" draggable="true" ondragstart="drag(event)">

								<img id="witch" src="../static/witch.png" draggable="true" ondragstart="drag(event)">

								<img id="sun" src="../static/sun.png" draggable="true" ondragstart="drag(event)">

								<img id="house" src="../static/house.png" draggable="true" ondragstart="drag(event)">
							</div>

										<!--Innehåller olika färgval för texten -->
										<div id="textchoose">

											<!--Listan med alla färger(bilder) & knappar för funktionen -->
											
											<ul class="change_text_style">

												<li><img src="../static/black.png" alt="Färgen svart">
													<button class="text_style_button" onclick="set_color_black();">Svart</button>
												</li>

												<li><img src="../static/red.png" alt="Färgen röd">
													<button class="text_style_button" onclick="set_color_red();">Röd</button>
												</li>

												<li><img src="../static/blue.png" alt="Färgen blå">
													<button class="text_style_button" onclick="set_color_blue();">Blå</button>
												</li>

												<li><img src="../static/orange.png" alt="Färgen orange">
													<button class="text_style_button" onclick="set_color_orange();">Orange</button>
												</li>

												<li><img src="../static/pink.png" alt="Färgen rosa">
													<button class="text_style_button" onclick="set_color_pink();">Rosa</button>
												</li>

												<li><img src="../static/green.png" alt="Färgen grön">
													<button class="text_style_button" onclick="set_color_green();">Grön</button>
												</li>

											</ul>
										</div>
												<!-- Innehåller de olika font alternativen(bild) & knappar för funktionen -->
												<div id="font_text">

													<ul class="change_text_style">

														<li><img src="../static/impact.png">
															<button class="text_style_button" onclick="set_font_impact();">Ändra typsnitt</button>
														</li>

														<li><img src="../static/georgia.png">
															<button class="text_style_button" onclick="set_font_georgia();">Ändra typsnitt</button>
														</li>

														<li><img src="../static/algerian.png">
															<button class="text_style_button" onclick="set_font_algerian();">Ändra typsnitt</button>
														</li>

														<li><img src="../static/comic.png">
															<button class="text_style_button" onclick="set_font_ComicSansMS();">Ändra typsnitt</button>
														</li>

													</ul>

												</div>
				</section>
		</div>
	</body>
</html>