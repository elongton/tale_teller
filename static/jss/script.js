$(document).ready(function(){

//responsive design

	if ($(window).width() < 935){
			$( "#header_block").css("margin-left", "20px");
			$( "#header_block").css("left", "0");
			
			$( "#center_block").css("margin-left", "0px");
			$( "#center_block").css("left", "0");
			
			//calculation of how big content block is going to be
			var size = 920 - $("#right_block").width();
			size = (size.toString()).concat("px");
			//assignment
			$("#content_block").css("width", size);
			//add content_block and right_block to center_block div
			$("#content_block").appendTo("#center_block");
			$("#right_block").appendTo("#center_block");
			$("#content_block").css("margin-top", "95px");
			$("#right_block").css("margin-top", "95px");
	}
	else if($(window).width() < (935+2*$("#right_block").width())){
			var $body = $('body');
			$("#content_block").appendTo($body);
			$("#right_block").appendTo($body);
			$("#footer_block").appendTo($body);
			$("#center_block").empty();
			var X = 920/2, 
				Y = $(window).width()/2,
				Z = $("#right_block").width(),
				K = Z-(Y-X),
				size = 920 - K-10;
			size = (size.toString()).concat("px");
			$("#content_block").css("width", size);
			$("#content_block").css("margin-top", "95px");
			$("#right_block").css("margin-top", "95px");
			//keep header in the middle
			$( "#header_block").css("margin-left", "-460px");
			$( "#header_block").css("left", "50%");
	
	}
	else{
			var $body = $('body');
			$("#content_block").appendTo($body);
			$("#right_block").appendTo($body);
			$("#footer_block").appendTo($body);
			$("#center_block").empty();
			$("#content_block").css("margin-top", "95px");
			$("#right_block").css("margin-top", "95px");
			$("#content_block").css("width", "920px");
			$( "#header_block").css("margin-left", "-460px");
			$( "#header_block").css("left", "50%");
	};
	
	
	
	$(window).resize(function(){
		if ($(window).width() < 935){
				$( "#header_block").css("margin-left", "20px");
				$( "#header_block").css("left", "0");
				
				$( "#center_block").css("margin-left", "0px");
				$( "#center_block").css("left", "0");
				
				//calculation of how big content block is going to be
				var size = 920 - $("#right_block").width();
				size = (size.toString()).concat("px");
				//assignment
				$("#content_block").css("width", size);
				//add content_block and right_block to center_block div
				$("#content_block").appendTo("#center_block");
				$("#right_block").appendTo("#center_block");
				$("#content_block").css("margin-top", "95px");
				$("#right_block").css("margin-top", "95px");
		}
		else if($(window).width() < (935+2*$("#right_block").width())){
				var $body = $('body');
				$("#content_block").appendTo($body);
				$("#right_block").appendTo($body);
				$("#footer_block").appendTo($body);
				$("#center_block").empty();
				var X = 920/2, 
					Y = $(window).width()/2,
					Z = $("#right_block").width(),
					K = Z-(Y-X),
					size = 920 - K-10;
				size = (size.toString()).concat("px");
				$("#content_block").css("width", size);
				$("#content_block").css("margin-top", "95px");
				$("#right_block").css("margin-top", "95px");
				//keep header in the middle
				$( "#header_block").css("margin-left", "-460px");
				$( "#header_block").css("left", "50%");
		
		}
		else{
				var $body = $('body');
				$("#content_block").appendTo($body);
				$("#right_block").appendTo($body);
				$("#footer_block").appendTo($body);
				$("#center_block").empty();
				$("#content_block").css("margin-top", "95px");
				$("#right_block").css("margin-top", "95px");
				$("#content_block").css("width", "920px");
				$( "#header_block").css("margin-left", "-460px");
				$( "#header_block").css("left", "50%");
		};
	});


// //kay's dynamic page
	// $('#target1').addClass('active').show()

    // $('span.panel').click(function() {
        // var $target = $($(this).attr('id')),
            // $other = $target.siblings('.active');
        
        // if (!$target.hasClass('active')) {
            // $other.each(function(index, self) {
                // var $this = $(this);
                // $this.removeClass('active').animate({
                    // left: $this.width()
                // }, 500);
            // });

            // $target.addClass('active').show().css({
                // left: -($target.width())
            // }).animate({
                // left: 0
            // }, 500);
        // }
    // });



//change cursors to pointers on service page links
	$('#IE_link').css('cursor', 'pointer');
	$('#CC_link').css('cursor', 'pointer');
	$('#MP_link').css('cursor', 'pointer');
	$('#P_link').css('cursor', 'pointer');
	$('.topreturn').css('cursor', 'pointer');
	
	
//scrolling to links on services page

//calculate pixel locations
var IE = $('#ind_editing').offset().top - 110;
var CC = $('#crea_consult').offset().top - 110;
var MP = $('#mark_pro').offset().top - 110;
var P = $('#pricing').offset().top - 110;

IE = "+=" + IE.toString() + "px";
CC = "+=" + CC.toString() + "px";
MP = "+=" + MP.toString() + "px";
P = "+=" + P.toString() + "px";

//$('.notes').text(IE);


	$('#IE_link').click(function(){
		$.scrollTo(IE, 500, { axis:'y' });
	});

		$('#CC_link').click(function(){
		$.scrollTo(CC, 1200, { axis:'y' });
	});

		$('#MP_link').click(function(){
		$.scrollTo(MP, 1500, { axis:'y' });
	});

		$('#P_link').click(function(){
		$.scrollTo(P, 1500, { axis:'y' });
	});


	$('.topreturn').click(function(){	
		var marg = $(document).scrollTop();
		var time = 0;
		if (marg < 260){
			time = 500;
		}
		else if(marg < 990){
			time = 1200;
		}
		else{
			time = 1500;
		}	
		$.scrollTo('0px', time, { axis:'y' });
	});
	
		
//for keeping form on services page static
	$(document).scroll(function(){
			var marg = $(document).scrollTop();
			marg = (marg.toString()).concat("px");
			$("#formlist").css("margin-top", marg)
	});
	

});
