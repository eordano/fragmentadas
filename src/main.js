window.addEventListener('load', function() {
  const EPISODES = "{{ episodes | join(',') }}".split(',')

  function randomNext() {
    return EPISODES[Math.floor(Math.random() * EPISODES.length)]
  }

  const random = document.getElementById('random')
  random.setAttribute('href', '/ep/' + randomNext())
  random.style.display = 'flex'
})
