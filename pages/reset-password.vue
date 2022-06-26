<template>
  <div class="login">

    <div class="login-content">
      <h1 class="login-title" @click="redirect('/')">
        <span class="login-title-header">pNb</span>
      </h1>
    </div>

    <div class="login-header">
      <p class="paragraph right">Don't have account yet?
        <span class="paragraph link" @click="redirect('/signup')">Sign up now!</span>
      </p>
    </div>

    <div class="login-inputs">
      <div class="login-inputs-container">
        <h1>Forgot password?</h1>

        <div class="login-options">
          <p class="choose" @click="chooseOption('email')">Email</p>
          <div class="vertical-line" />
          <p class="choose" @click="chooseOption('phone')">Phone</p>
        </div>

        <InputWithButton
          :error="resetPasswordEmail.emailError"
          :button-click-on="() => {}"
          :title="'Email'"
          :focus="resetPasswordEmail.emailFocus"
          :button-title="'Send code'"
          :style="[!resetPasswordLoginWithEmail ? {'display': 'none'} : {'': ''}]"
          v-model="resetPasswordEmail.email"
        />
        <InputWithButton
          :button-click-on="() => {}"
          :title="'Phone'"
          :focus="resetPasswordPhone.phoneFocus"
          :button-title="'Send code'"
          :style="[resetPasswordLoginWithEmail ? {'display': 'none'} : {'': ''}]"
          v-model="resetPasswordPhone.phone"
        />

        <Input @keyup.enter.native="() => {}" :title="'Verification code'" />
        <Button :label="'Submit'" :clickon="() => {}" />
      </div>
    </div>

  </div>
</template>

<script>
import InputWithButton from "~/components/InputWithButton";
import Button from "~/components/Button";
import { validateEmail } from "~/helpers/frontValidator";
export default {
  name: "reset-password",
  components: {
    InputWithButton,
    Button
  },
  watch: {
    'resetPasswordEmail.email': {
      handler: function () {
        this.resetPasswordEmail.emailError = !validateEmail(this.resetPasswordEmail.email)
      }
    },
  },
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
      resetPasswordLoginWithEmail: false
    }
  },
  mounted() {
    this.chooseOption('email')
  },
  methods: {
    redirect(path) {
      this.$router.push({ path })
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
@import "../assets/css/signup";
</style>
