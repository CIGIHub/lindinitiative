jQuery(document).ready(function($) {

    $('html').on('click touch', function() {
        $('#overlay').fadeIn("slow");

    });

    $(window).on('scroll', function(){
        $('#overlay').fadeIn("slow");
    });
});