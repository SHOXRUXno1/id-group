!function(){"use strict";var e=$(".home__slide");e.owlCarousel({loop:!0,margin:10,nav:!1,items:1,autoplay:!0,autoplayTimeout:5e3,autoplayHoverPause:!0,responsive:{0:{dots:!1},540:{dots:!0}}}),$(".home__slider-nav .next").click((function(){e.trigger("next.owl.carousel")})),$(".home__slider-nav .prev").click((function(){e.trigger("prev.owl.carousel",[300])}));var o=$(".services__slider");o.owlCarousel({center:!0,loop:!0,margin:30,nav:!1,dots:!1,items:3,responsive:{0:{items:1},520:{items:2},840:{items:3}}}),$(".services__slide-nav .next").click((function(){o.trigger("next.owl.carousel")})),$(".services__slide-nav .prev").click((function(){o.trigger("prev.owl.carousel",[300])}));var t=$(".partner__slider");t.owlCarousel({loop:!0,margin:30,nav:!1,dots:!1,autoWidth:!0,autoplay:!0,autoplayTimeout:3e3,items:7}),$(".partner__slide-nav .next").click((function(){t.trigger("next.owl.carousel")})),$(".partner__slide-nav .prev").click((function(){t.trigger("prev.owl.carousel",[300])}));var r=$(".desktop");$(".nav__menu-burger").click((function(){r.hasClass("active")?(r.removeClass("active"),console.log("true")):(r.addClass("active"),console.log("false"))})),window.addEventListener("load",(function(){setTimeout((function(){document.querySelector(".preloader").classList.add("fade-out"),setTimeout((function(){document.querySelector(".preloader").style.display="none"}),1e3)}),800)}))}();
//# sourceMappingURL=script.e34b02601aa4b70679c4.js.map


$(document).ready(function(){
    $('.serviceSlider').slick();
});

