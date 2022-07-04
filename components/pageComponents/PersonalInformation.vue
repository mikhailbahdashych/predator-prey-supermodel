<template>
  <div>
    <div class="account-security-content">

    </div>
  </div>
</template>

<script>
import { getUserSettings } from '~/api'
export default {
  name: 'PersonalInformation',
  data() {
    return {
      personalInfo: {}
    }
  },
  async mounted() {
    if (localStorage.getItem('token') !== null) await this.getUserPersonalInfo(localStorage.getItem('token'))
    else await this.$router.push('/')
  },
  methods: {
    async getUserPersonalInfo(token) {
      this.personalInfo = await getUserSettings(token, 'p')
      if (this.personalInfo.status === -1)
        return this.$router.push('/')
    }
  },
}
</script>

<style lang="scss">
@import "../../assets/css/edit";
</style>
