

  $(".comment-reply-btn").click(function(event){
    event.preventDefault();
    $(this).parent().next(".comment-reply").toggle();
  })


  $(document).ready(function(){
          function updateText(btn, newCount){
          btn.html( "<img src='https://s3-us-west-2.amazonaws.com/bif-ball/static/images/arrow.svg'/><p>" + newCount + "</p>")
      }
      $(".like-btn").click(function(e){
        e.preventDefault()
        var this_ = $(this)
        var likeUrl = this_.attr("data-href")
        var likeCount = parseInt(this_.attr("data-likes")) 
        var addLike = likeCount + 1
        var removeLike = likeCount - 1
        if (likeUrl){
           $.ajax({
            url: likeUrl,
            method: "GET",
            data: {},
            success: function(data){
              console.log(data)
              var newLikes;
              if (data.liked){
                  updateText(this_, addLike)
              } 
            }, error: function(error){
              console.log(error)
              console.log("error")
            }
          })
        }
       
      })
  })

   $('.mobile-hamburger-icon').click(function(e) {
      $('.mobile-hamburger--menu').toggleClass('open');

      $('body').addClass('modal');
      $('.icon-1').toggleClass('open');
      $('.icon-2').toggleClass('open');
      $('.icon-3').toggleClass('open');

      e.preventDefault();
    });



function curvedText(time) {
  var tl   = new TimelineMax({ repeat: -1 });
  var text = document.querySelector('.text-animate');

  var from = {
    transformOrigin: 'center center',
    rotation: 0
  };

  var to = {
    rotation: 560,
    ease: Linear.easeInOut
  };

  tl.fromTo([text], time, from, to);

  return tl;
}

curvedText(15);


(function($) { // Begin jQuery
  $(function() { // DOM ready
    // If a link has a dropdown, add sub menu toggle.
    $('nav ul li a:not(:only-child)').click(function(e) {
      $(this).siblings('.nav-dropdown').toggle();
      // Close one dropdown when selecting another
      $('.nav-dropdown').not($(this).siblings()).hide();
      e.stopPropagation();
    });
    // Clicking away from dropdown will remove the dropdown class
    $('html').click(function() {
      $('.nav-dropdown').hide();
    });
    // Toggle open and close nav styles on click
    $('#nav-toggle').click(function() {
      $('nav ul').slideToggle();
    });
    // Hamburger to X toggle
    $('#nav-toggle').on('click', function() {
      this.classList.toggle('active');
    });
  }); // end DOM ready
})(jQuery); // end jQuery


// $(function(){
//   $(".hamburger-icon").click(function(){
//     $(".navigation").toggleClass("popout");
//   });
//   $(".hamburger-icon").click(function(){
//     $(".hamburger-icon").toggleClass("icon");
//   });
// });
