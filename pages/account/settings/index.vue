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

    <security-settings v-else-if="currentSection === 'Security settings'" />

    <div v-else class="account-security-content">

    </div>

  </div>
</template>

<script>
import SecuritySettings from '~/components/pageComponents/SecuritySettings'
export default {
  name: 'Settings',
  components: {
    SecuritySettings
  },
  data() {
    return {
      accountHeaderItems: [
        { title: 'Personal information', active: true },
        { title: 'Security settings', active: false },
        { title: 'Site settings', active: false }
      ],
      currentSection: 'Personal information',
      userSettings: {},
    }
  },
  methods: {
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
