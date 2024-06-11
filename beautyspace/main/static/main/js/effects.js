$(document).ready(function () {
    $("#page").hide().fadeIn(1000);

    $(".my-card").hover(
        function () {
            $(this).css({
                transform: "scale(1.2)",
                transition: "transform 0.3s ease"
            });
        },
        function () {
            $(this).css({
                transform: "scale(1)",
                transition: "transform 0.3s ease"
            });
        }
    );



});

document.addEventListener('DOMContentLoaded', function() {
        const pulseButtons = document.querySelectorAll('.price-service-button');

        pulseButtons.forEach(function(button) {
            button.addEventListener('mouseover', function() {
                button.classList.add('pulse');
            });

            button.addEventListener('mouseout', function() {
                button.classList.remove('pulse');
            });
        });
    });
