// login.js

document.getElementById('login-form').addEventListener('submit', function (event) {
    const email = document.querySelector('[name="email"]').value;
    const password = document.querySelector('[name="password"]').value;

    if (!email || !password) {
        event.preventDefault();
        alert('Both email and password fields are required.');
    }
});

// Add functionality for social login buttons if needed
document.querySelector('.btn-google').addEventListener('click', function (event) {
    // Add any specific actions needed before redirecting to Google login
});

document.querySelector('.btn-facebook').addEventListener('click', function (event) {
    // Add any specific actions needed before redirecting to Facebook login
});
