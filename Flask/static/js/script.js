$(document).ready(function(){
    $("#menu-button").click(function(){
        $(this).toggleClass("active");
        $('.line').toggleClass('line-changeColor');
        $("#menu").slideToggle();
    });

    $(document).on('click', function(event){
        if(!$(event.target).closest('#menu-button, #menu').length){
            $('.line').removeClass('line-changeColor');
            $('#menu-button').removeClass('active');
            $('#menu').hide();
        }
    });
});