// register.js

document.getElementById('register-form').addEventListener('submit', function (event) {
  const termsCheckbox = document.getElementById('terms');
  if (!termsCheckbox.checked) {
    event.preventDefault();
    alert('You must agree to the terms and conditions before registering.');
  }

  const email = document.querySelector('[name="email"]').value;
  const password = document.querySelector('[name="password"]').value;
  const passwordConfirm = document.querySelector('[name="password_confirm"]').value;

  if (password !== passwordConfirm) {
    event.preventDefault();
    alert('Passwords do not match. Please confirm your password.');
  }
});
// register.js

document.getElementById('register-form').addEventListener('submit', function (event) {
  const termsCheckbox = document.getElementById('terms');
  if (!termsCheckbox.checked) {
    event.preventDefault();
    alert('You must agree to the terms and conditions before registering.');
  }

  const email = document.querySelector('[name="email"]').value;
  const password = document.querySelector('[name="password"]').value;
  const passwordConfirm = document.querySelector('[name="password_confirm"]').value;

  if (password !== passwordConfirm) {
    event.preventDefault();
    alert('Passwords do not match. Please confirm your password.');
  }
});
// register.js

document.getElementById('register-form').addEventListener('submit', function (event) {
  const termsCheckbox = document.getElementById('terms');
  if (!termsCheckbox.checked) {
    event.preventDefault();
    alert('You must agree to the terms and conditions before registering.');
  }

  const email = document.querySelector('[name="email"]').value;
  const password = document.querySelector('[name="password"]').value;
  const passwordConfirm = document.querySelector('[name="password_confirm"]').value;

  if (password !== passwordConfirm) {
    event.preventDefault();
    alert('Passwords do not match. Please confirm your password.');
  }
});
