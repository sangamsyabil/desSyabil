// mobile menu
$(document).ready(function(){
    $(".navbar-mobile-menu-icon").click(function(){
       $(".navbar-mobile-detail-menu").toggle();
       $(".navbar-mobile-account-menu-base").hide();
    });
    $(".navbar-account-user-icon").click(function(){
       $(".navbar-mobile-account-menu-base").toggle();
       $(".navbar-mobile-detail-menu").hide();
    });

    $(".navbar-account-orders-base").click(function(){

    });
});
