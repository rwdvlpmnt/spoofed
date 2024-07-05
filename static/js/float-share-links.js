function shareFacebook(page) {
  const url = encodeURIComponent(window.location.origin + '/' + page);
  window.open(`https://www.facebook.com/sharer/sharer.php?u=${url}`, '_blank');
}

function shareTwitter(page) {
  const url = encodeURIComponent(window.location.origin + '/' + page);
  window.open(`https://twitter.com/intent/tweet?url=${url}`, '_blank');
}

function shareLinkedIn(page) {
  const url = encodeURIComponent(window.location.origin + '/' + page);
  window.open(`https://www.linkedin.com/shareArticle?url=${url}`, '_blank');
}

// Facebook SDK initialization
window.fbAsyncInit = function () {
  FB.init({
    appId: '3706290656326007',
    cookie: true,
    xfbml: true,
    version: 'v20.0'
  });

  FB.AppEvents.logPageView();
};

// Load the Facebook SDK asynchronously
(function (d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) { return; }
  js = d.createElement(s); js.id = id;
  js.src = "https://connect.facebook.net/en_US/sdk.js";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

// Show share buttons on scroll
document.addEventListener('scroll', function () {
  const shareButtonsContainer = document.querySelector('.share-buttons-container');
  if (window.scrollY > 100) { // Show buttons after scrolling 100px
    shareButtonsContainer.style.display = 'block';
  } else {
    shareButtonsContainer.style.display = 'none';
  }
});
