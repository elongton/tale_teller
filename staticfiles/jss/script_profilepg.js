$(document).ready(function(){

	var size = $('#content_block').width() - $('#profile_right').width() -10;
	size = size.toString().concat('px');
	$('#profile_left').css('width', size);

	$(window).resize(function(){
		var size = $('#content_block').width() - $('#profile_right').width() -10;
		size = size.toString().concat('px');
		$('#profile_left').css('width', size);
	});

	
});


	// $(window.resize(function(){
		// var size = $('#content_block').width() - $('.rightside').width();
		// size = size.toString().concat('px');
		// $('.leftside').css('width', size);
	// });