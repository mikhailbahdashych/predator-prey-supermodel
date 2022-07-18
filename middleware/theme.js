export default function() {
  if (process.server) return
  const t = localStorage.getItem('_t')
  if (!t || t !== '_d' || t !== '_l') {
    localStorage.setItem('_t', '_d')
    document.documentElement.setAttribute('data-theme', 'dark')
  } else {
    document.documentElement.setAttribute('data-theme', t === '_d' ? 'dark' : 'light')
  }
}
