<template>
  <div class="account-wrapper">

    <div class="account-wrapper__avatar" @click="redirect(`/account/${currentUser.personalId}`)">
      <img class='account-wrapper__avatar-box' :src="require('../../../assets/img/testava.jpg')" alt="ava">
      <div class="account-wrapper__avatar-text">
        <skeleton v-if="loading" />
        <h2 v-else>{{ currentUser.username }}</h2>
        <p class="opacity">Public profile</p>
      </div>
    </div>

    <div class="account-wrapper__side-bar-wrapper">
      <div class="account-wrapper__side-bar">
        <div v-for="item in accountHeaderItems" :key="item.title" class="account-wrapper__box">
          <div v-if="item.active" class="account-wrapper__vertical-line" />
          <p :class="[
            item.active ?
            'account-wrapper__item account-wrapper__item--item-active' :
             'account-wrapper__item']"
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
import Skeleton from '~/components/skeleton/Skeleton'
import { verifyToken } from '~/helpers/crypto'
export default {
  name: 'Settings',
  components: {
    SecuritySettings,
    PersonalInformation,
    SiteSettings,
    Notifications,
    Skeleton
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
    this.getCurrentUser()
  },
  methods: {
    getCurrentUser() {
      const token = sessionStorage.getItem('_at')
      const tokenData = verifyToken(token)
      this.currentUser = {
        personalId: tokenData.personalId,
        username: tokenData.username,
      }
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
