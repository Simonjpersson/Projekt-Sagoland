/*-- Funktionen som döljer bilder! */

function toggle_div_fun(id) {

	var divelement = document.getElementById(id)
	if(divelement.style.display == 'block')
		divelement.style.display = 'none';
	else
		divelement.style.display = 'block';
}
/*-- Funktionen som gör det möjligt att dra och släppa bilder */

function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
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


window.addEventListener("load")