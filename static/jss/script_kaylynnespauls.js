$(document).ready(function(){

//kay's dynamic page
	$('#target1').addClass('active').show()

	
//make content box the right size
	
	var size = $('.divpanel').width() - $('.right_scroll').width()-10;
	size = size.toString().concat('px');
	$('.scroll_content').css('width', size);
	
	$(window).resize(function(){
		var size = $('.divpanel').width() - $('.right_scroll').width()-10;
		size = size.toString().concat('px');
		$('.scroll_content').css('width', size);
	});
	
	
	
	
    $('.panel').click(function() {
        var $target = $($(this).attr('id')),
            $other = $target.siblings('.active');
        
        if (!$target.hasClass('active')) {
            $other.each(function(index, self) {
                var $this = $(this);
                $this.removeClass('active').animate({
                    right: 2*$this.width()
                }, 500);
            });

            $target.addClass('active').show().css({
                right: -2*($target.width())
            }).animate({
                right: -40
            }, 500)
        }
    });
	
	
	//change cursors to pointers on service page links
	$('.panel').css('cursor', 'pointer');
	
	$(".like_button").button();

	
});