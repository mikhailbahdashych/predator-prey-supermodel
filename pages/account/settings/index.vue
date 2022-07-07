<template>
  <div>
    <div class="account-header">
      <div class="account-header-inner">
        <div v-for="item in accountHeaderItems" :key="item.title" :class="[item.active ? 'active' : '']" class="item-box">
          <p :class="[item.active ? 'active' : '']" class="item" @click="changeSubpage(item)">
            {{item.title}}
          </p>
        </div>
      </div>
    </div>

    <personal-information v-if="currentSection === 'Personal information'" />
    <security-settings v-else-if="currentSection === 'Security settings'" />
    <site-settings v-else />

  </div>
</template>

<script>
import SecuritySettings from '~/components/pageComponents/settings/SecuritySettings'
import PersonalInformation from '~/components/pageComponents/settings/PersonalInformation'
import SiteSettings from '~/components/pageComponents/settings/SiteSettings'
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
