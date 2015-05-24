/*-- Funktionen som klickar fram bilderna till sagan och döljer dem! */
function toggle_div_fun(id) {

	var divelement = document.getElementById(id)
	if(divelement.style.display == 'block')
		divelement.style.display = 'none';
	else
		divelement.style.display = 'block';
}

/* JQ för att kunna skicka bilderna till och från DIV, samt dra i bilderna */
$(document).ready(function() {
    
    var moveImg = function (e){
        var $el = $(e);
        var $dropbox = $('#dropbox');
        
        /* Tar bort positioneringen på bilderna */

        $el.css({ "top": "auto", "bottom": "auto", "left": "auto", "right": "auto" });
        
        if( $el.parents("#picturebox").length !== 0 ){
            $el.detach().appendTo('#dropbox');
            
            /* postitioneringen inom dropbox diven som top-bot/höjd-bred. */
            
            var dropbox_bottom = $dropbox.offset().top + $dropbox.height();
            var dropbox_right = $dropbox.offset().left + $dropbox.width();
            if ( $el.offset().top + $el.height() > dropbox_bottom ||
                $el.offset().left + $el.width() > dropbox_right ) {
                
                /* Z-indexet som gör det möjligt att img kan ligga ovanpå varandra inom div elementet för att undvika "overflow" */ 
                
                $el.css("z-index", "+=1");
                $el.offset({ 
                    top: dropbox_bottom - $el.height(),
                    right: $dropbox.offset().left          
                });
            }
        }
        /* Z-indexet som gör det möjligt att img kan ligga ovanpå varandra inom div elementet för att undvika "overflow" */
        else if( $el.parents("#dropbox").length !== 0 ){
            $el.detach().appendTo('#picturebox'); 
            
            $el.css("z-index", "auto");
        }
    };
    /* gör så att img kan dras inom div elementet dropbox*/

    $('.move_image').draggable({
        cursor: 'move',
        containment: '#dropbox'
    });
    /* Måste ha för att divdropbox ska kunna taemot bilderna */
    $('#dropbox').droppable({
        
    });    
    /* När du dbclickar körs funktionen move_image = flytta img och sedan dra i dropbox */
    $(document).on('dblclick', '.move_image', function(){
        moveImg($(this));
    });
    
});


/*-- Alla färger du kan välja på för att ändra texten! startar igenom klick event i HTML anroppar funktionen*/


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



function saveTextAsFile()
{
    var textToWrite = document.getElementById("story_text").value;
    var textFileAsBlob = new Blob([textToWrite], {type:'text/plain'});
    var fileNameToSaveAs = document.getElementById("Title").value;

    var downloadLink = document.createElement("a");
    downloadLink.download = fileNameToSaveAs;
    downloadLink.innerHTML = "Download File";
    if (window.webkitURL != null)
    {
        // Chrome allows the link to be clicked
        // without actually adding it to the DOM.
        downloadLink.href = window.webkitURL.createObjectURL(textFileAsBlob);
    }
    else
    {
        // Firefox requires the link to be added to the DOM
        // before it can be clicked.
        downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
        downloadLink.onclick = destroyClickedElement;
        downloadLink.style.display = "none";
        document.body.appendChild(downloadLink);
    }

    downloadLink.click();
}

