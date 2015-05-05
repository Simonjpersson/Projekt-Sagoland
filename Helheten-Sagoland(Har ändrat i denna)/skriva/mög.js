
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