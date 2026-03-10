import re

html_file = 'c:/xampp/htdocs/portfolio/index.html'
css_file = 'c:/xampp/htdocs/portfolio/assets/css/style.css'
js_file = 'c:/xampp/htdocs/portfolio/assets/js/main.js'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Scripts
html = html.replace('<script src="assets/js/main.js"></script>', '<!-- tsParticles -->\n    <script src="https://cdn.jsdelivr.net/npm/tsparticles@2/tsparticles.bundle.min.js"></script>\n    <script src="assets/js/main.js"></script>')

# 2. Update Navbar
old_nav = """            <a class="navbar-brand fw-bold" href="#">
                <span class="text-primary">&lt;</span>Abdelrhman<span class="text-primary">/&gt;</span>
            </a>
            <button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <i class="fas fa-bars fa-lg text-primary"></i>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link active" href="#home">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="#about">About</a></li>
                    <li class="nav-item"><a class="nav-link" href="#skills">Skills</a></li>
                    <li class="nav-item"><a class="nav-link" href="#experience">Experience</a></li>
                    <li class="nav-item"><a class="nav-link" href="#projects">Projects</a></li>
                    <li class="nav-item"><a class="nav-link" href="#education">Education</a></li>
                    <li class="nav-item"><a class="nav-link" href="#contact">Contact</a></li>
                </ul>
            </div>"""

new_nav = """            <a class="navbar-brand fw-bold" href="#">
                <img src="assets/img/logo.png" alt="AN Logo" class="navbar-logo">
            </a>
            <button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <i class="fas fa-bars fa-lg text-primary"></i>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link active" href="#home">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="#about">About</a></li>
                    <li class="nav-item"><a class="nav-link" href="#projects">Projects</a></li>
                    <li class="nav-item"><a class="nav-link" href="#skills">Skills</a></li>
                    <li class="nav-item"><a class="nav-link" href="#experience">Services</a></li>
                    <li class="nav-item"><a class="nav-link" href="#contact">Contact</a></li>
                </ul>
                <div class="d-flex align-items-center gap-3 ms-lg-4 mt-3 mt-lg-0">
                    <button class="btn btn-link text-light-500 p-0 text-decoration-none transition-colors"><i class="fas fa-sun fa-lg"></i></button>
                    <a href="#contact" class="btn btn-primary px-4 py-2 rounded-2 fw-medium">Get In Touch</a>
                </div>
            </div>"""

if old_nav in html:
    html = html.replace(old_nav, new_nav)
else:
    print("Could not find old_nav in HTML")

# 3. Update Hero Section
old_hero_match = re.search(r'<!-- Hero Section -->.*?<!-- About Section -->', html, re.DOTALL)
if old_hero_match:
    old_hero = old_hero_match.group(0)

    new_hero = """<!-- Hero Section -->
    <section id="home" class="min-vh-100 d-flex align-items-center justify-content-center position-relative overflow-hidden text-center">
        <div id="tsparticles"></div>
        <div class="container position-relative z-1 mt-5 pt-5">
            <div class="row justify-content-center">
                <div class="col-lg-10" data-aos="fade-up">
                    <div class="mb-4 d-flex justify-content-center">
                        <div class="availability-pill">
                            <span class="status-dot"></span>
                            Available for new projects
                        </div>
                    </div>
                    <h2 class="text-primary fw-medium mb-3 fs-4">React Frontend Developer — Cairo, Egypt</h2>
                    <h1 class="hero-title-main mb-4">I Help Businesses Launch<br>Beautiful, Fast Web Applications</h1>
                    
                    <p class="lead text-light-500 mb-5 mx-auto w-lg-75">
                        I build elegant, high-performance web experiences that convert<br>
                        visitors into customers. Specialized in React, TypeScript, and modern<br>
                        frontend architecture with production-grade delivery.
                    </p>
                    
                    <div class="d-flex justify-content-center gap-3 flex-wrap flex-md-nowrap mb-5">
                        <a href="#projects" class="btn btn-primary px-4 py-2 rounded-2 fw-medium d-flex align-items-center gap-2">View My Work <i class="fas fa-arrow-right"></i></a>
                        <a href="#contact" class="btn btn-outline-light px-4 py-2 rounded-2 fw-medium border-secondary text-white bg-dark-2 hover-bg-transparent">Let's Connect</a>
                    </div>
                    
                    <div class="social-links-hero d-flex justify-content-center gap-4">
                        <a href="https://github.com/AbdelrhmanNoby" target="_blank" class="text-white transition-colors opacity-75 hover-opacity-100"><i class="fab fa-github fa-2x"></i></a>
                        <a href="https://www.linkedin.com/in/abdelrhman-noby-youssef-a71221213/" target="_blank" class="text-white transition-colors opacity-75 hover-opacity-100"><i class="fab fa-linkedin fa-2x"></i></a>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="mouse-scroll d-none d-md-block"></div>
    </section>

    <!-- About Section -->"""
    html = html.replace(old_hero, new_hero)
else:
    print("Could not find Hero section")

# 4. Update About Section
old_about_match = re.search(r'<!-- About Section -->\s*<section id="about" class="section-padding bg-dark-2">.*?</section>', html, re.DOTALL)
if old_about_match:
    old_about = old_about_match.group(0)

    new_about = """<!-- About Section -->
    <section id="about" class="section-padding bg-dark-2 position-relative">
        <div class="container">
            <div class="row justify-content-center mb-5">
                <div class="col-lg-8" data-aos="fade-up">
                    <div class="section-title text-center">
                        <h2 class="text-white fw-bold display-5 mb-2">About <span class="text-primary">Me</span></h2>
                        <p class="text-light-500">Combining technical expertise with professional communication skills</p>
                    </div>
                </div>
            </div>
            
            <div class="row align-items-center g-5">
                <div class="col-lg-5" data-aos="fade-right">
                    <div class="about-img-wrapper">
                        <img src="assets/img/profile.jpg" alt="Abdelrhman Noby" class="about-img shadow-lg">
                    </div>
                </div>
                
                <div class="col-lg-7" data-aos="fade-left">
                    <div class="about-content ps-lg-4">
                        <h3 class="text-primary fw-medium mb-4 fs-2">Who I Am</h3>
                        <p class="text-light-500 mb-4 lh-lg">
                            I'm a React Frontend Developer who delivers production-ready web applications for real businesses. From enterprise HRMS platforms with 7 interconnected modules to bilingual client websites with RTL support — I focus on building complex, scalable frontends that solve real problems. Computer Science graduate with McKinsey-certified problem-solving skills.
                        </p>
                        <p class="text-light-500 mb-5 lh-lg">
                            I believe great software is built at the intersection of clean architecture, beautiful design, and genuine user empathy. Every component I build is tested, typed, and optimized for the real world.
                        </p>
                        
                        <h3 class="text-primary fw-medium mb-4 fs-2">What I Build</h3>
                        <p class="text-light-500 mb-4 lh-lg">
                            Building enterprise applications with TypeScript, automated testing, and advanced state management patterns — delivering production-grade code through real team collaboration.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>"""
    html = html.replace(old_about, new_about)
else:
    print("Could not find About Section")

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

with open(css_file, 'a', encoding='utf-8') as f:
    f.write('''\n
/* --- NEW STYLES: PORTFOLIO REDESIGN --- */

/* Navbar Logo */
.navbar-logo {
    max-height: 40px;
    width: auto;
    object-fit: contain;
    transition: transform 0.3s ease;
}

.navbar-logo:hover {
    transform: scale(1.05);
}

/* tsParticles Background */
#tsparticles {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
}

/* Hero Pill */
.availability-pill {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 8px 18px;
    background: rgba(100, 255, 218, 0.05);
    border: 1px solid rgba(100, 255, 218, 0.2);
    border-radius: 50px;
    color: var(--primary-color);
    font-size: 0.9rem;
    font-weight: 400;
}

.status-dot {
    width: 8px;
    height: 8px;
    background-color: var(--primary-color);
    border-radius: 50%;
    box-shadow: 0 0 10px var(--primary-color);
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% {
        box-shadow: 0 0 0 0 rgba(100, 255, 218, 0.7);
    }
    70% {
        box-shadow: 0 0 0 10px rgba(100, 255, 218, 0);
    }
    100% {
        box-shadow: 0 0 0 0 rgba(100, 255, 218, 0);
    }
}

/* Hero Typography */
.hero-title-main {
    font-size: 4.5rem;
    font-weight: 800;
    line-height: 1.1;
    color: #fff;
    letter-spacing: -1px;
}

.opacity-75 { opacity: 0.75; }
.hover-opacity-100:hover { opacity: 1 !important; }

/* Mouse Scroll Animation */
.mouse-scroll {
    position: absolute;
    bottom: 40px;
    left: 50%;
    transform: translateX(-50%);
    width: 26px;
    height: 40px;
    border: 2px solid var(--text-slate);
    border-radius: 13px;
    z-index: 2;
    opacity: 0.7;
}

.mouse-scroll::before {
    content: '';
    position: absolute;
    top: 6px;
    left: 50%;
    transform: translateX(-50%);
    width: 4px;
    height: 8px;
    background-color: var(--primary-color);
    border-radius: 2px;
    animation: mouse-scroll-anim 2s infinite;
}

@keyframes mouse-scroll-anim {
    0% { transform: translate(-50%, 0); opacity: 1; }
    100% { transform: translate(-50%, 15px); opacity: 0; }
}

/* Updated Button Styles */
.hover-bg-transparent:hover {
    background-color: transparent !important;
}

/* About Section Image */
.about-img-wrapper {
    position: relative;
    border-radius: 16px;
    overflow: visible;
}

.about-img-wrapper::before {
    content: '';
    position: absolute;
    top: -15px;
    left: -15px;
    bottom: -15px;
    right: -15px;
    background: radial-gradient(circle, rgba(100,255,218,0.15) 0%, rgba(10,25,47,0) 70%);
    z-index: 0;
    opacity: 0.8;
}

.about-img {
    position: relative;
    width: 100%;
    height: auto;
    border-radius: 16px;
    z-index: 1;
    box-shadow: 0 10px 40px rgba(0,0,0,0.4);
    transition: transform 0.3s ease;
}

.about-img-wrapper:hover .about-img {
    transform: translateY(-5px);
}

@media (max-width: 991px) {
    .hero-title-main {
        font-size: 3rem;
    }
}
@media (max-width: 767px) {
    .hero-title-main {
        font-size: 2.2rem;
    }
}
''')

with open(js_file, 'a', encoding='utf-8') as f:
    f.write('''\n
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
''')

print("Update completed successfully.")
