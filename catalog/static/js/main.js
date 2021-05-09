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
  $("#categories .card" ).hover(function() {
    $(this).addClass('shadow-lg').css('cursor', 'pointer'); 
  }, function() {
    $(this).removeClass('shadow-lg');
  });
});

// make sticky header smaller when customer scrolls the page down
$(window).scroll(function() {
  if ($(this).scrollTop() > 250){  
      $('#top-bar').addClass("sticky");
  } else{
      $('#top-bar').removeClass("sticky");
  }
});

// add dynamic year
const date = new Date();
document.querySelector('span.year').innerHTML = date.getFullYear();

//fetch google maps
let map;
function initMap() {
  if (document.getElementById("googleMap") != null) {
    map = new google.maps.Map(document.getElementById("googleMap"), {
      center: { lat: 47.02124873693511, lng: 23.87716751017298 },
      zoom: 16,
    });
  }
}

//Owl carousel
$('.owl-carousel').owlCarousel({
  loop:true,
  nav:false,
  autoplay:true,
  margin:100,
  responsiveClass:true,
  responsive:{
    0:{
      items:1
    },
    600:{
      items:3
    },
    1000:{
      items:4
    }
  }
});