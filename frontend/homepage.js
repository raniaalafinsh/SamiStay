// Function to navigate to specific pages
function navigateTo(page) {
    if (page === 'login') {
        window.location.href = 'login.html'; // Navigate to the login page
    } else if (page === 'signup') {
        window.location.href = 'signup.html'; // Navigate to the signup page
    } else if (page === 'apartments') {
        window.location.href = 'apartmentlisting.html'; // Example for future page
    }
}

// Add event listeners after DOM loads
document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('login-btn').addEventListener('click', () => navigateTo('login'));
    document.getElementById('signup-btn').addEventListener('click', () => navigateTo('signup'));
});
