/*!
 * Start Bootstrap - Creative Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

(function($) {
    "use strict"; // Start of use strict

    // jQuery for page scrolling feature - requires jQuery Easing plugin
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top - 65)
        }, 1250, 'easeInOutExpo');
        event.preventDefault();
    });

    // Highlight the top nav as scrolling occurs
    $('body').scrollspy({
        target: '.navbar-fixed-top',
        offset: 65
    })

    // Closes the Responsive Menu on Menu Item Click
    $('.navbar-collapse ul li a').click(function() {
        $('.navbar-toggle:visible').click();
    });

    // Fit Text Plugin for Main Header
    $("#caption-text").fitText(
        1.4, {
            minFontSize: '5px',
            maxFontSize: '26px'
        }
    );

 // Offset for Main Navigation
    $('#mainNav').affix({
        offset: {
            top: 100
        }
    })

 // Initialize WOW.js Scrolling Animations
    new WOW().init();
	
//Header Background Image Transition
	$("header").bgswitcher({
  images: ["/static/fmc/clubs/animation/img/header1.jpg", "/static/fmc/clubs/animation/img/header2.jpg", "/static/fmc/clubs/animation/img/header3.jpg", "/static/fmc/clubs/animation/img/header4.jpg"],
  effect: "fade",
  interval: 4000,
  duration: 1000
});

/*Caption change JavaScript for Header background*/	

 $("#caption-text").Morphext({
    // The [in] animation type. Refer to Animate.css for a list of available animations.
    animation: "fadeInUp",
    // An array of phrases to rotate are created based on this separator. Change it if you wish to separate the phrases differently (e.g. So Simple | Very Doge | Much Wow | Such Cool).
    separator: "_",
    // The delay between the changing of each phrase in milliseconds.
    speed: 4000,
    complete: function () {
        // Called after the entrance animation is executed.
    }
});


 
 
 })(jQuery); // End of use strict
