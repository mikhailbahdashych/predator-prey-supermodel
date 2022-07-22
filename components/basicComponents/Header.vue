<template>
  <div class="header">
    <div v-if='loading' class="link-logo"><skeleton :text="'pNb'" /></div>
    <div v-else class="link-logo">
      <nuxt-link no-prefetch to="/">
        <h3 class='logo'>pNb</h3>
      </nuxt-link>
    </div>
    <div class="inner-header">
      <div class="content">
        <div class="content">
          <skeleton v-if='loading' :text="'Q&A'" />
          <div v-else class="link">
            <nuxt-link no-prefetch to="/qa" class='nuxt-link'>
              <p class="link-title">Q&A</p>
            </nuxt-link>
          </div>
          <skeleton v-if='loading' :text="'FORUM'" />
          <div v-else class="link">
            <nuxt-link no-prefetch to="/forum" class='nuxt-link'>
              <p class="link-title">Forum</p>
            </nuxt-link>
          </div>
          <skeleton v-if='loading' :text="'BLOG'" />
          <div v-else class="link">
            <nuxt-link no-prefetch to="/blog" class='nuxt-link'>
              <p class="link-title">Blog</p>
            </nuxt-link>
          </div>
        </div>
        <div class="content">
          <input-search />
        </div>
        <div v-if="userData.status === -1" class="content">
          <div class="button">
            <skeleton v-if='loading' :text="'SIGN IN'" />
            <Button
              v-else
              :label="'SIGN IN'"
              :btn-class="'basic-button--transparent'"
              @click-handler="redirect('/signin')"
            />
          </div>
          <div class="button">
            <skeleton v-if='loading' :text="'SIGN UP'" />
            <Button
              v-else :label="'SIGN UP'"
              @click-handler="redirect('/signup')"
            />
          </div>
        </div>
        <div v-else class="content">
          <div class="button">
            <skeleton v-if='loading' :text="'My account'" />
            <Button
              v-else
              :label="'My account'"
              @click-handler="redirect(`/account/${userData.personalId}`)"
            />
          </div>
          <div class="button">
            <skeleton v-if='loading' :text="'Log Out'" />
            <Button
              v-else
              :label="'Log Out'"
              :btn-class="'basic-button--transparent'"
              @click-handler="logout"
            />
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
    this.decodeToken()
  },
  methods: {
    decodeToken() {
      const token = sessionStorage.getItem('_at')

      if (!token) {
        this.userData.status = -1
        return
      }

      const tokenData = verifyToken(token)
      if (tokenData.message === 'invalid-token') {
        sessionStorage.removeItem('_at')
        this.userData.status = -1
        return this.$router.push('/signin')
      } else {
        this.userData.status = 1;
        this.userData.personalId = tokenData.personalId
      }
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
