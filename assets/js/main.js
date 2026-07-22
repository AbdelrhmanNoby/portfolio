// Initialize AOS Animation
document.addEventListener('DOMContentLoaded', function () {
    AOS.init({
        duration: 1000,
        easing: 'ease-in-out',
        once: true,
        mirror: false
    });

    // Theme Toggle Logic
    const themeToggleBtn = document.getElementById('themeToggle');
    const themeToggleIcon = themeToggleBtn ? themeToggleBtn.querySelector('i') : null;

    // Default state: Dark mode, so the icon is the sun to switch to light mode
    if (themeToggleIcon) {
        themeToggleIcon.className = 'fas fa-sun fa-lg';
    }

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', function () {
            document.body.classList.toggle('light-theme');
            const isLight = document.body.classList.contains('light-theme');
            if (themeToggleIcon) {
                themeToggleIcon.className = isLight ? 'fas fa-moon fa-lg' : 'fas fa-sun fa-lg';
            }
        });
    }

    const navbar = document.querySelector('.navbar');
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-link');

    // Navbar Scroll Effect and Scroll to Top
    const scrollTopBtn = document.getElementById('scrollToTop');

    function checkScroll() {
        if (window.scrollY > 50) {
            if (navbar) navbar.classList.add('scrolled');
        } else {
            if (navbar) navbar.classList.remove('scrolled');
        }

        if (window.scrollY > 300) {
            if (scrollTopBtn) scrollTopBtn.classList.add('active');
        } else {
            if (scrollTopBtn) scrollTopBtn.classList.remove('active');
        }
    }

    if (scrollTopBtn) {
        scrollTopBtn.addEventListener('click', function (e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    if (navbar || scrollTopBtn) {
        window.addEventListener('scroll', checkScroll);
        checkScroll();
    }

    // 2. Custom Active Link Highlighting (Fixes ScrollSpy issues)
    function changeLinkState() {
        let index = sections.length;

        // Loop fast backwards to find the first section whose top is above the viewport center
        while (--index && window.scrollY + 150 < sections[index].offsetTop) { }

        navLinks.forEach((link) => link.classList.remove('active'));

        // Match section id with nav-link href
        // Note: navLinks index might not match sections perfectly if Home is first
        // Better robust way: match href ID
        if (index >= 0) {
            const currentId = sections[index].id;
            navLinks.forEach((link) => {
                if (link.getAttribute('href') === `#${currentId}`) {
                    link.classList.add('active');
                }
            });
        }
    }
    window.addEventListener('scroll', changeLinkState);
    changeLinkState(); // Initial check

    // 3. Mobile Menu Handlers
    const menuToggle = document.getElementById('navbarNav');
    if (menuToggle) {
        const bsCollapse = new bootstrap.Collapse(menuToggle, { toggle: false });

        // Close menu when clicking a link
        navLinks.forEach((l) => {
            l.addEventListener('click', () => {
                if (menuToggle.classList.contains('show')) {
                    bsCollapse.hide();
                }
            })
        });

        // Toggle 'mobile-open' class for background
        menuToggle.addEventListener('show.bs.collapse', function () {
            if (navbar) navbar.classList.add('mobile-open');
        });

        menuToggle.addEventListener('hide.bs.collapse', function () {
            if (navbar) navbar.classList.remove('mobile-open');
        });
    }

    // Contact Form Submission (AJAX via FormSubmit.co)
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function (e) {
            e.preventDefault();

            const submitBtn = document.getElementById('submitBtn');
            const btnText = submitBtn.querySelector('.btn-text');
            const spinner = submitBtn.querySelector('.spinner-border');
            const formMessage = document.getElementById('formMessage');

            // Show loading state
            btnText.classList.add('d-none');
            spinner.classList.remove('d-none');
            submitBtn.disabled = true;

            formMessage.classList.add('d-none');
            formMessage.className = 'alert d-none text-center rounded-3 mt-3 mb-0 fw-medium';

            // Gather data
            const formData = new FormData(contactForm);
            const data = Object.fromEntries(formData.entries());

            // Use FormSubmit.co AJAX API
            fetch("https://formsubmit.co/ajax/abdelrhmannobyyoussef@gmail.com", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    _subject: data.subject,
                    name: data.name,
                    email: data.email,
                    message: data.message
                })
            })
                .then(response => response.json())
                .then(result => {
                    // Success
                    formMessage.textContent = "Message sent successfully! I will get back to you soon.";
                    formMessage.classList.add('alert-success-custom');
                    formMessage.classList.remove('d-none');
                    contactForm.reset();
                })
                .catch(error => {
                    // Error
                    formMessage.textContent = "Oops! Something went wrong. Please try again later.";
                    formMessage.classList.add('alert-danger-custom');
                    formMessage.classList.remove('d-none');
                })
                .finally(() => {
                    // Restore button state
                    btnText.classList.remove('d-none');
                    spinner.classList.add('d-none');
                    submitBtn.disabled = false;

                    // Hide message after 5 seconds
                    setTimeout(() => {
                        formMessage.classList.add('d-none');
                    }, 5000);
                });
        });
    }
});


// Initialize tsParticles
if (document.getElementById('tsparticles')) {
    tsParticles.load("tsparticles", {
        fpsLimit: 60,
        interactivity: {
            events: {
                onClick: { enable: true, mode: "push" },
                onHover: { enable: true, mode: "grab" },
                resize: true,
            },
            modes: {
                push: { quantity: 4 },
                grab: { distance: 150, links: { opacity: 0.5 } }
            },
        },
        particles: {
            color: { value: "#64ffda" },
            links: {
                color: "#64ffda",
                distance: 150,
                enable: true,
                opacity: 0.2,
                width: 1,
            },
            collisions: { enable: true },
            move: {
                direction: "none",
                enable: true,
                outModes: { default: "bounce" },
                random: false,
                speed: 1.5,
                straight: false,
            },
            number: { density: { enable: true, area: 800 }, value: 80 },
            opacity: { value: 0.3 },
            shape: { type: "circle" },
            size: { value: { min: 1, max: 3 } },
        },
        detectRetina: true,
    });
}
