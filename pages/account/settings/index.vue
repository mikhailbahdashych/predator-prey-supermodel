<template>
  <div class="account-wrapper">

    <div class="avatar" @click="redirect('/account/me')">
      <img class='avatar-box' src="../../../assets/img/testava.jpg" alt="ava">
      <div class="avatar-text">
        <h2 class="nmp">{{ personalSettings.username }}</h2>
        <p class="paragraph opacity nmp">Public profile</p>
      </div>
    </div>

    <div class="side-bar">
      <div v-for="item in accountHeaderItems" :key="item.title" class="flex">
        <div v-if="item.active" class="vertical-line" />
        <p :class="[item.active ? 'item item-active' : 'item']" @click="changeSubsection(item)">
          {{ item.title }}
        </p>
      </div>
    </div>

    <personal-information v-if="currentSection === 'Public account'" :personal-settings="personalSettings" />
    <security-settings v-else-if="currentSection === 'Security settings'" :security-settings="securitySettings" />
    <site-settings v-else />

  </div>
</template>

<script>
import SecuritySettings from '~/components/pageComponents/settings/SecuritySettings'
import PersonalInformation from '~/components/pageComponents/settings/PersonalInformation'
import SiteSettings from '~/components/pageComponents/settings/SiteSettings'
import { getUserSettings } from "~/api";
export default {
  name: 'Settings',
  components: {
    SecuritySettings,
    PersonalInformation,
    SiteSettings
  },
  data() {
    return {
      accountHeaderItems: [
        { title: 'Public account', active: true },
        { title: 'Security settings', active: false },
        { title: 'Appearance settings', active: false },
        { title: 'Notifications', active: false }
      ],
      currentSection: 'Public account',

      personalSettings: {},
      securitySettings: {},
    }
  },
  async mounted() {
    if (localStorage.getItem('token') !== null) await this.getUsersSettings(localStorage.getItem('token'))
    else await this.$router.push('/')
  },
  methods: {
    async getUsersSettings(token) {
      const userSettings = await getUserSettings(token)

      if (userSettings.status === -1)
        return this.$router.push('/')

      this.personalSettings = userSettings.personalSettings
      this.securitySettings = userSettings.securitySettings
    },
    changeSubsection(item) {
      this.currentSection = item.title
      this.accountHeaderItems.forEach(header => {
        header.active = item.title === header.title
      })
    },
    redirect(path) {
      this.$router.push(path)
    },
  }
}
</script>

<style lang="scss">
@import "../../../assets/css/edit";
</style>
