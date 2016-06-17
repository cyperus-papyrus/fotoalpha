        function init_masonry(){
          var $container = $('#content');

          $container.imagesLoaded( function(){
              $container.masonry({
                itemSelector: '.box',
                isAnimated: true
            });
          });
        }

        $(document).ready(function(){

            //Init jQuery Masonry layout
            init_masonry();

            // Magnific Popup
            $('.gallery-images-container').magnificPopup({
                delegate: 'a', // child items selector, by clicking on it popup will open
                type: 'image',
                gallery: {
                    enabled: true,
                    navigateByImgClick: true,
                    preload: [0,1] // Will preload 0 - before current, and 1 after the current image
                },
            });

            //Select menu onchange
            $("#collapsed-navbar").change(function () {
                window.location = $(this).val();
            });

        });


