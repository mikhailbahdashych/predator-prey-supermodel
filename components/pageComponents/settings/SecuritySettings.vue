<template>
  <div>
    <Popup v-if="showPopup" :content="'Copied!'" />
    <div class="account-security-content">
      <div v-for="setting in securitySettingsOptions" :key="setting.title" :class="`security-item ${setting.danger ? 'danger' : ''}`">
        <div v-if="setting.title === 'Set 2FA'" class="security-items">
          <div class="security-items texts">
            <h3 class="font-second">{{ securityTwoFa.status === 2 ? 'Disable 2FA' : setting.title }}</h3>
            <p class="font-second">{{ securityTwoFa.status === 2 ? 'You have set up Two-factor authentication (2FA) for your account.' : setting.description}}</p>
          </div>
          <div class="security-items">
            <Button
              :label="securityTwoFa.status === 2 ? 'Disable 2FA' : setting.buttonTitle"
              :additional-class="`transparent min-width150`"
              @click-handler="openModal(securityTwoFa.status === 2 ? 'Disable 2FA' : setting.title)" />
          </div>
        </div>
        <div v-else class="security-items">
          <div class="security-items texts">
            <h3 :class="`font-second ${setting.danger ? 'danger' : ''}`">{{ setting.title }}</h3>
            <p :class="`font-second ${setting.danger ? 'danger' : ''}`">{{ setting.description }}</p>
            <p v-if="setting.title === 'Close account'" class="paragraph link" @click="stateShowCloseAccMoreInfo">
              {{ !closeAccountMoreInfo ? 'Show more' : 'Show less' }}
            </p>
          </div>
          <div class="security-items">
            <Button
              :label="setting.buttonTitle"
              :additional-class="`transparent min-width150 ${setting.danger ? 'danger' : ''}`"
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
          :oneerror="securityPassword.currentPasswordLength"
          :title="'Current password'"
          :title-class="'on-white-paragraph'"
          :additional-class="'on-white w400'"
          :type="'password'"
        />
        <Input
          v-model="securityPassword.newPassword"
          :oneerror="passwordError.passwordMismatch || passwordError.passwordRequirement"
          :title="'New password'"
          :title-class="'on-white-paragraph'"
          :additional-class="'on-white w400'"
          :type="'password'"
        />
        <Input
          v-model="securityPassword.newPasswordRepeat"
          :oneerror="passwordError.passwordMismatch || passwordError.passwordRequirement"
          :title="'Repeat new password'"
          :title-class="'on-white-paragraph'"
          :additional-class="'on-white w400'"
          :type="'password'"
        />

        <p v-if="securityPassword.status === 1" class="paragraph success">Password has been successfully changed!</p>
        <p v-else-if="securityPassword.status === -2" class="paragraph error">Wrong password!</p>
        <p v-else-if="securityPassword.status === -3" class="paragraph error">Wrong 2FA code!</p>
        <p v-else-if="securityPassword.status === -4" class="paragraph error">New password can't be the same as current one!</p>

        <p v-if="passwordError.passwordMismatch" class="paragraph error">Passwords have to match!</p>
        <p v-else-if="passwordError.passwordRequirement" class="paragraph error">Password are requirement!</p>

        <div v-if="passwordError.passwordRules">

          <div v-for="rule in passwordRulesList" :key="rule.text" class="password-requirement-list">
            <div v-for="(item, i) in Object.entries(rule)" :key="i">
              <p class="password-requirement-list-item">
                <span v-if="item[0] === 'text'" class="paragraph on-white-paragraph">{{ item[1] }}</span>
                <span v-else>
                  <img v-if="item[1]" class="status" src="../../../assets/img/redcircle.svg" alt="NOT OK" />
                  <img v-else class="status" src="../../../assets/img/greencircle.svg" alt="OK" />
                </span>
              </p>
            </div>
          </div>
        </div>
        <Button
          :label="'Change password'"
          :additional-class="'big w400'"
          :disabled="
           !securityPassword.currentPassword ||
           passwordError.passwordMismatch ||
           passwordError.passwordRequirement ||
           securityPassword.error ||
           !securityPassword.newPassword ||
           !securityPassword.newPasswordRepeat"
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
        <Button :label="'Close account'" :additional-class="'danger-fill big w400'" :disabled="!closeAcc.currentPassword" @click-handler="closeAccount" />
        <p v-if="closeAcc.status === -2" class="paragraph error">Wrong 2FA code!</p>
        <p v-else-if="closeAcc.status === -3" class="paragraph error">Invalid password!</p>
      </basic-modal>
    </div>

    <basic-modal
      v-if="confirmActionTwoFa.show"
      header="Confirm action"
      description="Confirm action by providing 2FA code in the box below."
      @close="closeConfirmTwoFa"
    >
      <InputTwoFa :twofa="securityTwoFa.code" :onwhite="true" @returnTwoFa="returnTwoFaConfirmAction" />
      <Button :label="'Confirm action'" :additional-class="'danger-fill big w400'" @click-handler="confirmAction" />
    </basic-modal>

  </div>
</template>

<script>
import * as node2fa from 'node-2fa'
import Button from '~/components/Button'
import BasicModal from '~/components/BasicModal'
import InputTwoFa from '~/components/InputTwoFa'
import Input from '~/components/Input'
import Popup from '~/components/Popup'
import { validatePassword, validatePasswordLength, validatePasswordRules } from '~/helpers/frontValidator'
import {
  changeEmail,
  changePassword,
  closeAccount,
  disableTwoFa,
  getUserByToken,
  getUserSettings,
  setTwoFa
} from '~/api'
export default {
  name: 'SecuritySettings',
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

      closeAcc: { currentPassword: null, status: null },

      securityPassword: {
        currentPasswordLength: null,
        currentPassword: null,
        newPassword: null,
        newPasswordRepeat: null,
        status: null
      },
      passwordError: {
        passwordMismatch: false,
        passwordRequirement: false,
        passwordRules: false
      },
      passwordRulesList: [
        {eightChars: false, text: 'Password length should be more than 8 characters'},
        {uppCase: false, text: 'Password should contain at least one uppercase character'},
        {lowCase: false, text: 'Password should contain at least one lowercase character'},
        {specChar: false, text: 'Password should contain at least one special character'},
        {digitChar: false, text: 'Password should contain at least one digit character'}
      ],

      changeEmailData: {
        newEmail: null,
        status: null
      },

      confirmActionTwoFa: {
        show: false,
        code: [],
        normalCode: null,
        action: null
      },

      userSettings: {}
    }
  },
  watch: {
    'securityPassword.currentPassword': {
      handler: function () {
        this.securityPassword.currentPasswordLength = !validatePasswordLength(this.securityPassword.currentPassword)
      }
    },
    'securityPassword.newPassword': {
      handler: function() {
        if (this.securityPassword.newPassword === this.securityPassword.newPasswordRepeat) { this.passwordError.passwordMismatch = false }
        this.validPassword()
      }
    },
    'securityPassword.newPasswordRepeat': {
      handler: function() {
        if (this.securityPassword.newPassword === this.securityPassword.newPasswordRepeat) { this.passwordError.passwordMismatch = false }
        this.validPassword()
      }
    }
  },
  async mounted() {
    if (localStorage.getItem('token') !== null) await this.getUsersSettings(localStorage.getItem('token'))
    else await this.$router.push('/')
  },
  methods: {
    async getUsersSettings(token) {
      this.userSettings = await getUserSettings(token, 's')
      if (this.userSettings.status === -1)
        return this.$router.push('/')

      if (this.userSettings.twoFa) {
        this.securityTwoFa.status = 2
      }
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
    returnTwoFaConfirmAction(twoFa) {
      if (twoFa.length !== 6 || twoFa.join('').length !== 6) return
      this.confirmActionTwoFa.normalCode = twoFa.join('')
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
      if (this.userSettings.twoFa && !this.confirmActionTwoFa.normalCode) {
        this.confirmActionTwoFa.show = true
        this.confirmActionTwoFa.action = 'closeAccount'
      } else {
        const { status } = await closeAccount({
          password: this.closeAcc.currentPassword,
          twoFa: this.confirmActionTwoFa.normalCode,
          token: localStorage.getItem('token')
        })
        this.closeAcc.status = status
        this.closeAcc.currentPassword = null

        if (status === 1) {
          localStorage.removeItem('token')
          await this.$router.push('/')
        }
      }
    },
    async changePassword() {
      if (this.userSettings.twoFa && !this.confirmActionTwoFa.normalCode) {
        this.confirmActionTwoFa.show = true
        this.confirmActionTwoFa.action = 'changePassword'
      } else {
        const { status } = await changePassword({
          token: localStorage.getItem('token'),
          currentPassword: this.securityPassword.currentPassword,
          newPassword: this.securityPassword.newPassword,
          newPasswordRepeat: this.securityPassword.newPasswordRepeat,
          twoFa: this.confirmActionTwoFa.normalCode
        })
        this.securityPassword.status = status
      }
    },
    async changeEmail() {
      if (this.userSettings.twoFa && !this.confirmActionTwoFa.normalCode) {
        this.confirmActionTwoFa.show = true
        this.confirmActionTwoFa.action = 'changeEmail'
      } else {
        const { status } = await changeEmail({
          token: localStorage.getItem('token'),
          twoFa: this.confirmActionTwoFa.normalCode,
          newEmail: this.changeEmailData.newEmail
        })
        this.changeEmailData.status = status
      }
    },
    async generateTwoFa() {
      const user = await getUserByToken(localStorage.getItem('token'))
      if (user.status === -1) return

      const { qr, secret } = node2fa.generateSecret({ name: 'PNB - Pentesters Notes Blog', account: user.username })
      this.securityTwoFa.qr = qr
      this.securityTwoFa.secret = secret
    },
    async confirmAction() {
      switch (this.confirmActionTwoFa.action) {
        case 'closeAccount':
          await this.closeAccount()
          break;
        case 'changePassword':
          await this.changePassword()
          break;
        case 'changeEmail':
          await this.changeEmail()
          break;
      }
      this.confirmActionTwoFa.show = false
      this.confirmActionTwoFa.normalCode = null
    },
    closeConfirmTwoFa() {
      this.confirmActionTwoFa = {
        show: false,
        code: [],
        normalCode: null,
        action: null
      }
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
    redirect(path) {
      this.$router.push(path)
    },
    validPassword() {
      const passwordRuleCheck = validatePasswordRules(this.securityPassword.newPassword)
      Object.entries(passwordRuleCheck).forEach(item => {
        this.passwordRulesList.forEach(rule => {
          Object.entries(rule).forEach(x => {
            if (item[0] === x[0]) rule[item[0]] = item[1]
          })
        })
      })
      this.passwordError.passwordMismatch = !!((this.securityPassword.newPassword && this.securityPassword.newPasswordRepeat) && (this.securityPassword.newPassword !== this.securityPassword.newPasswordRepeat));
      this.passwordError.passwordRequirement = !this.securityPassword.newPassword || !this.securityPassword.newPasswordRepeat;
      this.passwordError.passwordRules = !!(!validatePassword(this.securityPassword.newPassword) || !validatePassword(this.securityPassword.newPasswordRepeat));
      if (!this.securityPassword.newPassword && !this.securityPassword.newPasswordRepeat) {
        this.passwordError.passwordMismatch = false
        this.passwordError.passwordRequirement = false
        this.passwordError.passwordRules = false
      }
    },
    stateShowCloseAccMoreInfo() {
      this.closeAccountMoreInfo = !this.closeAccountMoreInfo
    }
  }
}
</script>

<style lang="scss">
@import "../../../assets/css/edit";
</style>
