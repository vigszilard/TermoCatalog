$(document).ready(function() {
   console.log("document is ready");
   
     $( ".card" ).hover(
     function() {
       $(this).addClass('shadow-lg').css('cursor', 'pointer'); 
     }, function() {
       $(this).removeClass('shadow-lg');
     }
   );
});

$(window).scroll(function() {
  if ($(this).scrollTop() > 250){  
      $('#top-bar').addClass("sticky");
  }
  else{
      $('#top-bar').removeClass("sticky");
  }
});