$(document).ready(function(){
    
    
    setTimeout(function(){
        $("#messages").fadeOut('slow', function(){
            $(this).remove()
        })
    },2000);

    $("#menu-button").click(function(){
        $(this).toggleClass("active");
        $('.line').toggleClass('line-changeColor');
        $("#menu").slideToggle();
    });

    $(document).click(function(event){
        if(!$(event.target).closest('#menu-button, #menu').length){
            $('.line').removeClass('line-changeColor');
            $('#menu-button').removeClass('active');
            $('#menu').hide();
        }
    });

    $('#add').click(function(){
        $('.add-modal-bg').css('display', 'block');
    });

});

