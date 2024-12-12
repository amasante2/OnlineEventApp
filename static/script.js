// Simple form validation for registration
document.getElementById('registerForm').onsubmit = function(event) {
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    if (password !== confirmPassword) {
        alert('Passwords do not match!');
        event.preventDefault();  // Prevent form submission
    }
};
