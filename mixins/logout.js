import { logout } from '~/api'

export default {
  methods: {
    async logout() {
      await logout(sessionStorage.getItem('_at') )
      sessionStorage.removeItem('_at')
      return this.$router.push('/')
    },
  }
}
