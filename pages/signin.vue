<template>
  <div class="login">

    <div class="login-content">
      <h1 class="login-title" @click="redirect('/')">pNb</h1>
    </div>

    <div class="login-header">
      <p class="paragraph right">Don't have account yet?
        <span class="paragraph link" @click="redirect('/signup')">Sign up now!</span>
      </p>
    </div>

    <div class="login-inputs">
      <div class="login-inputs-container" v-if="!phone.show && !twofa.show">
        <h1>Log In</h1>

        <div class="login-options">
          <p class="choose" @click="chooseLogin('email')">With Email</p>
          <div class="vertical-line" />
          <p class="choose" @click="chooseLogin('phone')">With Phone Number</p>
        </div>

        <Input
          :oneerror="loginEmail.loginEmailError"
          :style="[!loginEmail.loginWithEmail ? {'display': 'none'} : {'': ''}]"
          :focus="loginEmail.emailFocus"
          :title="'Email'"
          :type="'email'"
          v-model="loginEmail.email"
        />
        <Input
          :style="[loginEmail.loginWithEmail ? {'display': 'none'} : {'': ''}]"
          :focus="loginPhone.phoneFocus"
          :title="'Phone number'"
          :type="'email'"
          v-model="loginPhone.phone"
        />

        <Input @keyup.enter.native="signin" :oneerror="loginPassword.loginPasswordError" :title="'Password'" :type="'password'" v-model="loginPassword.password" />
        <p v-if="loginError === -1" class="paragraph error">Account doesn't exists or wasn't confirmed!</p>
        <Button :label="'Log In'" :clickon="signin" />
        <p class="paragraph right link" @click="redirect('reset-password')">Forgot password?</p>

      </div>

      <div class="login-inputs-container" v-else-if="twofa.show">
        <h1>Two-Factor authentication</h1>
        <div class="login-inputs-container-two-fa">
          <p class="paragraph">Please, provide Google Authenticator code to continue</p>
          <InputTwoFa :twofa="twofa.code" @returnTwofa="returnTwofa" />
          <p v-if="this.twofa.error" class="paragraph error">Wrong code!</p>
          <p class="paragraph right link">Unable to login with 2FA?</p>
        </div>
      </div>

      <div class="login-inputs-container" v-else-if="phone.show"></div>

    </div>

  </div>
</template>

<script>
import Input from "~/components/Input";
import Button from "~/components/Button";
import InputTwoFa from "~/components/InputTwoFa";
import {validateEmail, validatePasswordLength} from "~/helpers/frontValidator";
export default {
  name: "Signin",
  components: {
    Input,
    Button,
    InputTwoFa
  },
  watch: {
    'loginEmail.email': {
      handler: function () {
        this.loginEmail.loginEmailError = !validateEmail(this.loginEmail.email)
      }
    },
    'loginPassword.password': {
      handler: function () {
        this.loginPassword.loginPasswordError = !validatePasswordLength(this.loginPassword.password)
      }
    },
  },
  data() {
    return {
      loginEmail: {
        email: null,
        loginWithEmail: null,
        emailFocus: false,
        loginEmailError: false,
      },
      loginPassword: {
        loginPasswordError: false,
        password: null,
      },
      loginPhone: {
        phoneFocus: false,
        phone: null,
      },
      loginError: false,
      twofa: { code: [], show: false, error: false },
      phone: { phone: null, show: false, error: false }
    }
  },
  methods: {
    signin() {
      if (
        (this.loginEmail.email || this.loginPhone.phone) &&
        (!this.loginEmail.loginEmailError && !this.loginPassword.loginPasswordError)
      ) {
        //
      } else {
        this.loginEmail.loginEmailError = true
        this.loginPassword.loginPasswordError = true
      }
    },
    redirect(path) {
      this.$router.push({ path })
    },
    returnTwofa(twofa) {
      if (twofa.length !== 6 || twofa.join('').length !== 6) return
      this.signin()
    },
    chooseLogin(option) {
      if (option === 'email') this.setEmailFocusLogin()
      else this.setPhoneFocusLogin()
    },
    setEmailFocusLogin() {
      this.loginEmail = {
        email: null,
        loginWithEmail: true,
        emailFocus: true,
        loginEmailError: false,
      }
      this.loginPhone = {
        phoneFocus: false,
        phone: null,
      }
    },
    setPhoneFocusLogin() {
      this.loginEmail = {
        email: null,
        loginWithEmail: false,
        emailFocus: false,
        loginEmailError: false,
      }
      this.loginPhone = {
        phoneFocus: true,
        phone: null,
      }
    }
  }
}
</script>

<style lang="scss">
@import "../assets/css/signup";
</style>
