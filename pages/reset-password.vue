<template>
  <div class="login">

    <div class="login-content">
      <div class="login-content__center">
        <h1 class="source-sans-pro bold">Forgot your password?</h1>
        <h1 class="source-sans-pro bold">Nah... not a big deal</h1>
      </div>
    </div>

    <div class="login-header">
      <h1 class="login-header__login-title" @click="redirect('/')">pNb</h1>
      <div class="login-header__login-header-btn">
        <p>Don't have account yet?
          <span class="link" @click="redirect('/signup')">Sign up now!</span>
        </p>
      </div>
    </div>

    <div class="login-inputs">
      <div class="login-inputs__login-inputs-container">
        <h1 class="source-sans-pro bold">Forgot password?</h1>

        <div class="login-inputs__options">
          <p class="login-inputs__choose" @click="chooseOption('email')">With Email</p>
          <div class="login-inputs__vertical-line" />
          <p class="login-inputs__choose" @click="chooseOption('phone')">With Phone Number</p>
        </div>

        <InputWithButton
          v-model="resetPasswordEmail.email"
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
        <div class="login-inputs__sign-in-btn">
          <Button
            :label="'Submit'"
            :btn-class="'basic-button--high-height'"
            @click-handler="() => {}"
          />
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import InputWithButton from "~/components/basicComponents/InputWithButton";
import Button from "~/components/basicComponents/Button";
import Input from '~/components/basicComponents/Input'
import { validateEmail } from "~/helpers/frontValidator";
export default {
  name: "ResetPassword",
  components: {
    InputWithButton,
    Button,
    Input
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
