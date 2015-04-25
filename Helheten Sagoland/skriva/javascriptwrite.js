function doFirst(){
	Girl = document.getElementById('Girl');
	Girl.addEventListener("dragstart", startDrag, false);
	dropbox = document.getElementById('dropbox');
	dropbox.addEventListener("dragenter", function(e){e.preventDefault()},false);
	dropbox.addEventListener("dragover", function(e){e.preventDefault()},false);
	dropbox.addEventListener("drop", dropped,false);
}

function startDrag(e){
	var code ='<img id="Girl" src="girl.png">';
	e.dataTransfer.setData('Text', code);

}

function dropped(e){
	e.preventDefault();
	dropbox.innerHTML= e.dataTransfer.getData('Text');

}
window.addEventListener("load",doFirst, false);