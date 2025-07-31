// Enhanced Mobile Navigation with Accessibility
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    // Set initial ARIA attributes
    navMenu.setAttribute('id', 'nav-menu');
    hamburger.setAttribute('aria-controls', 'nav-menu');

    // Toggle mobile menu with ARIA support
    hamburger.addEventListener('click', function() {
        const isExpanded = hamburger.getAttribute('aria-expanded') === 'true';
        
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
        
        // Update ARIA attributes
        hamburger.setAttribute('aria-expanded', !isExpanded);
        
        // Focus management
        if (!isExpanded) {
            // When opening menu, focus first menu item
            const firstMenuItem = navMenu.querySelector('.nav-link');
            if (firstMenuItem) {
                firstMenuItem.focus();
            }
        }
    });

    // Close mobile menu when clicking on a nav link
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
            hamburger.setAttribute('aria-expanded', 'false');
        });
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', function(e) {
        if (!hamburger.contains(e.target) && !navMenu.contains(e.target)) {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
            hamburger.setAttribute('aria-expanded', 'false');
        }
    });

    // Keyboard navigation for mobile menu
    navMenu.addEventListener('keydown', function(e) {
        const focusableElements = navMenu.querySelectorAll('.nav-link');
        const currentIndex = Array.from(focusableElements).indexOf(document.activeElement);

        switch(e.key) {
            case 'Escape':
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
                hamburger.setAttribute('aria-expanded', 'false');
                hamburger.focus();
                break;
            case 'ArrowDown':
                e.preventDefault();
                const nextIndex = (currentIndex + 1) % focusableElements.length;
                focusableElements[nextIndex].focus();
                break;
            case 'ArrowUp':
                e.preventDefault();
                const prevIndex = currentIndex === 0 ? focusableElements.length - 1 : currentIndex - 1;
                focusableElements[prevIndex].focus();
                break;
        }
    });

    // Dark Mode Toggle Functionality
    const darkModeToggle = document.querySelector('.dark-mode-toggle');
    const htmlElement = document.documentElement;
    
    // Check for saved theme preference or default to light mode
    const savedTheme = localStorage.getItem('theme') || 'light';
    htmlElement.setAttribute('data-theme', savedTheme);
    
    // Update toggle icon based on current theme
    updateToggleIcon(savedTheme);
    
    // Toggle dark mode when button is clicked
    darkModeToggle.addEventListener('click', function() {
        const currentTheme = htmlElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        // Update theme
        htmlElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        
        // Update toggle icon
        updateToggleIcon(newTheme);
        
        // Update navbar immediately
        updateNavbarForTheme(newTheme);
        
        // Announce theme change to screen readers
        const announcement = newTheme === 'dark' ? 'Dark mode activated' : 'Light mode activated';
        announceToScreenReader(announcement);
    });
    
    // Function to update navbar based on theme
    function updateNavbarForTheme(theme) {
        const navbar = document.querySelector('.navbar');
        const scrollY = window.scrollY;
        
        if (scrollY > 50) {
            if (theme === 'dark') {
                navbar.style.background = 'rgba(15, 23, 42, 0.98)';
                navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.3)';
            } else {
                navbar.style.background = 'rgba(255, 255, 255, 0.98)';
                navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
            }
        } else {
            if (theme === 'dark') {
                navbar.style.background = 'rgba(15, 23, 42, 0.95)';
                navbar.style.boxShadow = 'none';
            } else {
                navbar.style.background = 'rgba(255, 255, 255, 0.95)';
                navbar.style.boxShadow = 'none';
            }
        }
    }
    
    // Function to update toggle icon
    function updateToggleIcon(theme) {
        const icon = darkModeToggle.querySelector('i');
        if (theme === 'dark') {
            icon.className = 'fas fa-sun';
            darkModeToggle.setAttribute('aria-label', 'Switch to light mode');
        } else {
            icon.className = 'fas fa-moon';
            darkModeToggle.setAttribute('aria-label', 'Switch to dark mode');
        }
    }
    
    // Function to announce changes to screen readers
    function announceToScreenReader(message) {
        const announcement = document.createElement('div');
        announcement.setAttribute('aria-live', 'polite');
        announcement.setAttribute('aria-atomic', 'true');
        announcement.className = 'visually-hidden';
        announcement.textContent = message;
        document.body.appendChild(announcement);
        
        // Remove announcement after it's been read
        setTimeout(() => {
            document.body.removeChild(announcement);
        }, 1000);
    }
});

// Smooth Scrolling for Navigation Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            const offsetTop = targetElement.offsetTop - 80; // Account for fixed navbar
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

// Active Navigation Link Highlighting
window.addEventListener('scroll', function() {
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-link');
    
    let currentSection = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop - 100;
        const sectionHeight = section.clientHeight;
        
        if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
            currentSection = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${currentSection}`) {
            link.classList.add('active');
        }
    });
});

// Navbar Background Change on Scroll
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
    
    if (window.scrollY > 50) {
        if (currentTheme === 'dark') {
            navbar.style.background = 'rgba(15, 23, 42, 0.98)';
            navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.3)';
        } else {
            navbar.style.background = 'rgba(255, 255, 255, 0.98)';
            navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
        }
    } else {
        if (currentTheme === 'dark') {
            navbar.style.background = 'rgba(15, 23, 42, 0.95)';
            navbar.style.boxShadow = 'none';
        } else {
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            navbar.style.boxShadow = 'none';
        }
    }
});

// Animation on Scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in');
        }
    });
}, observerOptions);

// Observe elements for animation
document.querySelectorAll('.feature, .timeline-item, .speaker-card, .pricing-card').forEach(el => {
    observer.observe(el);
});

// Enhanced Form Accessibility and Validation
document.addEventListener('DOMContentLoaded', function() {
    const newsletterForm = document.querySelector('.newsletter-form');
    const emailInput = document.querySelector('#email-input');

    if (newsletterForm && emailInput) {
        // Add live validation
        emailInput.addEventListener('blur', function() {
            validateEmail(this);
        });

        emailInput.addEventListener('input', function() {
            // Clear error state when user starts typing
            clearErrorState(this);
        });

        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            if (validateEmail(emailInput)) {
                // Show success message
                showSuccessMessage(emailInput);
                // Reset form
                newsletterForm.reset();
            }
        });
    }

    function validateEmail(input) {
        const email = input.value.trim();
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        
        if (!email) {
            showError(input, 'Email address is required');
            return false;
        } else if (!emailRegex.test(email)) {
            showError(input, 'Please enter a valid email address');
            return false;
        } else {
            clearErrorState(input);
            return true;
        }
    }

    function showError(input, message) {
        // Remove existing error
        clearErrorState(input);
        
        // Add error class
        input.classList.add('error');
        input.setAttribute('aria-invalid', 'true');
        
        // Create error message
        const errorElement = document.createElement('span');
        errorElement.className = 'error-message';
        errorElement.id = input.id + '-error';
        errorElement.textContent = message;
        errorElement.setAttribute('role', 'alert');
        
        // Insert error message after input
        input.parentNode.insertBefore(errorElement, input.nextSibling);
        
        // Update aria-describedby
        const describedBy = input.getAttribute('aria-describedby') || '';
        input.setAttribute('aria-describedby', describedBy + ' ' + errorElement.id);
    }

    function clearErrorState(input) {
        input.classList.remove('error');
        input.setAttribute('aria-invalid', 'false');
        
        // Remove error message
        const errorElement = input.parentNode.querySelector('.error-message');
        if (errorElement) {
            errorElement.remove();
        }
        
        // Clean up aria-describedby
        const describedBy = input.getAttribute('aria-describedby');
        if (describedBy) {
            const cleaned = describedBy.replace(input.id + '-error', '').trim();
            input.setAttribute('aria-describedby', cleaned);
        }
    }

    function showSuccessMessage(input) {
        // Create success message
        const successElement = document.createElement('span');
        successElement.className = 'success-message';
        successElement.textContent = 'Thank you! You have been subscribed to updates.';
        successElement.setAttribute('role', 'status');
        successElement.setAttribute('aria-live', 'polite');
        
        // Insert success message
        input.parentNode.insertBefore(successElement, input.nextSibling);
        
        // Remove success message after 5 seconds
        setTimeout(() => {
            if (successElement.parentNode) {
                successElement.remove();
            }
        }, 5000);
    }
});

// Registration Button Handlers
document.querySelectorAll('.pricing-card .btn').forEach(button => {
    button.addEventListener('click', function(e) {
        e.preventDefault();
        const cardTitle = this.closest('.pricing-card').querySelector('h3').textContent;
        showNotification(`Registration for ${cardTitle} ticket initiated! You would be redirected to payment.`, 'info');
    });
});

// Hero Button Handlers
document.querySelectorAll('.hero-buttons .btn').forEach(button => {
    button.addEventListener('click', function(e) {
        if (this.textContent.includes('Register')) {
            e.preventDefault();
            document.querySelector('#register').scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Notification System
function showNotification(message, type = 'info') {
    // Remove existing notification
    const existing = document.querySelector('.notification');
    if (existing) {
        existing.remove();
    }

    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <span class="notification-message">${message}</span>
            <button class="notification-close">&times;</button>
        </div>
    `;

    // Add styles
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        background: ${type === 'success' ? '#10b981' : type === 'error' ? '#ef4444' : '#2563eb'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
        z-index: 10000;
        max-width: 400px;
        transform: translateX(100%);
        transition: transform 0.3s ease;
    `;

    notification.querySelector('.notification-content').style.cssText = `
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
    `;

    notification.querySelector('.notification-close').style.cssText = `
        background: none;
        border: none;
        color: white;
        font-size: 1.5rem;
        cursor: pointer;
        padding: 0;
        line-height: 1;
    `;

    // Add to page
    document.body.appendChild(notification);

    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);

    // Auto remove after 5 seconds
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            if (notification.parentNode) {
                notification.remove();
            }
        }, 300);
    }, 5000);

    // Close button handler
    notification.querySelector('.notification-close').addEventListener('click', () => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            if (notification.parentNode) {
                notification.remove();
            }
        }, 300);
    });
}

// Dynamic Year Update
document.addEventListener('DOMContentLoaded', function() {
    const currentYear = new Date().getFullYear();
    const yearElements = document.querySelectorAll('.current-year');
    yearElements.forEach(el => {
        el.textContent = currentYear;
    });
});

// Conference Countdown Timer
function updateCountdown() {
    const conferenceDate = new Date('2025-09-15T09:00:00');
    const now = new Date();
    const timeDifference = conferenceDate - now;

    if (timeDifference > 0) {
        const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
        
        // If there's a countdown element, update it
        const countdownEl = document.querySelector('.countdown');
        if (countdownEl) {
            countdownEl.innerHTML = `
                <div class="countdown-item">
                    <span class="countdown-number">${days}</span>
                    <span class="countdown-label">Days</span>
                </div>
                <div class="countdown-item">
                    <span class="countdown-number">${hours}</span>
                    <span class="countdown-label">Hours</span>
                </div>
                <div class="countdown-item">
                    <span class="countdown-number">${minutes}</span>
                    <span class="countdown-label">Minutes</span>
                </div>
            `;
        }
    }
}

// Update countdown every minute
setInterval(updateCountdown, 60000);
updateCountdown(); // Initial call

// Back to Top Button
function createBackToTopButton() {
    const backToTop = document.createElement('button');
    backToTop.innerHTML = '<i class="fas fa-arrow-up"></i>';
    backToTop.className = 'back-to-top';
    backToTop.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 50px;
        height: 50px;
        background: #4B9CD3;
        color: white;
        border: none;
        border-radius: 50%;
        cursor: pointer;
        display: none;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
        box-shadow: 0 4px 12px rgba(75, 156, 211, 0.3);
        transition: all 0.3s ease;
        z-index: 1000;
    `;

    backToTop.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    backToTop.addEventListener('mouseenter', () => {
        backToTop.style.transform = 'scale(1.1)';
        backToTop.style.background = '#13294B';
    });

    backToTop.addEventListener('mouseleave', () => {
        backToTop.style.transform = 'scale(1)';
        backToTop.style.background = '#4B9CD3';
    });

    document.body.appendChild(backToTop);

    // Show/hide based on scroll position
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            backToTop.style.display = 'flex';
        } else {
            backToTop.style.display = 'none';
        }
    });
}

// Initialize back to top button
document.addEventListener('DOMContentLoaded', createBackToTopButton);

// Lazy Loading for Images (if added later)
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });

    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

// Performance: Preload critical resources
document.addEventListener('DOMContentLoaded', function() {
    // Preload fonts
    const fontLink = document.createElement('link');
    fontLink.rel = 'preload';
    fontLink.href = 'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap';
    fontLink.as = 'style';
    document.head.appendChild(fontLink);
});

// Analytics placeholder (replace with actual analytics code)
function trackEvent(category, action, label) {
    // Placeholder for analytics tracking
    console.log(`Analytics: ${category} - ${action} - ${label}`);
    
    // Example Google Analytics 4 event (uncomment and configure when ready):
    // gtag('event', action, {
    //     event_category: category,
    //     event_label: label
    // });
}

// Track button clicks
document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('click', function() {
        const buttonText = this.textContent.trim();
        trackEvent('Button', 'Click', buttonText);
    });
});

// Track section views
const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const sectionId = entry.target.id;
            trackEvent('Section', 'View', sectionId);
        }
    });
}, { threshold: 0.5 });

document.querySelectorAll('section[id]').forEach(section => {
    sectionObserver.observe(section);
});
