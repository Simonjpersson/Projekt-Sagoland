/*-- Funktionen som döljer bilder! */
function toggle_div_fun(id) {

	var divelement = document.getElementById(id)
	if(divelement.style.display == 'block')
		divelement.style.display = 'none';
	else
		divelement.style.display = 'block';
}

/*-- När du dubbelklickar på bilden så flyttar den upp till droppbox*/
function moveImg(e){
    if( $(e).parent().attr("id") == "picturebox" ){
        $(e).detach().appendTo('#dropbox');
    }
    else{
        $(e).detach().appendTo('#picturebox'); 
    }
    /*-- gör så att bilden går att flytta på */
    $(document).ready(function() {
  		$('.move_image').draggable({
    	cursor: 'move',
    	containment: '#dropbox'});
  
	});
}




function saveStoryTextAsFile(){

	var textToWrite = document.getElementById("story_text").value;
	var textFileAsBlob = new Blob([textToWrite], {type:'text/plain'});
	var fileNameToSaveAs = document.getElementById("inputFileNameToSaveAs").value;

	var downloadLink = document.createElement("a");
	downloadLink.download = fileNameToSaveAs;
	downloadLink.innerHTML = "Download File";
	if (window.webkitURL != null)

	{
		/* behöver för att chrome ska tillåta den att fungera*/

		downloadLink.href = window.webkitURL.createObjectURL(textFileAsBlob);
	}
	else
	{
		// Vid Firefox måste länken för att lägga till DOM innan man kan klicka */

		downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
		downloadLink.onclick = destroyClickedElement;
		downloadLink.style.display = "none";
		document.body.appendChild(downloadLink);
	}

	downloadLink.click();
}

function destroyClickedElement(event)
{
	document.body.removeChild(event.target);
}

function loadFileAsText()
{
	var fileToLoad = document.getElementById("fileToLoad").files[0];

	var fileReader = new FileReader();
	fileReader.onload = function(fileLoadedEvent) 
	{
		var textFromFileLoaded = fileLoadedEvent.target.result;
		document.getElementById("inputTextToSave").value = textFromFileLoaded;
	}

	fileReader.readAsText(fileToLoad, "UTF-8");
}

/*-- Alla färger du kan välja på för att ändra texten! */


function set_color_red(id) {
	document.getElementById("story_text").style.color = "#FF0D00"
}

function set_color_green(id) {
	document.getElementById("story_text").style.color = "#14D100"
}

function set_color_pink(id) {
	document.getElementById("story_text").style.color = "#F76F87"
}

function set_color_blue(id) {
	document.getElementById("story_text").style.color = "#0F4FA8"
}

function set_color_black(id) {
	document.getElementById("story_text").style.color = "#000000"
}

function set_color_orange(id) {
	document.getElementById("story_text").style.color = "#FF7A00"
}

/*-- Ändra typsnitt funktion --*/

function set_font_impact(id) {
	document.getElementById("story_text").style.fontFamily= "impact"
}

function set_font_georgia(id) {
	document.getElementById("story_text").style.fontFamily= "Georgia"
	
}

function set_font_algerian(id) {
	document.getElementById("story_text").style.fontFamily= "algerian"
}

function set_font_ComicSansMS(id) {
	document.getElementById("story_text").style.fontFamily= "Comic Sans MS"
}

