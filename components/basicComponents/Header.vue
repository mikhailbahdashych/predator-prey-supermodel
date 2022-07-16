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
          <nuxt-link v-else to="/forum" class='nuxt-link'>
            <h3 class="links">FORUM</h3>
          </nuxt-link>
          <skeleton v-if='loading' :text="'Q&A'" />
          <nuxt-link v-else to="/qa" class='nuxt-link'>
            <h3 class="links">Q&A</h3>
          </nuxt-link>
          <skeleton v-if='loading' :text="'BLOG'" />
          <nuxt-link v-else to="/blog" class='nuxt-link'>
            <h3 class="links">BLOG</h3>
          </nuxt-link>
        </div>
        <div class="content">
          <input-search />
        </div>
        <div v-if="userData.status === -1" class="content">
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
            <Button v-else :label="'My account'" @click-handler="redirect(`/account/${userData.personalId}`)" />
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
import Button from '~/components/basicComponents/Button'
import Skeleton from '~/components/skeleton/Skeleton'
import InputSearch from '~/components/basicComponents/InputSearch'
import { verifyToken } from '~/helpers/crypto'
export default {
  name: 'Header',
  components: {
    Button,
    Skeleton,
    InputSearch
  },
  data() {
    return {
      userData: {},
      loading: true
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
  mounted() {
    const tokenData = this.decodeToken()
    if (tokenData.message === 'invalid-token') {
      sessionStorage.removeItem('_at')
      this.userData.status = -1
      return this.$router.push('/')
    } else {
      this.userData.status = 1;
      this.userData.personalId = tokenData.personalId
    }
  },
  methods: {
    decodeToken() {
      const token = sessionStorage.getItem('_at')
      return verifyToken(token)
    },
    redirect(path) {
      return this.$router.push(path)
    },
    logout() {
      sessionStorage.removeItem('_at')
      return this.$router.push('/')
    },
  }
}
</script>

<style lang='scss'>
@import '../../assets/css/basicComponents/Header';
</style>
