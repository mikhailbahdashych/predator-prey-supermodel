<template>
  <div class="header">
    <div class="inner-header">
      <div class="header-content">
        <div class="header-content">
          <nuxt-link to="/" class='nuxt-link'>
            <h3 class="header-links logo">pNb</h3>
          </nuxt-link>
          <nuxt-link to="/" class='nuxt-link'>
            <h3 class="header-links">FORUM</h3>
          </nuxt-link>
          <nuxt-link to="/" class='nuxt-link'>
            <h3 class="header-links">Q&A</h3>
          </nuxt-link>
          <nuxt-link to="/" class='nuxt-link'>
            <h3 class="header-links">BLOG</h3>
          </nuxt-link>
        </div>
        <div class="header-content" v-if="!token">
          <div class="header-button">
            <Button @click-handler="redirect('/signin')" :label="'SIGN IN'" :additional-class="'transparent'" />
          </div>
          <div class="header-button">
            <Button @click-handler="redirect('/signup')" :label="'SIGN UP'" />
          </div>
        </div>
        <div class="header-content" v-else>
          <div class="header-button">
            <Button :label="'My account'" />
          </div>
          <div class="header-button">
            <Button @click-handler="logout" :label="'Log Out'" :additional-class="'transparent'" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Button from "~/components/Button";
export default {
  name: 'Header',
  components: {
    Button
  },
  data() {
    return {
      token: null
    }
  },
  mounted() {
    this.checkToken()
  },
  methods: {
    checkToken() {
      this.token = !!localStorage.getItem('token');
    },
    redirect(path) {
      this.$router.push({ path })
    },
    logout() {
      localStorage.removeItem('token')
      this.$router.push({ path: '/' })
    },
  }
}
</script>

<style lang='scss'>
@import '../assets/css/components/Header';
</style>
