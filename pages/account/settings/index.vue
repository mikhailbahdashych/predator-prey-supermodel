<template>
  <div class="account-wrapper">

    <div class="avatar" @click="redirect(`/account/${decodeToken()}`)">
      <img class='avatar-box' :src="require('../../../assets/img/testava.jpg')" alt="ava">
      <div class="avatar-text">
        <h2 class="nmp">{{ currentUser.username }}</h2>
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

    <personal-information v-if="currentSection === 'Public account'" />
    <security-settings v-else-if="currentSection === 'Security settings'" />
    <site-settings v-else />

  </div>
</template>

<script>
import SecuritySettings from '~/components/pageComponents/settings/SecuritySettings'
import PersonalInformation from '~/components/pageComponents/settings/PersonalInformation'
import SiteSettings from '~/components/pageComponents/settings/SiteSettings'
import { getUserByAccessToken } from "~/api";
import { verifyToken } from '~/helpers/crypto'
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
      currentUser: {}
    }
  },
  async mounted() {
    if (sessionStorage.getItem('_at')) await this.getCurrentUser(sessionStorage.getItem('_at'))
    else return this.$router.push('/')
  },
  methods: {
    async getCurrentUser(token) {
      this.currentUser = await getUserByAccessToken(token)

      if (this.currentUser === -1)
        return this.redirect('/')
    },
    decodeToken() {
      const { personalId } = verifyToken(sessionStorage.getItem('_at'))
      return personalId
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
@import "../../../assets/css/edit";
</style>
