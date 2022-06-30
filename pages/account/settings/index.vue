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
      userSettings: {}
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
