(function(){var r,t;r=window.jQuery||("function"==typeof require?require("jquery"):void 0),t=r(document),r.turbo={version:"2.1.0",isReady:!1,use:function(r,o){return t.off(".turbo").on(""+r+".turbo",this.onLoad).on(""+o+".turbo",this.onFetch)},addCallback:function(o){return r.turbo.isReady&&o(r),t.on("turbo:ready",function(){return o(r)})},onLoad:function(){return r.turbo.isReady=!0,t.trigger("turbo:ready")},onFetch:function(){return r.turbo.isReady=!1},register:function(){return r(this.onLoad),r.fn.ready=this.addCallback}},r.turbo.register(),r.turbo.use("page:load","page:fetch")}).call(this);
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

$(document).ready(function() 
  {
    $('#loading').animate({
       opacity: .2,
     }).hide();
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


(function(e){if(typeof exports=="object"&&typeof module!="undefined")module.exports=e();else if(typeof define=="function"&&define.amd)define([],e);else{var t;typeof window!="undefined"?t=window:typeof global!="undefined"?t=global:typeof self!="undefined"?t=self:t=this,t.starRatings=e()}})(function(){var e,t,n;return function r(e,t,n){function i(o,u){if(!t[o]){if(!e[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(s)return s(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=t[o]={exports:{}};e[o][0].call(l.exports,function(t){var n=e[o][1][t];return i(n?n:t)},l,l.exports,r,e,t,n)}return t[o].exports}var s=typeof require=="function"&&require;for(var o=0;o<n.length;o++)i(n[o]);return i}({1:[function(e,t,n){t.exports=e("./src/ratings")},{"./src/ratings":2}],2:[function(e,t,n){function s(){var e=document.querySelectorAll(".star-ratings-rate-action"),t;for(t=0;t<e.length;t+=1)o(e[t])}function o(e){e.addEventListener("click",u),e.onmouseenter=function(){var e=f(this),t=this.getAttribute("data-score"),n=i.findParent(this,"star-ratings");n.querySelector(".star-ratings-rating-foreground").style.width=100/e*t+"%"},e.onmouseleave=function(){var e=l(this),t=f(this),n=this.getAttribute("data-score"),r=i.findParent(this,"star-ratings"),s=100/t*e+"%";r.querySelector(".star-ratings-rating-foreground").style.width=s}}function u(e){e.stopPropagation(),e.preventDefault();var t=this.getAttribute("href"),n=this.getAttribute("data-score");a(t,n,this)}function a(e,t,n){r.post(e,{score:t},function(e){c(e,n)},function(e){h(e,n)})}function f(e){var t=i.findParent(e,"star-ratings");return t?parseInt(t.getAttribute("data-max-rating")):-1}function l(e){var t=i.findParent(e,"star-ratings");return t?parseFloat(t.getAttribute("data-avg-rating")):-1}function c(e,t){var n=i.findParent(t,"star-ratings"),r;if(n===undefined||n===null)return;n.setAttribute("data-avg-rating",e.average);var s=n.getElementsByClassName("star-ratings-rating-average")[0];s&&(r=s.getElementsByClassName("star-ratings-rating-value")[0],r&&(r.innerHTML=e.average.toFixed(2)));var o=n.getElementsByClassName("star-ratings-rating-count")[0];o&&(r=o.getElementsByClassName("star-ratings-rating-value")[0],r&&(r.innerHTML=e.count));var u=n.getElementsByClassName("star-ratings-rating-user")[0];u&&(r=u.getElementsByClassName("star-ratings-rating-value")[0],r&&(r.innerHTML=e.user_rating)),n.querySelector(".star-ratings-rating-foreground").style.width=e.percentage+"%"}function h(e,t){var n=i.findParent(t,"star-ratings");if(n===undefined||n===null)return;n.querySelector(".star-ratings-errors").innerHTML=e.error,setTimeout(function(){n.querySelector(".star-ratings-errors").innerHTML=""},2500)}var r=e("./rest.js"),i=e("./utils");document.addEventListener("DOMContentLoaded",function(e){document.querySelector(".star-ratings")&&s()}),t.exports={bindRating:o}},{"./rest.js":3,"./utils":4}],3:[function(e,t,n){"use strict";var r={getCookie:function(e){var t=null,n,r,i;if(document.cookie&&document.cookie!==""){n=document.cookie.split(";");for(r=0;r<n.length;r+=1){i=n[r].trim();if(i.substring(0,e.length+1)===e+"="){t=decodeURIComponent(i.substring(e.length+1));break}}}return t},makeRequest:function(e,t,n,r){var i=new XMLHttpRequest;return i.overrideMimeType!==undefined&&i.overrideMimeType("application/json"),i.open(t,e,!0),i.setRequestHeader("Content-Type","application/json"),i.setRequestHeader("X-Requested-With","XMLHttpRequest"),i.onreadystatechange=function(){if(i.readyState!==4)return;i.status>=200&&i.status<=299?n&&(i.responseText?n(JSON.parse(i.responseText)):n()):r&&r(JSON.parse(i.responseText))},i},get:function(e,t,n,r){var i=this.makeRequest(e,"GET",n,r);i.send(JSON.stringify(t))},post:function(e,t,n,r){var i=this.makeRequest(e,"POST",n,r);i.setRequestHeader("X-CSRFToken",this.getCookie("csrftoken")),i.send(JSON.stringify(t))},put:function(e,t,n,r){var i=this.makeRequest(e,"PUT",n,r);i.setRequestHeader("X-CSRFToken",this.getCookie("csrftoken")),i.send(JSON.stringify(t))},patch:function(e,t,n,r){var i=this.makeRequest(e,"PATCH",n,r);i.setRequestHeader("X-CSRFToken",this.getCookie("csrftoken")),i.send(JSON.stringify(t))},"delete":function(e,t,n,r){var i=this.makeRequest(e,"DELETE",n,r);i.setRequestHeader("X-CSRFToken",this.getCookie("csrftoken")),i.send(JSON.stringify(t))}};t.exports=r},{}],4:[function(e,t,n){function r(e,t){return(" "+e.className+" ").indexOf(" "+t+" ")>-1}function i(e,t){var n=e.parentNode;while(r(n,t)===!1){if(n.parentNode===undefined)return null;n=n.parentNode}return n}t.exports={hasClass:r,findParent:i}},{}]},{},[1])(1)});


//turbo links


// $(function(){
//   $(".hamburger-icon").click(function(){
//     $(".navigation").toggleClass("popout");
//   });
//   $(".hamburger-icon").click(function(){
//     $(".hamburger-icon").toggleClass("icon");
//   });
// });
