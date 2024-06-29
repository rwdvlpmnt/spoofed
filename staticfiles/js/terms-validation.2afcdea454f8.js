document.getElementById('register-form').addEventListener('submit', function(event) {
  const termsCheckbox = document.getElementById('terms');
  if (!termsCheckbox.checked) {
    event.preventDefault();
    alert('You must agree to the terms and conditions before registering.');
  }
});
