$(document).ready(function() {
    $('.menu-toggle').click(function() {
        $('#navbarNav').toggleClass('show');
    });

    // Закрытие меню при клике на ссылку внутри него
    $('#navbarNav .nav-link').click(function() {
        $('#navbarNav').removeClass('show');
    });

    // Закрытие меню при клике вне его области
    $(document).click(function(event) {
        if (!$(event.target).closest('.menu-toggle, #navbarNav').length) {
            $('#navbarNav').removeClass('show');
        }
    });

});
