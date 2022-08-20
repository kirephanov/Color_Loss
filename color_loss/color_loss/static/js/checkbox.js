$(window).keyup(function(e){
    var target = $('.checkbox-other input:focus');
    if (e.keyCode == 9 && $(target).length){
        $(target).parent().addClass('focused');
    }
});
  
$('.checkbox-other input').focusout(function(){
    $(this).parent().removeClass('focused');
});