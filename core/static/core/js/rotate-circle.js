let el = document.getElementById('layer-1');
let elDisplay = el.children[0];

var deg = 0;

function rotate() {
    deg = (deg + 0.1) % 360
    elDisplay.style.transform = "rotate(" + deg + "deg)";
}

setInterval(rotate, 10);
