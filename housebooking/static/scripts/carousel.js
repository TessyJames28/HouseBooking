$(document).ready(function() {
    $('#carousel-container').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 5000,
    dots: true,
    arrows: false,
    infinite: true,
    appendDots: '#carousel-dots'
  });
});