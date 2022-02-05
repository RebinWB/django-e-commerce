(function ($) {
    "use strict";

    /*----------------------------------------
	   Sticky Menu Activation
	------------------------------------------*/

	$(window).on('scroll', function () {
		if ($(this).scrollTop() > 350) {
			$('.header-sticky').addClass('sticky');
		} else {
			$('.header-sticky').removeClass('sticky');
		}
	});
	
	/*-----------------------------------------
		Off Canvas Mobile Menu
	-------------------------------------------*/

	$(".header-action-btn-menu").on('click', function () {
		$("body").addClass('fix');
		$(".mobile-menu-wrapper").addClass('open');
	});

	$(".offcanvas-btn-close,.offcanvas-overlay").on('click', function () {
		$("body").removeClass('fix');
		$(".mobile-menu-wrapper").removeClass('open');
    });

    /*-----------------------------------------
		Off Canvas Search
	-------------------------------------------*/

	$(".header-action-btn-search").on('click', function () {
		$("body").addClass('fix');
		$(".offcanvas-search").addClass('open');
	});

	$(".offcanvas-btn-close,.body-overlay").on('click', function () {
		$("body").removeClass('fix');
		$(".offcanvas-search").removeClass('open');
	});
	
	/*-----------------------------------------
		Off Canvas Mobile Menu
	-------------------------------------------*/

	$(".header-action-btn-cart").on('click', function () {
		$("body").addClass('fix');
		$(".cart-offcanvas-wrapper").addClass('open');
	});

	$(".offcanvas-btn-close,.offcanvas-overlay").on('click', function () {
		$("body").removeClass('fix');
		$(".cart-offcanvas-wrapper").removeClass('open');
    });
    
    /*----------------------------------------
		Responsive Mobile Menu
	------------------------------------------*/

	//Variables
	var $offCanvasNav = $('.mobile-menu, .category-menu'),
	$offCanvasNavSubMenu = $offCanvasNav.find('.dropdown');

	//Close Off Canvas Sub Menu
	$offCanvasNavSubMenu.slideUp();

	//Category Sub Menu Toggle
	$offCanvasNav.on('click', 'li a, li .menu-expand', function(e) {
	var $this = $(this);
		if ( ($this.parent().attr('class').match(/\b(menu-item-has-children|has-children|has-sub-menu)\b/)) && ($this.attr('href') === '#' || $this.hasClass('menu-expand')) ) {
			e.preventDefault();
			if ($this.siblings('ul:visible').length){
				$this.parent('li').removeClass('active');
				$this.siblings('ul').slideUp();
			} else {
				$this.parent('li').addClass('active');
				$this.closest('li').siblings('li').removeClass('active').find('li').removeClass('active');
				$this.closest('li').siblings('li').find('ul:visible').slideUp();
				$this.siblings('ul').slideDown();
			}
		}
	});
    
    /*----------------------------------------
	   Slider Activation
	------------------------------------------*/

	/* Hero Slider Activation */
    var swiper = new Swiper('.hero-slider .swiper-container', {
        loop: true,
        speed: 1150,
        spaceBetween: 30,
        slidesPerView: 1,
		effect: 'fade',
		pagination: true,
		navigation: true,


        // Navigation arrows
        navigation: {
            nextEl: '.hero-slider .home-slider-next',
            prevEl: '.hero-slider .home-slider-prev'
        },
        pagination: {
            el: '.hero-slider .swiper-pagination',
			type: 'bullets',
			clickable: 'true'
		},
		// Responsive breakpoints
	});
	
	/* Product Carousel Activation */
    var productCarousel = new Swiper('.product-carousel .swiper-container', {
		loop: true,
		slidesPerView: 3,
		spaceBetween: 0,
		pagination: true,
		navigation: true,
		observer: true,
		observeParents: true,

		navigation: {
			nextEl: '.product-carousel .swiper-product-button-next',
			prevEl: '.product-carousel .swiper-product-button-prev'
		},
		pagination: {
			el: '.product-carousel .swiper-pagination',
			type: 'bullets',
			clickable: 'true'
		},
		
		// Responsive breakpoints
		breakpoints: {
			// when window width is >= 320px
			320: {
				slidesPerView: 1,
			},
			// when window width is >= 480px
			480: {
				slidesPerView: 1,
			},
			// when window width is >= 575px
			575: {
				slidesPerView: 2,
			},
			// when window width is >= 768px
			768: {
				slidesPerView: 2,
			},
			// when window width is >= 992px
			992: {
				slidesPerView: 3,
			},
			// when window width is >= 1200px
			1200: {
				slidesPerView: 4,
			}
		}
	});	
	/* Modal Product Carousel Activation */
    var productCarousel = new Swiper('.modal-product-carousel .swiper-container', {
		loop: true,
		slidesPerView: 1,
		spaceBetween: 0,
		pagination: false,
		navigation: true,
		observer: true,
		observeParents: true,

		navigation: {
			nextEl: '.modal-product-carousel .swiper-product-button-next',
			prevEl: '.modal-product-carousel .swiper-product-button-prev'
		}
	});

	/* Product Deal Crousel Activation */
	var productCarousel = new Swiper('.product-deal-carousel .swiper-container', {
        loop: true,
        slidesPerView: 2,
		spaceBetween: 0,
		pagination: true,
		navigation: true,
		observer: true,
		observeParents: true,

		navigation: {
			nextEl: '.product-deal-carousel .swiper-product-deal-next',
			prevEl: '.product-deal-carousel .swiper-product-deal-prev'
		},
		pagination: {
			el: '.product-deal-carousel .swiper-pagination',
			type: 'bullets',
			clickable: 'true'
		},
		breakpoints: {
			// when window width is >= 320px
			320: {
				slidesPerView: 1,
			},
			// when window width is >= 480px
			480: {
				slidesPerView: 1,
			},
			// when window width is >= 575px
			575: {
				slidesPerView: 1,
			},
			// when window width is >= 768px
			768: {
				slidesPerView: 2,
			}
		}
	});

	/* Product List Crousel Activation */
	var productCarousel = new Swiper('.product-list-carousel .swiper-container', {
		loop: true,
		slidesPerView: 1,
		spaceBetween: 0,
		pagination: false,
		navigation: true,
		observer: true,
		observeParents: true,

		navigation: {
			nextEl: '.product-list-carousel .swiper-product-list-next',
			prevEl: '.product-list-carousel .swiper-product-list-prev'
		},
		// pagination: {
		// 	el: '.product-list-carousel .swiper-pagination',
		// 	type: 'bullets',
		// 	clickable: 'true'
		// }
	});
	var productCarousel = new Swiper('.product-list-carousel-2 .swiper-container', {
		loop: true,
		slidesPerView: 1,
		spaceBetween: 0,
		pagination: false,
		navigation: true,
		observer: true,
		observeParents: true,

		navigation: {
			nextEl: '.product-list-carousel-2 .swiper-product-list-next',
			prevEl: '.product-list-carousel-2 .swiper-product-list-prev'
		},
		// pagination: {
		// 	el: '.product-list-carousel-2 .swiper-pagination',
		// 	type: 'bullets',
		// 	clickable: 'true'
		// }
	});
	var productCarousel = new Swiper('.product-list-carousel-3 .swiper-container', {
		loop: true,
		slidesPerView: 1,
		spaceBetween: 0,
		pagination: false,
		navigation: true,
		observer: true,
		observeParents: true,

		navigation: {
			nextEl: '.product-list-carousel-3 .swiper-product-list-next',
			prevEl: '.product-list-carousel-3 .swiper-product-list-prev'
		}
	});

	/*-- Brand Logo --*/
	var brandCarousel = new Swiper('.brand-logo-carousel .swiper-container', {
		loop: true,
		speed: 750,
		spaceBetween: 30,
		slidesPerView: 5,
		effect: 'slide',
		//autoplay: {},

		// Responsive breakpoints
		breakpoints: {
			// when window width is >= 320px
			320: {
			slidesPerView: 2,
			spaceBetween: 20
			},
			// when window width is >= 480px
			480: {
			slidesPerView: 3,
			spaceBetween: 30
			},
			// when window width is >= 768px
			768: {
			slidesPerView: 4,
			spaceBetween: 30
			},
			// when window width is >= 992px
			992: {
			slidesPerView: 5,
			spaceBetween: 30
			}
		}
	});

    /*-- Single product with Thumbnail Vertical -- */
    var zoomThumb = new Swiper('.product-thumb-vertical', {
        spaceBetween: 0,
		slidesPerView: 4,
        direction: 'vertical',
        freeMode: true,
        watchSlidesVisibility: true,
		watchSlidesProgress: true,
		// Responsive breakpoints
		breakpoints: {
			// when window width is >= 320px
			320: {
			slidesPerView: 2,
			},
			// when window width is >= 480px
			480: {
			slidesPerView: 3,
			},
			// when window width is >= 575px
			575: {
			slidesPerView: 3,
			},
			// when window width is >= 767px
			767: {
			slidesPerView: 3,
			},
			// when window width is >= 991px
			991: {
				slidesPerView: 3,
			},
			// when window width is >= 1200px
			1200: {
				slidesPerView: 4,
			},
		}
	});
    var zoomTop = new Swiper('.single-product-vertical-tab', {
		spaceBetween: 10,
		loop: true,
		navigation: {
			nextEl: '.product-thumb-vertical .swiper-button-vertical-next',
			prevEl: '.product-thumb-vertical .swiper-button-vertical-prev',
		},
        thumbs: {
            swiper: zoomThumb
        }
	});
	
    /*-- Single product with Thumbnail Horizental -- */
	var galleryThumbs = new Swiper('.single-product-thumb', {
		spaceBetween: 10,
		slidesPerView: 4,
		// loop: false,
		freeMode: true,
		watchSlidesVisibility: true,
		watchSlidesProgress: true,
		// Responsive breakpoints
		breakpoints: {
			// when window width is >= 320px
			320: {
			slidesPerView: 2,
			},
			// when window width is >= 575px
			575: {
			slidesPerView: 3,
			},
			// when window width is >= 767px
			767: {
			slidesPerView: 4,
			},
			// when window width is >= 991px
			991: {
				slidesPerView: 3,
			},
			// when window width is >= 1200px
			1200: {
				slidesPerView: 4,
			},
		}
	});
	var galleryTop = new Swiper('.single-product-img', {
		spaceBetween: 10,
		loop: true,
		navigation: {
			nextEl: '.single-product-thumb, .swiper-button-horizental-next',
			prevEl: '.single-product-thumb, .swiper-button-horizental-prev',
		},
		// loop: true,
		// loopedSlides: 5, //looped slides should be the same
		thumbs: {
			swiper: galleryThumbs,
		},
	});

	/*----------------------------------------*/
	/*  Countdown
	/*----------------------------------------*/

	$('[data-countdown]').each(function() {
		var $this = $(this), finalDate = $(this).data('countdown');
		$this.countdown(finalDate, function(event) {
			$this.html(event.strftime('<div class="single-countdown"><span class="single-countdown_time">%D</span><span class="single-countdown_text">Days</span></div><div class="single-countdown"><span class="single-countdown_time">%H</span><span class="single-countdown_text">Hours</span></div><div class="single-countdown"><span class="single-countdown_time">%M</span><span class="single-countdown_text">Min</span></div><div class="single-countdown"><span class="single-countdown_time">%S</span><span class="single-countdown_text">Sec</span></div>'));
		});
	});

	/*----------------------------------------
		Aos Activation Js
	------------------------------------------*/

	AOS.init({
		duration: 1500, // values from 0 to 3000, with step 50ms
		disable: false, // accepts following values: 'phone', 'tablet', 'mobile', boolean, expression or function
		offset: 0, // offset (in px) from the original trigger point
		once: true,
		easing: 'ease',
	});

	/*----------------------------------------*/
	/*  Shop Grid Activation
	/*----------------------------------------*/

	$('.shop_toolbar_btn > button').on('click', function (e) {
	
		e.preventDefault();
		
		$('.shop_toolbar_btn > button').removeClass('active');
		$(this).addClass('active');
		
		var parentsDiv = $('.shop_wrapper');
		var viewMode = $(this).data('role');
		
		
		parentsDiv.removeClass('grid_3 grid_4 grid_5 grid_list').addClass(viewMode);

		if(viewMode == 'grid_3'){
			parentsDiv.children().addClass('col-lg-4 col-md-4 col-sm-6').removeClass('col-lg-3 col-cust-5 col-12');
			
		}

		if(viewMode == 'grid_4'){
			parentsDiv.children().addClass('col-xl-3 col-lg-4 col-md-4 col-sm-6').removeClass('col-lg-4 col-cust-5 col-12');
		}
		
		if(viewMode == 'grid_list'){
			parentsDiv.children().addClass('col-12').removeClass('col-xl-3 col-lg-3 col-lg-4 col-md-6 col-md-4 col-sm-6 col-cust-5');
		}
			
	});

	/*----------------------------------------*/
	/*  Nice Select
	/*----------------------------------------*/

	$(document).on('ready', function () {
		$('.nice-select').niceSelect();
	});

	/*-----------------------------------------
	Price Slider Active
	------------------------------------------- */

	$( "#slider-range" ).slider({
        range: true,
        min: 0,
        max: 500,
        values: [ 0, 500 ],
        slide: function( event, ui ) {
        $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
       }
    });
    $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
       " - $" + $( "#slider-range" ).slider( "values", 1 ) );

	/*----------------------------------------*/
	/*  Cart Plus Minus Button
	/*----------------------------------------*/

	$('.cart-plus-minus').append(
		'<div class="dec qtybutton"><i class="fa fa-minus"></i></div><div class="inc qtybutton"><i class="fa fa-plus"></i></div>'
	);
	$('.qtybutton').on('click', function () {
		var $button = $(this);
		var oldValue = $button.parent().find('input').val();
		if ($button.hasClass('inc')) {
			var newVal = parseFloat(oldValue) + 1;
		} else {
			// Don't allow decrementing below zero
			if (oldValue > 1) {
				var newVal = parseFloat(oldValue) - 1;
			} else {
				newVal = 1;
			}
		}
		$button.parent().find('input').val(newVal);
	});

	/*----------------------------------------*/
	/*  Lightgallery Active
	/*----------------------------------------*/

	$(".popup-gallery").lightGallery({
		pager: false, // Enable/Disable pager
		thumbnail: false, // Enable thumbnails for the gallery
		fullScreen: true, // Enable/Disable fullscreen mode
		zoom: true, // Enable/Disable zoom option
		rotateLeft: true, // Enable/Disable Rotate Left
		rotateRight: true, // Enable/Disable Rotate Right
	  });

	/*-----------------------------------------
		Sticky Sidebar Activation
	-------------------------------------------*/

	$('#sticky-sidebar').theiaStickySidebar({
		// Settings
		additionalMarginTop: 150
	});

	/*----------------------------------------*/
	/* Toggle Function Active
	/*----------------------------------------*/

	// showlogin toggle
	$('#showlogin').on('click', function () {
		$('#checkout-login').slideToggle(500);
	});
	// showlogin toggle
	$('#showcoupon').on('click', function () {
		$('#checkout_coupon').slideToggle(500);
	});
	// showlogin toggle
	$('#cbox').on('click', function () {
		$('#cbox-info').slideToggle(500);
	});

	// Ship box toggle
	$('#ship-box').on('click', function () {
		$('#ship-box-info').slideToggle(1000);
	});
	/*---------------------------------
        Scroll Up
    -----------------------------------*/
    function scrollToTop() {
        var $scrollUp = $('#scroll-top'),
            $lastScrollTop = 0,
            $window = $(window);

        $window.on('scroll', function () {
            var st = $(this).scrollTop();
            if (st > $lastScrollTop) {
                $scrollUp.removeClass('show');
            } else {
                if ($window.scrollTop() > 200) {
                    $scrollUp.addClass('show');
                } else {
                    $scrollUp.removeClass('show');
                }
            }
            $lastScrollTop = st;
        });

        $scrollUp.on('click', function (evt) {
            $('html, body').animate({scrollTop: 0}, 600);
            evt.preventDefault();
        });
    }
	scrollToTop();
	/*---------------------------------
	 	MailChimp
    -----------------------------------*/
    $('#mc-form').ajaxChimp({
        language: 'en',
        callback: mailChimpResponse,
        // ADD YOUR MAILCHIMP URL BELOW HERE!
        url: 'http://devitems.us11.list-manage.com/subscribe/post?u=6bbb9b6f5827bd842d9640c82&amp;id=05d85f18ef'
    });
    function mailChimpResponse(resp) {
        if (resp.result === 'success') {
            $('.mailchimp-success').html('' + resp.msg).fadeIn(900);
            $('.mailchimp-error').fadeOut(400);
        } else if (resp.result === 'error') {
            $('.mailchimp-error').html('' + resp.msg).fadeIn(900);
        }
	}
	/*-------------------------
        Ajax Contact Form 
    ---------------------------*/
    $(function() {

        // Get the form.
        var form = $('#contact-form');

        // Get the messages div.
        var formMessages = $('.form-messege');

        // Set up an event listener for the contact form.
        $(form).submit(function(e) {
            // Stop the browser from submitting the form.
            e.preventDefault();

            // Serialize the form data.
            var formData = $(form).serialize();

            // Submit the form using AJAX.
            $.ajax({
                type: 'POST',
                url: $(form).attr('action'),
                data: formData
            })
            .done(function(response) {
                // Make sure that the formMessages div has the 'success' class.
                $(formMessages).removeClass('error');
                $(formMessages).addClass('success');

                // Set the message text.
                $(formMessages).text(response);

                // Clear the form.
                $('#contact-form input,#contact-form textarea').val('');
            })
            .fail(function(data) {
                // Make sure that the formMessages div has the 'error' class.
                $(formMessages).removeClass('success');
                $(formMessages).addClass('error');

                // Set the message text.
                if (data.responseText !== '') {
                    $(formMessages).text(data.responseText);
                } else {
                    $(formMessages).text('Oops! An error occured and your message could not be sent.');
                }
            });
        });

    });



})(jQuery);

