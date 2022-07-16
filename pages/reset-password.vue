<template>
  <div class="login">

    <div class="login-content">
      <h1 class="login-title center" @click="redirect('/')">
        <span class="login-title-header">pNb</span>
      </h1>
      <div class="login-welcome-texts">
        <h1 class="center">Forgot your password? Nah... not a big deal</h1>
      </div>
    </div>

    <div class="login-header">
      <p class="paragraph account-having right">Don't have account yet?
        <span class="paragraph link" @click="redirect('/signup')">Sign up now!</span>
      </p>
    </div>

    <div class="login-inputs">
      <div class="login-inputs-container">
        <h1>Forgot password?</h1>

        <div class="flex">
          <p class="choose" @click="chooseOption('email')">Email</p>
          <div class="vertical-line" />
          <p class="choose" @click="chooseOption('phone')">Phone</p>
        </div>

        <InputWithButton
          v-model="resetPasswordEmail.email"
          :error="resetPasswordEmail.emailError"
          :button-click-on="() => {}"
          :title="'Email'"
          :focus="resetPasswordEmail.emailFocus"
          :button-title="'Send code'"
          :style="[!resetPasswordLoginWithEmail ? {'display': 'none'} : {'': ''}]"
        />
        <InputWithButton
          v-model="resetPasswordPhone.phone"
          :button-click-on="() => {}"
          :title="'Phone'"
          :focus="resetPasswordPhone.phoneFocus"
          :button-title="'Send code'"
          :style="[resetPasswordLoginWithEmail ? {'display': 'none'} : {'': ''}]"
        />

        <Input :title="'Verification code'" @keyup.enter.native="() => {}" />
        <Button :label="'Submit'" :additional-class="'mt high-height'" @click-handler="() => {}" />
      </div>
    </div>

  </div>
</template>

<script>
import InputWithButton from "~/components/basicComponents/InputWithButton";
import Button from "~/components/basicComponents/Button";
import { validateEmail } from "~/helpers/frontValidator";
export default {
  name: "ResetPassword",
  components: {
    InputWithButton,
    Button
  },
  layout: 'empty',
  data() {
    return {
      resetPasswordEmail: {
        email: null,
        emailError: false,
        emailFocus: false,
      },

      resetPasswordPhone: {
        phone: null,
        phoneFocus: false,
      },

      resetPasswordCode: null,
      resetPasswordLoginWithEmail: false,

      loading: true
    }
  },
  watch: {
    'resetPasswordEmail.email': {
      handler: function () {
        this.resetPasswordEmail.emailError = !validateEmail(this.resetPasswordEmail.email)
      }
    },
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
  mounted() {
    this.chooseOption('email')
  },
  methods: {
    redirect(path) {
      this.$router.push(path)
    },
    chooseOption(option) {
      if (option === 'email') this.setResetPasswordEmailFocusLogin()
      else this.setResetPasswordPhoneFocusLogin()
    },
    setResetPasswordEmailFocusLogin() {
      this.resetPasswordLoginWithEmail = true
      this.resetPasswordEmail = {
        email: null,
        emailError: false,
        emailFocus: true
      }
      this.resetPasswordPhone = {
        phone: null,
        phoneFocus: false,
      }
    },
    setResetPasswordPhoneFocusLogin() {
      this.resetPasswordLoginWithEmail = false
      this.resetPasswordEmail = {
        email: null,
        emailError: false,
        emailFocus: false
      }
      this.resetPasswordPhone = {
        phone: null,
        phoneFocus: true,
      }
    }
  }
}
</script>

<style lang="scss">
@import "../assets/css/pages/signup";
</style>
