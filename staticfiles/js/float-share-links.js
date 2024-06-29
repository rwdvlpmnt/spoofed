function shareFacebook() {
  window.open('https://www.facebook.com/sharer/sharer.php?u=https://example.com', '_blank');
}

function shareTwitter() {
  window.open('https://twitter.com/intent/tweet?url=https://example.com', '_blank');
}

function shareLinkedIn() {
  window.open('https://www.linkedin.com/shareArticle?url=https://example.com', '_blank');
}

// Facebook SDK initialization
window.fbAsyncInit = function () {
  FB.init({
    appId: 'your-app-id', // Replace 'your-app-id' with your actual Facebook App ID
    cookie: true,
    xfbml: true,
    version: 'v11.0'
  });
};

(function (d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) { return; }
  js = d.createElement(s); js.id = id;
  js.src = "https://connect.facebook.net/en_US/sdk.js";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

document.addEventListener('scroll', function() {
  const shareButtonsContainer = document.querySelector('.share-buttons-container');
  if (window.scrollY > 100) { // Show buttons after scrolling 100px
    shareButtonsContainer.style.display = 'block';
  } else {
    shareButtonsContainer.style.display = 'none';
  }
});
