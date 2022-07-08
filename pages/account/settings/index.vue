<template>
  <div>
    <div class="account-header">
      <div class="account-header-inner">
        <div v-for="item in accountHeaderItems" :key="item.title" class="item-box">
          <p :class="[item.active ? 'item item-active' : 'item']" @click="changeSubpage(item)">
            {{item.title}}
          </p>
        </div>
      </div>
    </div>

    <personal-information v-if="currentSection === 'Personal information'" />
    <security-settings v-else-if="currentSection === 'Security settings'" :security-settings="securitySettings" />
    <site-settings v-else />

  </div>
</template>

<script>
import SecuritySettings from '~/components/pageComponents/settings/SecuritySettings'
import PersonalInformation from '~/components/pageComponents/settings/PersonalInformation'
import SiteSettings from '~/components/pageComponents/settings/SiteSettings'
import {getUserSettings} from "~/api";
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
        { title: 'Personal information', active: true },
        { title: 'Security settings', active: false },
        { title: 'Site settings', active: false }
      ],
      currentSection: 'Personal information',

      personalSettings: {},
      securitySettings: {}
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
    changeSubpage(item) {
      this.currentSection = item.title
      this.accountHeaderItems.forEach(header => {
        header.active = item.title === header.title
      })
    },
  }
}
</script>

<style lang="scss">
@import "../../../assets/css/edit";
</style>
