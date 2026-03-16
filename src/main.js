(function() {
  window.addEventListener('load', function() {
    document.getElementById('random').setAttribute('href', '/ep/' + randomNext())
  });
  function randomNext() {
    return EPISODES[Math.floor(Math.random() * EPISODES.length)]
  }
  var EPISODES = [{{ episodes | join(', ') }}];
})();
