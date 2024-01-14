document.getElementById('explore').addEventListener('click', function() {
  var hidden_posts = document.querySelectorAll('.hidden');
    for (var i = 0; i < hidden_posts.length; i++) {
       hidden_posts[i].classList.remove('hidden');
  }
  var special_card = document.querySelector('.special_card')
  special_card.classList.remove('special_card')
});
