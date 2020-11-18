$(function() {

  $("#owl-demo").owlCarousel({
    autoPlay : 3000,
    loop : true,
    stopOnHover : true,
    navigation:true,
    paginationSpeed : 1000,
    goToFirstSpeed : 2000,
    singleItem : true,
    autoHeight : true,
    transitionStyle:"fade"

  });

});

$('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:5
        }
    }
})

$(function() {
    $("#owl-reviews").owlCarousel({
        loop:true,
        items: 1,
        margin:150,
        stagePadding:1,
        nav:true,
        onTranslated: animateImgFunc,
        onChanged: animateImgClear
    });

//Добавляем класс с анимацией изображения
function animateImgFunc() {
    $(".owl-reviews .active .inner-testimonial img").addClass("animated bounceIn full-opacity");
}

//Удаляем класс с анимацией изображения
function animateImgClear() {
    $(".owl-reviews .active .inner-testimonial img").removeClass("animated bounceIn full-opacity");
}
});
