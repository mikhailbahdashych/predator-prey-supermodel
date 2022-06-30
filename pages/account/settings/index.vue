<template>
  <div>
    <div class="account-header">
      <div class="account-header-inner">
        <div v-for="item in accountHeaderItems" :key="item.title" :class="[item.active ? 'active' : '']" class="account-header-item-block">
          <p :class="[item.active ? 'active' : '']" class="account-header-item" @click="changeSubpage(item)">
            {{item.title}}
          </p>
        </div>
      </div>
    </div>


    <div v-if="currentSection === 'Personal information'" class="account-security-content">

    </div>

    <div v-else-if="currentSection === 'Security settings'" class="account-security-content">

      <div v-for="setting in securitySettingsOptions" :key="setting.title" :class="`security-item ${setting.danger ? 'danger' : ''}`">
        <div class="security-item-content">
          <h3 class="font-second">{{ setting.title }}</h3>
          <p class="font-second">{{ setting.description }}</p>
        </div>
      </div>

    </div>

    <div v-else class="account-security-content">

    </div>

  </div>
</template>

<script>
import {getUserSettings} from "~/api";
export default {
  name: "Settings",
  data() {
    return {
      accountHeaderItems: [
        { title: 'Personal information', active: true },
        { title: 'Security settings', active: false },
        { title: 'Site settings', active: false },
      ],
      currentSection: 'Personal information',
      userSettings: {},

      securitySettingsOptions: [
        { title: 'Set 2FA', description: 'Secure your account with Two-factor authentication (2FA).', buttonTitle: 'Set 2FA', danger: false },
        { title: 'Change password', description: 'You are able to change email only one time.', buttonTitle: 'Change password', danger: false },
        { title: 'Change email', description: 'You are able to change email only one time.', buttonTitle: 'Change email', danger: false },
        { title: 'Close account', description: 'After closing account all information about it will be deleted.', buttonTitle: 'Close', danger: true }
      ]
    }
  },
  async mounted() {
    if (localStorage.getItem('token') !== null) await this.getUsersSettings(localStorage.getItem('token'))
    else await this.$router.push('/')
  },
  methods: {
    async getUsersSettings(token) {
      this.userSettings = await getUserSettings(token)
      if (this.userSettings.status === -1)
        return this.$router.push('/')
    },
    changeSubpage(item) {
      this.currentSection = item.title
      this.accountHeaderItems.forEach(header => { header.active = item.title === header.title })
    }
  }
}
</script>

<style lang="scss">
@import "../../../assets/css/edit";
</style>
