    var slider_img = document.querySelector('.slider-img');
    var images = ['1.png', '2.png', '1.png'];
    var i =0; 

    function prev() {
        if (i<=0) i = images.length;
        b=i
        i--;
        return setImg();
    }

    function next() {
        if (i >= images.length - 1) i = -1;
        b = i
        i++;
        return setImg();
    }

    function setImg(){
        return slider_img.setAttribute('src', "/media/works/krolik/second_part/main_slideshow/pics/" + images[i])
    }

    function borderMove(){

        var border_forward_animation =  anime({
            targets: '#forward-svg',
            strokeDashoffset: [anime.setDashoffset,0],
            easing: 'easeInOutSine',
            duration: 20500,
        
            direction:'alternate',
            delay: function(el, i) { return i * 250 },
            
            loop: true,
        });

        var border_backward_animation =  anime({
            targets: '#backward-svg',
            strokeDashoffset: [0, anime.setDashoffset],
            easing: 'easeInOutSine',
            duration: 20500,
        
            direction:'alternate',
            delay: function(el, i) { return i * 250 },
            
            loop: true,
        });
    } borderMove()

    var arrow_left = anime({
        targets:'.arrow_left',
        scale:1.1,
        duration:450,
        autoplay:false,
        loop:false,
    })

    var arrow_right = anime({
        targets:'.arrow_right',
        scale:1.1,
        duration:450,
        autoplay:false,
        loop:false,
    })

    var motion_of_name =  anime({
        targets: '.nazvanie',
        translateY: {
            value:15,
            duration: 7500,
        },
        direction: 'alternate',
        easing: 'easeInOutSine',
        loop: true,
    });

    function buySwitchToEnglish() {
        var english_buy_appears = anime({
            targets:'.krolik-buy',
            opacity: 1,
            duration:9000,
            autoplay:true,
        })   

        var disappear_buy = anime({
            targets:'.text-buy',
            opacity: 0,
            duration:9000,
            autoplay:true,
        })
    }

    function buyBackToRussian() {
        var disappear_english_buy = anime({
            targets:'.krolik-buy',
            opacity: 0,
            duration:9000,
            
            autoplay:true,
        })

        var buy_appears = anime({
            targets:'.text-buy',
            opacity: 1,
            duration:9000,
            autoplay:true,
        })
    }

    function razmerSwitchToEnglish() {
        var english_razmer_appears = anime({
            targets:'.razmer-english',
            opacity: 1,
            duration:9000,
            autoplay:true,
        })   

        var disappear_razmer = anime({
            targets:'.razmer',
            opacity: 0,
            duration:9000,
            autoplay:true,
        })

    }

    function razmerBackToRussian() {
        var disappear_english_razmer = anime({
            targets:'.razmer-english',
            opacity: 0,
            duration:9000,
            
            autoplay:true,
        })

        var razmer_appears = anime({
            targets:'.razmer',
            opacity: 1,
            duration:9000,
            autoplay:true,
        })

    }

    function materialsSwitchToEnglish() {
        var english_materials_appears = anime({
            targets:'.materials-english',
            opacity: 1,
            duration:9000,
            autoplay:true,
        })   

        var disappear_materials = anime({
            targets:'.materials',
            opacity: 0,
            duration:9000,
            autoplay:true,
        })
    }

    function materialsBackToRussian() {
        var disappear_english_materials = anime({
            targets:'.materials-english',
            opacity: 0,
            duration:9000,
            
            autoplay:true,
        })

        var materials_appears = anime({
            targets:'.materials',
            opacity: 1,
            duration:9000,
            autoplay:true,
        })
    }

    function farforSwitchToEnglish() {
        var english_farfor_appears = anime({
            targets:'.farfor-english',
            opacity: 1,
            duration:9000,
            autoplay:true,
        })   

        var disappear_farfor = anime({
            targets:'.farfor',
            opacity: 0,
            duration:9000,
            autoplay:true,
        })
    }

    function farforBackToRussian() {
        var disappear_english_farfor = anime({
            targets:'.farfor-english',
            opacity: 0,
            duration:9000,
            
            autoplay:true,
        })

        var farfor_appears = anime({
            targets:'.farfor',
            opacity: 1,
            duration:9000,
            autoplay:true,
        })
    }

    function paintsSwitchToEnglish() {
        var english_farfor_appears = anime({
            targets:'.paints-english',
            opacity: 1,
            duration:9000,
            autoplay:true,
        })   

        var disappear_farfor = anime({
            targets:'.paints',
            opacity: 0,
            duration:9000,
            autoplay:true,
        })
    }

    function paintsBackToRussian() {
        var disappear_english_farfor = anime({
            targets:'.paints-english',
            opacity: 0,
            duration:9000,
            
            autoplay:true,
        })

        var farfor_appears = anime({
            targets:'.paints',
            opacity: 1,
            duration:9000,
            autoplay:true,
        })
    }

    function akrilSwitchToEnglish() {
        var english_akril_appears = anime({
            targets:'.akril-english',
            opacity: 1,
            duration:9000,
            autoplay:true,
        })   

        var disappear_akril = anime({
            targets:'.akril',
            opacity: 0,
            duration:9000,
            autoplay:true,
        })
    }

    function akrilBackToRussian() {
        var disappear_english_akril = anime({
            targets:'.akril-english',
            opacity: 0,
            duration:9000,
            
            autoplay:true,
        })

        var akril_appears = anime({
            targets:'.akril',
            opacity: 1,
            duration:9000,
            autoplay:true,
        })
    }


 
    // LOGO PAGE STARTS HERE

    var minis = ['#mini_zakis', '#mini_glaz', '#mini_put', '#mini_kosmos', "#mini_maski", '#mini_vibe', '#mini_krolik', '#mini_panno']
    var minis_set = anime.set(minis,{
        opacity:0,
    })

    var zakis_set = anime({
        targets:'#mini_zakis',
        opacity:0,
        autoplay:false,
    })
    var zakis_onmove = anime({
        targets: '#mini_zakis',
        opacity:1,
        autoplay:false,
    })

    var glaz_set = anime({
        targets:'#mini_glaz',
        opacity:0,
        autoplay:false,
    })
    var glaz_onmove = anime({
        targets: '#mini_glaz',
        opacity:1,
        autoplay:false,
    })

    var put_set = anime({
        targets:'#mini_put',
        opacity:0,
        autoplay:false,
    })
    var put_onmove = anime({
        targets: '#mini_put',
        opacity:1,
        autoplay:false,
    })

    var kosmos_set = anime({
        targets:'#mini_kosmos',
        opacity:0,
        autoplay:false,
    })
    var kosmos_onmove = anime({
        targets: '#mini_kosmos',
        opacity:1,
        autoplay:false,
    })

    var maski_set = anime({
        targets:'#mini_maski',
        opacity:0,
        autoplay:false,
    })
    var maski_onmove = anime({
        targets: '#mini_maski',
        opacity:1,
        autoplay:false,
    })

    var ohboy_set = anime({
        targets:'#mini_vibe',
        opacity:0,
        autoplay:false,
    })
    var ohboy_onmove = anime({
        targets: '#mini_vibe',
        opacity:1,
        autoplay:false,
    })   
    var panno_set = anime({
        targets:'#mini_panno',
        opacity:0,
        autoplay:false,
    })
    var panno_onmove = anime({
        targets: '#mini_panno',
        opacity:1,
        autoplay:false,
    }) 

    var krolik_set = anime({
        targets:'#mini_krolik',
        opacity:0,
        autoplay:false,
    })
    var krolik_onmove = anime({
        targets: '#mini_krolik',
        opacity:1,
        autoplay:false,
    })   

    // ЭФФЕКТ ГЛАВНОГО МЕНЮ ИЗ ЛОГОТИПА
    // Step 1: Create jQuery plugin
            // ============================

    $.fn.fancyMorph = function( opts ) {

        var Morphing = function( $btn, opts ) {
        var self = this;

        self.opts = $.extend({
        animationEffect : false,
        infobar    : false,
        buttons    : ['close'],
        smallBtn   : false,
        touch      : false,
        baseClass  : 'fancybox-morphing',
        afterClose : function() {
            self.close();
        }
        }, opts);

        self.init( $btn );
        };

        Morphing.prototype.init = function( $btn ) {
        var self = this;

        self.$btn = $btn.addClass('morphing-btn');

        self.$clone = $('<div class="morphing-btn-clone" />')
        .hide()
        .insertAfter( $btn );

        // Add wrapping element and set initial width used for positioning
        $btn.wrap( '<span class="morphing-btn-wrap"></span>' ).on('click', function(e) {
        e.preventDefault();

        self.start();
        });

        };

        Morphing.prototype.start = function() {
        var self = this;

        if ( self.$btn.hasClass('morphing-btn_circle') ) {
        return;
        }

        // Set initial width, because it is not possible to start CSS transition from "auto"
        self.$btn.width( self.$btn.width() ).parent().width( self.$btn.outerWidth() );

        self.$btn.off('.fm').on("transitionend.fm webkitTransitionEnd.fm oTransitionEnd.fm MSTransitionEnd.fm", function(e) {

        if ( e.originalEvent.propertyName === 'width' ) {
            self.$btn.off('.fm');

            self.animateBg();
        }

        }).addClass('morphing-btn_circle');

        };

        Morphing.prototype.animateBg = function() {
        var self = this;

        self.scaleBg();

        self.$clone.show();

        // Trigger repaint
        self.$clone[0].offsetHeight;

        self.$clone.off('.fm').on("transitionend.fm webkitTransitionEnd.fm oTransitionEnd.fm MSTransitionEnd.fm", function(e) {
        self.$clone.off('.fm');

        self.complete();

        }).addClass('morphing-btn-clone_visible');
        };

        Morphing.prototype.scaleBg = function() {
        var self = this;

        var $clone = self.$clone;
        var scale  = self.getScale();
        var $btn   = self.$btn;
        var pos    = $btn.offset();

        $clone.css({
        top       : pos.top  + $btn.outerHeight() * 0.5 - ( $btn.outerHeight() * scale * 0.5 ) - $(window).scrollTop(),
        left      : pos.left + $btn.outerWidth()  * 0.5 - ( $btn.outerWidth()  * scale * 0.5 ) - $(window).scrollLeft(),
        width     : $btn.outerWidth()  * scale,
        height    : $btn.outerHeight() * scale,
        transform : 'scale(' + ( 1 / scale ) + ')'
        });
        };

        Morphing.prototype.getScale = function() {
        var $btn    = this.$btn,
            radius  = $btn.outerWidth() * 0.5,
            left    = $btn.offset().left + radius - $(window).scrollLeft(),
            top     = $btn.offset().top  + radius - $(window).scrollTop(),
            windowW = $(window).width(),
            windowH = $(window).height();

        var maxDistHor  = ( left > windowW / 2 ) ? left : ( windowW - left ),
            maxDistVert = ( top > windowH / 2 )  ? top  : ( windowH - top );

        return Math.ceil(Math.sqrt( Math.pow( maxDistHor, 2 ) + Math.pow( maxDistVert, 2 ) ) / radius );
        };

        Morphing.prototype.complete = function() {
        var self = this;
        var $btn = self.$btn;

        $.fancybox.open({ src : $btn.data('src') || $btn.attr('href') }, self.opts);

        $(window).on('resize.fm', function() {
        //self.scaleBg();
        });
        };

        Morphing.prototype.close = function() {
        var self   = this;
        var $clone = self.$clone;

        self.scaleBg();

        $clone.one('transitionend webkitTransitionEnd oTransitionEnd MSTransitionEnd', function(e) {
        $clone.hide();

        self.$btn.removeClass('morphing-btn_circle');
        });

        $clone.removeClass('morphing-btn-clone_visible');

        $(window).off('resize.fm');
        };

        // Init
        this.each(function() {
        var $this = $(this);

        if ( !$this.data("morphing") ) {
        $this.data( "morphing", new Morphing( $this, opts ) );
        }

        });

        return this;
        };


        // Step 2: Start using it!
        // =======================

        $("[data-morphing]").fancyMorph({
        hash : 'morphing'
        });
