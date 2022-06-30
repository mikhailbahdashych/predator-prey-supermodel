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
        <Button v-if="!securityTwoFa.qr && securityTwoFa.status !== 1" :label="'Generate 2FA'" @click-handler="generateTwoFa" />
        <div v-if="securityTwoFa.qr && securityTwoFa.status !== 1" class="center">
          <img :src="securityTwoFa.qr" alt="2fa">
          <InputTwoFa :twofa="securityTwoFa.code" :onwhite="true" :disabled="securityTwoFa.status === 1" @returnTwoFa="returnTwoFa" />
          <Button :label="'Confirm 2FA code'" :additional-class="'big'" :disabled="securityTwoFa.disabledButton || securityTwoFa.status === 1" @click-handler="setTwoFa" />
          <p v-if="securityTwoFa.status === 1" class="paragraph success">2FA has been successfully set!</p>
        </div>
        <div v-if="securityTwoFa.status === 1" class="center">
          <p class="paragraph on-white-paragraph">You have set up your 2FA, provide the code in input below, if you want to deactivate it.
            <span class="paragraph error">(Strongly isn't recommend!)</span>
          </p>
          <InputTwoFa :twofa="securityTwoFa.code" :onwhite="true" @returnTwoFa="returnTwoFa" />
          <Button :label="'Confirm 2FA disable'" :additional-class="'danger-fill'" :disabled="securityTwoFa.disabledButton || securityTwoFa.status === 0" @click-handler="disableTwoFa" />
          <p v-if="securityTwoFa.status === 0" class="paragraph success">2FA has been successfully disabled!</p>
        </div>
      </basic-modal>

      <basic-modal
        v-if="securityShowModal['Close account']"
        header="Close account"
        description="We are very sorry about this :( You can get back any time you want. Hope, to see you again."
        @close="closeModal('Close account')"
      >

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
import InputTwoFa from "~/components/InputTwoFa";
import {disableTwoFa, getUserByToken, getUserSettings, setTwoFa} from "~/api";
export default {
  name: "Settings",
  components: {
    Button,
    BasicModal,
    InputTwoFa
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
      securityTwoFa: { code: [], normalCode: null, qr: null, status: null, secret: null, disabledButton: true },

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

      if (this.userSettings.twoFa)
        this.securityTwoFa.status = 1

      // @TODO Fix big bug buttons
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
    returnTwoFa(twoFa) {
      this.securityTwoFa.disabledButton = !(twoFa.join('').length === 6)
      if (twoFa.length !== 6 || twoFa.join('').length !== 6) return
      this.securityTwoFa.normalCode = twoFa.join('')
    },
    async setTwoFa() {
      const { status } = await setTwoFa({
        twoFaCode: this.securityTwoFa.normalCode,
        twoFaToken: this.securityTwoFa.secret,
        token: localStorage.getItem('token')
      })
      this.securityTwoFa = { code: [], normalCode: null, qr: null, status, secret: null, disabledButton: true }
    },
    async disableTwoFa() {
      const { status } = await disableTwoFa({
        twoFa: this.securityTwoFa.code.join(''),
        token: localStorage.getItem('token')
      })
      this.securityTwoFa = { code: [], normalCode: null, qr: null, status: status === 1 ? 0 : -1, secret: null, disabledButton: true }
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
