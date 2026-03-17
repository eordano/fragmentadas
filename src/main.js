window.addEventListener('load', function() {
  const EPISODES = "{{ episodes | join(',') }}".split(',')

  function randomNext() {
    return EPISODES[Math.floor(Math.random() * EPISODES.length)]
  }

  document.getElementById('random').setAttribute('href', '/ep/' + randomNext())
})
