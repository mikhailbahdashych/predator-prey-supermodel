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
            <Button :label="'SIGN IN'" :additional-class="'transparent'" @click-handler="redirect('/signin')" />
          </div>
          <div class="button">
            <Button :label="'SIGN UP'" @click-handler="redirect('/signup')" />
          </div>
        </div>
        <div v-else class="content">
          <div class="button">
            <Button :label="'My account'" @click-handler="redirect(`/account/${tokenStatus}`)" />
          </div>
          <div class="button">
            <Button :label="'Log Out'" :additional-class="'transparent'" @click-handler="logout" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Button from "~/components/Button";
import Skeleton from '~/components/skeleton/Skeleton'
import {getUserByToken} from "~/api";
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
  async mounted() {
    await this.checkToken(localStorage.getItem('token'))
  },
  methods: {
    async checkToken(token) {
      const t = await getUserByToken(token);
      this.tokenStatus = t.status || t.personalId
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
