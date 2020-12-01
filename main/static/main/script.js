// When the user scrolls down 55px from the top of the document, resize the navbar's padding and the logo's font size
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 30 || document.documentElement.scrollTop > 40) {
    document.getElementsByClassName('logo-scroll')[0].setAttribute(
      "style", "display: block;"
    )
    document.getElementsByClassName('top')[0].style.display='block';
  } else {
    document.getElementsByClassName('logo-scroll')[0].setAttribute(
      "style", "display: none;"
    )
    document.getElementsByClassName('top')[0].style.display='block';
  }
}
//Move to top of the page
function topFun() {
  document.body.scrollTop = 0; 
  document.documentElement.scrollTop = 0;
}

function getcss(element){
  var s = "";
  var p = ["position", "margin", "color", "padding"];
  var x = getComputedStyle(element);
  for (var i = 0;i < x.length; i++){
    for (var j = 0; j < p.length; j++){
      if (x[i] == p[j])
        s+=x[i] + ': ' + x.getPropertyValue(x[i]) + ';';
    }
  }
  return s;
}
function x(element) {
  var e = document.getElementsByClassName(element)[0];
  if (e.style.display == 'none'){
    e.style.display = 'block';
  }
  else{
    e.style.display = 'none';
  }
}
