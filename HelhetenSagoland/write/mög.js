
	function startDrag(e) {
				// determine event object
				if (!e) {
					var e = window.event;
				}
                if(e.preventDefault) e.preventDefault();

				// IE uses srcElement, others use target
				targ = e.target ? e.target : e.srcElement;

				if (targ.className != 'dragme') {return};
				// calculate event X, Y coordinates
					offsetX = e.clientX;
					offsetY = e.clientY;

				// assign default values for top and left properties
				if(!targ.style.left) { targ.style.left='0px'};
				if (!targ.style.top) { targ.style.top='0px'};

				// calculate integer values for top and left 
				// properties
				coordX = parseInt(targ.style.left);
				coordY = parseInt(targ.style.top);
				drag = true;

				// move div element
					document.onmousemove=dragDiv;
                return false;
				
			}

			function dragDiv(e) {
				if (!drag) {return};
				if (!e) { var e= window.event};
				// var targ=e.target?e.target:e.srcElement;
				// move div element
				targ.style.left=coordX+e.clientX-offsetX+'px';
				targ.style.top=coordY+e.clientY-offsetY+'px';
				return false;
			}

			function stopDrag() {
				drag=false;
			}
			
			window.onload = function() {
				document.onmousedown = startDrag;
				document.onmouseup = stopDrag;
			}


		

			// target elements with the "draggable" class
interact('.draggable')
  .draggable({
    // enable inertial throwing
    inertia: true,
    // keep the element within the area of it's parent
    restrict: {
      restriction: "parent",
      endOnly: true,
      elementRect: { top: 0, left: 0, bottom: 1, right: 1 }
    },

    // call this function on every dragmove event
    onmove: dragMoveListener,
    // call this function on every dragend event
    onend: function (event) {
      var textEl = event.target.querySelector('p');

      textEl && (textEl.textContent =
        'moved a distance of '
        + (Math.sqrt(event.dx * event.dx +
                     event.dy * event.dy)|0) + 'px');
    }
  });

  function dragMoveListener (event) {
    var target = event.target,
        // keep the dragged position in the data-x/data-y attributes
        x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx,
        y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy;

    // translate the element
    target.style.webkitTransform =
    target.style.transform =
      'translate(' + x + 'px, ' + y + 'px)';

    // update the posiion attributes
    target.setAttribute('data-x', x);
    target.setAttribute('data-y', y);
  }

  // this is used later in the resizing demo
  window.dragMoveListener = dragMoveListener;






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

    else{
        $(elem).detach().appendTo('#picturebox'); 
    }

    if( 


        $(document).ready(function() {
    // sets draggable the elements with id="im"
    $('#Girl').draggable({
    cursor: 'move',        // sets the cursor apperance
    containment: '#dropbox'});    // sets to can be dragged only within "#drg" element
  
  });
}
function moveback(elem){
    $(elem).parent().attr("id") == "dropbox"){
    $(elem).detach().appendTo('#picturebox');
}



          <!--Input text till Sagans namn-->
          
          


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

function moveImg(e){
    // Clear position properties added by dregging
    $(e).css({ "top": "auto", "bottom": "auto", "left": "auto", "right": "auto" });
    
    if( $(e).parents("#picturebox").length != 0 ){
        $(e).detach().appendTo('#dropbox');
    }
    else if( $(e).parents("#dropbox").length != 0 ){
        $(e).detach().appendTo('#picturebox'); 
    }
}

$(document).ready(function() {
    $('.move_image').draggable({
        cursor: 'move',
        containment: '#dropbox'});
    $(#picturebox).on('dblclick', '.move_image', function(){
        moveImg($(this));
    });
});




 ondblclick="moveImg(this)"



              
              <li class="list_button"><button onclick="saveStoryTextAsFile('');">Spara din saga</button></li>
              <li class="list_button"><input id="inputFileNameToSaveAs" value="Vad heter din saga"></input></li>
              <li class="list_button"><button onclick="loadFileAsText()">Ladda en sparad saga</button></li>
              <li class="list_button"><input type="file" id="fileToLoad"></li>







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