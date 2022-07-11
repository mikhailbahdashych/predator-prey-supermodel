<template>
  <div class="header">
    <div class="inner-header">
      <div class="content">
        <div class="content">
          <skeleton v-if='loading' :text="'pNb'" />
          <nuxt-link v-else to="/" class='nuxt-link'>
            <h3 class="links logo">pNb</h3>
          </nuxt-link>
          <skeleton v-if='loading' :text="'FORUM'" />
          <nuxt-link v-else to="/" class='nuxt-link'>
            <h3 class="links">FORUM</h3>
          </nuxt-link>
          <skeleton v-if='loading' :text="'Q&A'" />
          <nuxt-link v-else to="/" class='nuxt-link'>
            <h3 class="links">Q&A</h3>
          </nuxt-link>
          <skeleton v-if='loading' :text="'BLOG'" />
          <nuxt-link v-else to="/" class='nuxt-link'>
            <h3 class="links">BLOG</h3>
          </nuxt-link>
        </div>
        <div v-if="tokenStatus === -1" class="content">
          <div class="button">
            <skeleton v-if='loading' :text="'SIGN IN'" />
            <Button v-else :label="'SIGN IN'" :additional-class="'transparent'" @click-handler="redirect('/signin')" />
          </div>
          <div class="button">
            <skeleton v-if='loading' :text="'SIGN UP'" />
            <Button v-else :label="'SIGN UP'" @click-handler="redirect('/signup')" />
          </div>
        </div>
        <div v-else class="content">
          <div class="button">
            <skeleton v-if='loading' :text="'My account'" />
            <Button v-else :label="'My account'" @click-handler="redirect('/account/me')" />
          </div>
          <div class="button">
            <skeleton v-if='loading' :text="'Log Out'" />
            <Button v-else :label="'Log Out'" :additional-class="'transparent'" @click-handler="logout" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Button from "~/components/Button";
import Skeleton from '~/components/skeleton/Skeleton';
export default {
  name: 'Header',
  components: {
    Button,
    Skeleton
  },
  data() {
    return {
      tokenStatus: -1,
      loading: true
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
  mounted() {
    this.tokenStatus = sessionStorage.getItem('accessToken') ? 1 : -1;
  },
  methods: {
    redirect(path) {
      return this.$router.push(path)
    },
    logout() {
      sessionStorage.removeItem('accessToken')
      return this.$router.push('/')
    },
  }
}
</script>

<style lang='scss'>
@import '../assets/css/components/Header';
</style>
