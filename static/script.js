$(document).ready(function() {
    // Hide the floating share buttons initially
    $('.floating-share').css('right', '-100px');

    // Show/hide floating share buttons on scroll
    $(window).scroll(function() {
        var scroll = $(this).scrollTop();
        if (scroll > 100) { // Adjust this value as needed
            $('.floating-share').css('right', '20px'); // Adjust the distance from the right side
        } else {
            $('.floating-share').css('right', '-100px');
        }
    });

    // Menu toggle
    const menuIcon = document.querySelector('.menu-icon img');
    const navMenu = document.querySelector('.main-nav ul');

    menuIcon.addEventListener('click', function() {
        navMenu.classList.toggle('show');
        menuIcon.classList.toggle('active');
    });

    // Accordion functionality
    const accordionHeaders = document.querySelectorAll('.accordion-header');
    accordionHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const isActive = this.classList.contains('active');
            closeAllAccordions();
            if (!isActive) {
                this.classList.add('active');
                this.nextElementSibling.style.display = 'block';
            }
        });
    });

    function closeAllAccordions() {
        accordionHeaders.forEach(header => {
            header.classList.remove('active');
            header.nextElementSibling.style.display = 'none';
        });
    }
});
