$(document).ready(function() {

  // Project - change icon logo depending on theme preference (dark/light mode)
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

  // Category page - add shadow to cards on hover
  $("#categories .card" ).hover(function() {
    $(this).addClass('shadow-lg').css('cursor', 'pointer');
  }, function() {
    $(this).removeClass('shadow-lg');
  });

  // Product page - add shadow to cards on hover
  $("#products .card" ).hover(function() {
    $(this).addClass('shadow-lg').css('cursor', 'pointer');
  }, function() {
    $(this).removeClass('shadow-lg');
  });

  // Category page - show/hide description containers
  $("#read-more-button").click(function(){
    $("#read-more").hide();
    $("#description-less").hide();
    $("#description-more").show();
    $("#read-less").show();
  });
  $("#read-less-button").click(function(){
    $("#read-less").hide();
    $("#description-more").hide();
    $("#description-less").show();
    $("#read-more").show();
  });

});

// Header - make sticky smaller on scroll
$(window).on('scroll', function() {
  if ($(this).scrollTop() > 250){
      $('#top-bar').addClass("sticky");
  } else{
      $('#top-bar').removeClass("sticky");
  }
});

// Footer - add dynamic year
const date = new Date();
document.querySelector('span.year').innerHTML = date.getFullYear();

// About page - owl carousel
$('.owl-carousel.partners').owlCarousel({
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

// Category page - rearrange gallery thumbnails container if it has a scrollbar displayed
$(window).on('resize', function() {
  if (document.getElementById('carousel-thumbnails') != null) {
    var div = document.getElementById('carousel-thumbnails');
    var hasHorizontalScrollbar = div.scrollWidth > div.clientWidth;
    if (hasHorizontalScrollbar) {
      div.style.justifyContent = 'start';
    } else {
      div.style.justifyContent = 'center';
    }
  }
}).resize();

// Product page - get offer - display city input if needed
$("#getOfferForm-montage, #getOfferForm-transport").click(function () {
  var montage = document.getElementById("getOfferForm-montage").checked;
  var transport = document.getElementById("getOfferForm-transport").checked;
  if (montage || transport) {
    $(".getOfferForm-body .city").show();
    $(".getOfferForm-body .city input").attr("required", true);
  } else if (!(montage || transport)) {
    $(".getOfferForm-body .city").hide();
    $(".getOfferForm-body .city input").attr("required", false);
  }
});
