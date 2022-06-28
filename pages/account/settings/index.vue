<template>
  <div>
    <div class="account-header">
      <div class="account-header-inner">
        <div v-for="item in accountHeaderItems" class="account-header-item-block" :key="item.title" :class="[item.active ? 'active' : '']">
          <p :class="[item.active ? 'active' : '']" class="account-header-item" @click="changeSubpage(item)">
            {{item.title}}
          </p>
        </div>
      </div>
    </div>


    <div class="account-security-content" v-if="currentSection === 'User settings'">

    </div>

    <div class="account-security-content" v-else-if="currentSection === 'Security settings'">

    </div>

    <div class="account-security-content" v-else>

    </div>

  </div>
</template>

<script>
import {verifyClientByToken} from "~/helpers/auth";
export default {
  name: "Settings",
  data() {
    return {
      accountHeaderItems: [
        { title: 'User settings', active: true },
        { title: 'Security settings', active: false },
        { title: 'Global settings', active: false },
      ],
      currentSection: 'User settings'
    }
  },
  async mounted() {
    await verifyClientByToken(this.$router, localStorage.getItem('token'))
  },
  methods: {
    changeSubpage(item) {
      this.accountHeaderItems.forEach(header => { header.active = item.title === header.title })
    }
  }
}
</script>

<style lang="scss">
@import "../../../assets/css/edit";
</style>
