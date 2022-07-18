export default function() {
  if (process.server) return
  const t = localStorage.getItem('_t')
  if (!t) {
    localStorage.setItem('_t', '_d')
    document.documentElement.setAttribute('data-theme', 'dark')
  } else {
    document.documentElement.setAttribute('data-theme', t === '_l' ? 'light' : 'dark')
  }
}
