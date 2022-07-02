<template>
  <div>
    <Popup v-if="showPopup" :content="'Copied!'" />
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
        <div v-if="setting.title === 'Set 2FA'" class="security-items">
          <div class="security-items">
            <h3 class="font-second">{{ securityTwoFa.status === 2 ? 'Disable 2FA' : setting.title }}</h3>
            <p class="font-second">{{ securityTwoFa.status === 2 ? 'You have set up Two-factor authentication (2FA) for your account.' : setting.description}}</p>
          </div>
          <div class="security-items">
            <Button
              :label="securityTwoFa.status === 2 ? 'Disable 2FA' : setting.buttonTitle"
              :additional-class="`transparent`"
              @click-handler="openModal(securityTwoFa.status === 2 ? 'Disable 2FA' : setting.title)" />
            <Button
              v-if="setting.title === 'Close account'"
              :label="'Show more'"
              @click-handler="stateShowCloseAccMoreInfo" />
          </div>
        </div>
        <div v-else class="security-items">
          <div class="security-items">
            <h3 :class="`font-second ${setting.danger ? 'danger' : ''}`">{{ setting.title }}</h3>
            <p :class="`font-second ${setting.danger ? 'danger' : ''}`">{{ setting.description }}</p>
          </div>
          <div class="security-items">
            <Button
              v-if="setting.title === 'Close account'"
              :label="'Show more'"
              :additional-class="`transparent mr`"
              @click-handler="stateShowCloseAccMoreInfo" />
            <Button
              :label="setting.buttonTitle"
              :additional-class="`transparent ${setting.danger ? 'danger' : ''}`"
              @click-handler="openModal(setting.title)" />
          </div>
        </div>
        <div v-if="closeAccountMoreInfo && setting.title === 'Close account'" class="font-second">
          <p>Closing your account means:</p>
          <ul>
            <li>Your username will be shown as user1234567890.</li>
            <li>All your personal information will be hidden from other users.</li>
            <li>You can restore your account any time just by signing in back.</li>
          </ul>
          <p>For more information see <span class="paragraph link" @click="redirect('tac')">terms and conditions</span>.</p>
        </div>
      </div>

      <basic-modal
        v-if="securityShowModal['Set 2FA']"
        header="Activate 2FA"
        description="We strongly recommend you to set up 2FA.
        This will increase the security of you account.
        Before it, you should download Google Authenticator application.
        Once it is done, click the button below to start."
        @close="closeModal('Set 2FA')"
      >
        <Button v-if="!securityTwoFa.qr && !([0, 1, 2].includes(securityTwoFa.status))" :label="'Generate 2FA'" :additional-class="'big w400'" @click-handler="generateTwoFa" />
        <div v-if="securityTwoFa.qr" class="center">
          <img :src="securityTwoFa.qr" alt="2fa">

          <p class="paragraph on-white-paragraph">In case if you are unable to scan this QR code, copy (click to copy) this key and paste it in Google Authenticator application as setup key.</p>
          <input id="secret" :value="`${securityTwoFa.secret}`" type="hidden" />
          <p class="paragraph link" @click="copy('secret')">{{ securityTwoFa.secret }}</p>

          <InputTwoFa :twofa="securityTwoFa.code" :onwhite="true" :disabled="securityTwoFa.status === 1" @returnTwoFa="returnTwoFa" />
          <Button :label="'Confirm 2FA code'" :additional-class="'big w400'" :disabled="securityTwoFa.disabledButton || securityTwoFa.status === 1" @click-handler="setTwoFa" />

          <p v-if="securityTwoFa.status === 1" class="paragraph success">2FA has been successfully set!</p>
          <p v-else-if="securityTwoFa.status === -1" class="paragraph error">Wrong code!</p>
        </div>
      </basic-modal>

      <basic-modal
        v-if="securityShowModal['Disable 2FA']"
        header="Disable 2FA"
        description="You are about deactivate your Two-factor authentication.
        Be careful! This action will decrease your account security"
        @close="closeModal('Disable 2FA')"
      >
        <div v-if="securityTwoFa.status === 2" class="center">
          <p class="paragraph on-white-paragraph">You have set up your 2FA, provide the code in input below, if you want to deactivate it.</p>

          <InputTwoFa :twofa="securityTwoFa.code" :onwhite="true" :disabled="securityTwoFa.disableStatus === 0" @returnTwoFa="returnTwoFa" />
          <Button :label="'Confirm 2FA disable'" :additional-class="'danger-fill big w400'" :disabled="securityTwoFa.disabledButton || securityTwoFa.disableStatus === 0" @click-handler="disableTwoFa" />

          <p v-if="securityTwoFa.disableStatus === 0" class="paragraph success">2FA has been successfully disabled!</p>
          <p v-else-if="securityTwoFa.disableStatus === -1" class="paragraph error">Wrong code!</p>
        </div>
      </basic-modal>

      <basic-modal
        v-if="securityShowModal['Change password']"
        header="Change password"
        description="Change your password by providing current password and new password.
        Be careful! After that, because of security reasons, you won't be able to change password for 48 hours."
        @close="closeModal('Change password')"
      >
        <Input
          v-model="securityPassword.currentPassword"
          :title="'Current password'"
          :title-class="'on-white-paragraph'"
          :additional-class="'on-white w400'"
          :type="'password'"
        />
        <Input
          v-model="securityPassword.newPassword"
          :title="'New password'"
          :title-class="'on-white-paragraph'"
          :additional-class="'on-white w400'"
          :type="'password'"
        />
        <Input
          v-model="securityPassword.newPasswordRepeat"
          :title="'Repeat new password'"
          :title-class="'on-white-paragraph'"
          :additional-class="'on-white w400'"
          :type="'password'"
        />
        <p v-if="securityPassword.error" class="paragraph error">Passwords have to match!</p>
        <Button
          :label="'Change password'"
          :additional-class="'big w400'"
          :disabled="!securityPassword.currentPassword || securityPassword.error || !securityPassword.newPassword || !securityPassword.newPasswordRepeat"
          @click-handler="changePassword"/>
      </basic-modal>

      <basic-modal
        v-if="securityShowModal['Change email']"
        header="Change email"
        description="Be careful! You are able to change email only one time."
        @close="closeModal('Change email')"
      >
      </basic-modal>

      <basic-modal
        v-if="securityShowModal['Close account']"
        header="Close account"
        description="We are very sorry about this :( You can get back any time you want. Hope, to see you again."
        @close="closeModal('Close account')"
      >
        <Input
          v-model="closeAcc.currentPassword"
          :title="'Current password'"
          :title-class="'on-white-paragraph'"
          :additional-class="'on-white w400'"
          :type="'password'"
        />
        <InputTwoFa v-if="securityTwoFa.status" :twofa="securityTwoFa.code" :onwhite="true" @returnTwoFa="returnTwoFa" />
        <Button :label="'Close account'" :additional-class="'danger-fill big w400'" :disabled="!closeAcc.currentPassword" @click-handler="closeAccount" />
        <p v-if="closeAcc.status === -2" class="paragraph error">Invalid 2FA!</p>
        <p v-else-if="closeAcc.status === -3" class="paragraph error">Invalid password!</p>
      </basic-modal>

    </div>

    <div v-else class="account-security-content">

    </div>

  </div>
</template>

<script>
import * as node2fa from 'node-2fa'
import Button from '~/components/Button'
import BasicModal from '~/components/BasicModal'
import InputTwoFa from '~/components/InputTwoFa'
import Input from '~/components/Input'
import Popup from '~/components/Popup'
import {
  disableTwoFa,
  getUserByToken,
  getUserSettings,
  setTwoFa,
  closeAccount,
  changePassword,
  changeEmail
} from '~/api'

export default {
  name: 'Settings',
  components: {
    Button,
    BasicModal,
    InputTwoFa,
    Input,
    Popup
  },
  data() {
    return {
      showPopup: false,
      closeAccountMoreInfo: false,

      accountHeaderItems: [
        { title: 'Personal information', active: true },
        { title: 'Security settings', active: false },
        { title: 'Site settings', active: false }
      ],
      currentSection: 'Personal information',
      userSettings: {},

      securitySettingsOptions: [
        {
          title: 'Set 2FA',
          description: 'Secure your account with Two-factor authentication (2FA).',
          buttonTitle: 'Set 2FA',
          danger: false
        },
        {
          title: 'Change password',
          description: 'Change your password by providing current password and new password.',
          buttonTitle: 'Change password',
          danger: false
        },
        {
          title: 'Change email',
          description: 'You are able to change email only one time.',
          buttonTitle: 'Change email',
          danger: false
        },
        {
          title: 'Close account',
          description: 'After closing account all information about it will be deleted.',
          buttonTitle: 'Close',
          danger: true
        }
      ],

      securityShowModal: {
        'Set 2FA': false,
        'Close account': false,
        'Change email': false,
        'Change password': false,
        'Disable 2FA': false,
        twoFa: false
      },

      securityTwoFa: {
        code: [],
        normalCode: null,
        qr: null,
        status: null,
        disableStatus: null,
        secret: null,
        disabledButton: true
      },
      securityPassword: { currentPassword: null, newPassword: null, newPasswordRepeat: null, status: null },
      closeAcc: { currentPassword: null, twoFa: null, status: null }
    }
  },
  watch: {
    'securityPassword.newPassword': {
      handler: function() {
        this.securityPassword.error = this.securityPassword.newPassword !== this.securityPassword.newPasswordRepeat
      }
    },
    'securityPassword.newPasswordRepeat': {
      handler: function() {
        this.securityPassword.error = this.securityPassword.newPassword !== this.securityPassword.newPasswordRepeat
      }
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

      if (this.userSettings.twoFa) {
        this.securityTwoFa.status = 2
      }
    },
    changeSubpage(item) {
      this.currentSection = item.title
      this.accountHeaderItems.forEach(header => {
        header.active = item.title === header.title
      })
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
      this.securityTwoFa.status = status
    },
    async disableTwoFa() {
      const { status } = await disableTwoFa({
        twoFaCode: this.securityTwoFa.normalCode,
        token: localStorage.getItem('token')
      })
      this.securityTwoFa.disableStatus = (status === 1 ? 0 : -1)
    },
    async closeAccount() {
      const { status } = await closeAccount({
        password: this.closeAcc.currentPassword,
        twoFa: this.closeAcc.twoFa,
        token: localStorage.getItem('token')
      })
      this.closeAcc.status = status
      this.closeAcc.currentPassword = null
      this.closeAcc.twoFa = null

      if (status === 1) {
        localStorage.removeItem('token')
        await this.$router.push('/')
      }
    },
    async changePassword() {
      const { status } = await changePassword({
        currentPassword: this.securityPassword.currentPassword,
        newPassword: this.securityPassword.newPassword
        // twoFa
      })
      this.securityPassword.status = status
    },
    async changeEmail() {
      await changeEmail({})
    },
    async generateTwoFa() {
      const user = await getUserByToken(localStorage.getItem('token'))
      if (user.status === -1) return

      const { qr, secret } = node2fa.generateSecret({ name: 'PNB - Pentesters Notes Blog', account: user.username })
      this.securityTwoFa.qr = qr
      this.securityTwoFa.secret = secret
    },
    copy(t) {
      const input = document.querySelector(`#${t}`)
      input.setAttribute('type', 'text')
      input.select()
      document.execCommand('copy')
      input.setAttribute('type', 'hidden')

      this.showPopup = true

      setTimeout(() => {
        this.showPopup = false
      }, 1500)
    },
    stateShowCloseAccMoreInfo() {
      this.closeAccountMoreInfo = !this.closeAccountMoreInfo
    },
    redirect(path) {
      this.$router.push(path)
    }
  }
}
</script>

<style lang="scss">
@import "../../../assets/css/edit";
</style>
