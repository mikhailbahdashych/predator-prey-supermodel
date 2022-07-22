<template>
  <div class="account-wrapper">

    <div class="account-wrapper__avatar" @click="redirect(`/account/${currentUser.personalId}`)">
      <img class='account-wrapper__avatar__avatar-box' :src="require('../../../assets/img/testava.jpg')" alt="ava">
      <div class="account-wrapper__avatar__avatar-text">
        <h2>{{ currentUser.username }}</h2>
        <p class="opacity">Public profile</p>
      </div>
    </div>

    <div class="account-wrapper__side-bar-wrapper">
      <div class="account-wrapper__side-bar-wrapper__side-bar">
        <div v-for="item in accountHeaderItems" :key="item.title" class="account-wrapper__side-bar-wrapper__side-bar__box">
          <div v-if="item.active" class="account-wrapper__side-bar-wrapper__side-bar__vertical-line" />
          <p :class="[
            item.active ?
            'account-wrapper__side-bar-wrapper__side-bar__item account-wrapper__side-bar-wrapper__side-bar__item--item-active' :
             'account-wrapper__side-bar-wrapper__side-bar__item']"
             @click="changeSubsection(item)">
            {{ item.title }}
          </p>
        </div>
      </div>

      <personal-information v-if="currentSection === 'Public account'" />
      <security-settings v-else-if="currentSection === 'Security settings'" />
      <site-settings v-else-if="currentSection === 'Appearance settings'" />
      <notifications v-else />
    </div>

  </div>
</template>

<script>
import SecuritySettings from '~/components/pageComponents/settings/SecuritySettings'
import PersonalInformation from '~/components/pageComponents/settings/PersonalInformation'
import SiteSettings from '~/components/pageComponents/settings/SiteSettings'
import Notifications from '~/components/pageComponents/settings/Notifications'
import { verifyToken } from '~/helpers/crypto'
export default {
  name: 'Settings',
  components: {
    SecuritySettings,
    PersonalInformation,
    SiteSettings,
    Notifications
  },
  data() {
    return {
      loading: true,
      accountHeaderItems: [
        { title: 'Public account', active: true },
        { title: 'Security settings', active: false },
        { title: 'Appearance settings', active: false },
        { title: 'Notifications', active: false }
      ],
      currentSection: 'Public account',
      currentUser: {}
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

      if (!token)
        return this.$router.push('/signin')

      const tokenData = verifyToken(token)

      if (tokenData.message === 'invalid-token') return this.$router.push('/signin')
      else this.currentUser = tokenData
    },
    changeSubsection(item) {
      this.currentSection = item.title
      this.accountHeaderItems.forEach(header => {
        header.active = item.title === header.title
      })
    },
    redirect(path) {
      return this.$router.push(path)
    },
  }
}
</script>

<style lang="scss">
@import "../../../assets/css/pages/account/settings";
</style>
