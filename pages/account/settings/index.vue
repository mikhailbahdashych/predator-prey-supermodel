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
        <div class="security-items">
          <div class="security-items">
            <h3 class="font-second danger-text">{{ setting.title }}</h3>
            <p class="font-second danger-text">{{ setting.description }}</p>
          </div>
          <div class="security-items">
            <Button
              :label="setting.buttonTitle"
              :additional-class="`transparent ${setting.danger ? 'danger' : ''}`"
              @click-handler="openModal(setting.title)" />
          </div>
        </div>
      </div>

      <basic-modal
        v-if="securityShowModal['Set 2FA']"
        header="Activate 2FA"
        description="We strongly recommend you to 2FA.
      This will increase the security of you account.
      Before it, you should download Google Authenticator application.
      Once it's done, click the button below to start."
        @close="closeModal('Set 2FA')"
      >
        <Button v-if="!securityTwoFa.qr" :label="'Generate 2FA'" @click-handler="generateTwoFa" />
        <img v-if="securityTwoFa.qr" :src="securityTwoFa.qr" alt="2fa">
<!--        <div v-if="securityTwofa.qr && ([null, -1, -2].includes(securityTwofa.status))">-->
<!--          <InputTwoFa :twofa="securityTwofa.code" @returnTwofa="returnTwofa" :onwhite="true" />-->
<!--          <Button :label="'Confirm 2FA'" :clickon="set2fa" />-->
<!--        </div>-->
<!--        <div v-else-if="securityTwofa.status === 1">-->
<!--          <p class="paragraph medium on-white-paragraph">2FA set successfully</p>-->
<!--        </div>-->
<!--        <div v-if="securityTwofa.status === -1">-->
<!--          <p class="paragraph medium error">Wrong code!</p>-->
<!--        </div>-->
      </basic-modal>

    </div>

    <div v-else class="account-security-content">

    </div>

  </div>
</template>

<script>
import * as node2fa from "node-2fa";
import Button from "~/components/Button";
import BasicModal from "~/components/BasicModal";
import {getUserByToken, getUserSettings} from "~/api";
export default {
  name: "Settings",
  components: {
    Button,
    BasicModal
  },
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
      ],
      securityShowModal: {
        'Set 2FA': false,
        'Close account': false,
        'Change email': false,
        'Change password': false,
        'Disable 2FA': false,
        twoFa: false,
      },

      securityTwoFa: { code: [], qr: null, status: null, secret: null },

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
    },
    openModal(option) {
      Object.entries(this.securityShowModal).forEach(item => {
        if (item[0] === option) this.securityShowModal[item[0]] = true
      })
    },
    closeModal(option) {
      Object.entries(this.securityShowModal).forEach(item => {
        if (item[0] === option) this.securityShowModal[item[0]] = false
      })
    },
    async generateTwoFa() {
      const user = await getUserByToken(localStorage.getItem('token'))
      if (user.status === -1) return

      const { qr, secret } = node2fa.generateSecret({ name: 'PNB - Pentesters Notes Blog', account: user.username })
      this.securityTwoFa.qr = qr
      this.securityTwoFa.secret = secret
    }
  }
}
</script>

<style lang="scss">
@import "../../../assets/css/edit";
</style>
