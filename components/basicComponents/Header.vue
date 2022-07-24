<template>
  <div class="header">
    <div v-if='loading' class="header__link-logo"><skeleton :text="'pNb'" /></div>
    <div v-else class="header__link-logo">
      <nuxt-link class="header__link-logo__logo" no-prefetch to="/">
        <h3>pNb</h3>
      </nuxt-link>
    </div>
    <div class="header__inner-header">
      <div class="header__inner-header__content">
        <div class="header__inner-header__content">
          <skeleton v-if='loading' :text="'Q&A'" />
          <div v-else class="header__inner-header__content__link">
            <nuxt-link no-prefetch to="/qa" class='header__inner-header__content__link__link-title'>
              <p>Q&A</p>
            </nuxt-link>
          </div>
          <skeleton v-if='loading' :text="'FORUM'" />
          <div v-else class="header__inner-header__content__link">
            <nuxt-link no-prefetch to="/forum" class='header__inner-header__content__link__link-title'>
              <p>Forum</p>
            </nuxt-link>
          </div>
          <skeleton v-if='loading' :text="'BLOG'" />
          <div v-else class="header__inner-header__content__link">
            <nuxt-link no-prefetch to="/blog" class='header__inner-header__content__link__link-title'>
              <p>Blog</p>
            </nuxt-link>
          </div>
        </div>
        <div class="header__inner-header__content">
          <input-search />
        </div>
        <div v-if="userData.status === -1" class="header__inner-header__content">
          <div class="header__inner-header__content__button">
            <skeleton v-if='loading' :text="'SIGN IN'" />
            <Button
              v-else
              :label="'SIGN IN'"
              :btn-class="'basic-button--transparent'"
              @click-handler="redirect('/signin')"
            />
          </div>
          <div class="header__inner-header__content__button">
            <skeleton v-if='loading' :text="'SIGN UP'" />
            <Button
              v-else :label="'SIGN UP'"
              @click-handler="redirect('/signup')"
            />
          </div>
        </div>
        <div v-else class="header__inner-header__content">
          <div class="header__inner-header__content__button">
            <skeleton v-if='loading' :text="'My account'" />
            <Button
              v-else
              :label="'My account'"
              @click-handler="redirect(accountRedirect)"
            />
          </div>
          <div class="header__inner-header__content__button">
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
      loading: true,
      accountRedirect: null
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
      this.userData.status = tokenData.message === 'invalid-token' ? -1 : 1;
      this.accountRedirect = tokenData.message === 'invalid-token' ? '/signin' : `/account/${tokenData.personalId}`;
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
