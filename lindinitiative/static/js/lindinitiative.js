jQuery(document).ready(function($) {

    $('html').on('click', function() {
        $('#overlay').fadeIn("slow");

    });

    $(window).on('scroll touchmove', function(){
        $('#overlay').fadeIn("slow");
    });

    $(window).off('scroll touchmove');


});