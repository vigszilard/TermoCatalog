$(document).ready(function() {
  console.log("document is ready");

  // change icon logo depending on theme preference (dark/light mode)
  if (!window.matchMedia)
      return;
  var current = $('head > link[rel="icon"][media]');
  $.each(current, function(i, icon) {
    var match = window.matchMedia(icon.media);
    function swap() {
      if (match.matches) {
        current.remove();
        current = $(icon).appendTo('head');
      }
    }
    match.addEventListener('change', swap);
    swap();
  });
   
  // add shadow to categories on hover
  $( ".card" ).hover(function() {
    $(this).addClass('shadow-lg').css('cursor', 'pointer'); 
  }, function() {
    $(this).removeClass('shadow-lg');
  });
});

// make sticky header smaller when customer scrolls the page down
$(window).scroll(function() {
  if ($(this).scrollTop() > 250){  
      $('#top-bar').addClass("sticky");
  }
  else{
      $('#top-bar').removeClass("sticky");
  }
});

// add dynamic year
const date = new Date();
document.querySelector('span.year').innerHTML = date.getFullYear();