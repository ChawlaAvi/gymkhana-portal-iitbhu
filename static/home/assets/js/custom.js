$(document).ready(function(){	
	$("#news-ticker").load("news.txt");
        $("#parliament-ticker").load("parliament-activities.txt");
        $("#upcoming-ticker").load("upcoming.txt");
});


$('.navbar .dropdown').hover(function() {
  $(this).find('.dropdown-menu').first().stop(true, true).delay(100).slideDown();
}, function() {
  $(this).find('.dropdown-menu').first().stop(true, true).delay(80).slideUp();
});

