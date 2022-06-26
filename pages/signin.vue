<template>
  <div class="login">

    <div class="login-inputs">
      <div v-if="!phone.show && !twofa.show" class="login-inputs-container">
        <h1>Sign In</h1>

        <div class="login-options">
          <p class="choose" @click="chooseLogin('email')">With Email</p>
          <div class="vertical-line" />
          <p class="choose" @click="chooseLogin('phone')">With Phone Number</p>
        </div>

        <Input
          v-model="loginEmail.email"
          :oneerror="loginEmail.loginEmailError"
          :style="[!loginEmail.loginWithEmail ? {'display': 'none'} : {'': ''}]"
          :focus="loginEmail.emailFocus"
          :title="'Email'"
          :type="'email'"
        />
        <Input
          v-model="loginPhone.phone"
          :style="[loginEmail.loginWithEmail ? {'display': 'none'} : {'': ''}]"
          :focus="loginPhone.phoneFocus"
          :title="'Phone number'"
          :type="'email'"
        />

        <Input
          v-model="loginPassword.password"
          :oneerror="loginPassword.loginPasswordError"
          :title="'Password'"
          :type="'password'"
          @keyup.enter.native="signin"
        />
        <p v-if="loginError === -1" class="paragraph error">Account doesn't exists or wasn't confirmed!</p>
        <Button :label="'Sign In'" :clickon="signin" :additional-class="'big'" />
        <p class="paragraph right link" @click="redirect('reset-password')">Forgot password?</p>

      </div>

      <div v-else-if="twofa.show" class="login-inputs-container">
        <h1>Two-Factor authentication</h1>
        <div class="center">
          <p class="paragraph">Please, provide Google Authenticator code to continue</p>
          <InputTwoFa :twofa="twofa.code" @returnTwofa="returnTwofa" />
          <p v-if="twofa.error" class="paragraph error">Wrong code!</p>
          <p class="paragraph right link">Unable to login with 2FA?</p>
        </div>
      </div>

      <div v-else-if="phone.show" class="login-inputs-container"></div>

    </div>

    <div class="login-content">
      <h1 class="login-title center" @click="redirect('/')">
        <span class="login-title-header">pNb</span>
      </h1>
    </div>

    <div class="login-header">
      <p class="paragraph left">Don't have account yet?
        <span class="paragraph link" @click="redirect('/signup')">Sign up now!</span>
      </p>
    </div>

  </div>
</template>

<script>
import Input from "~/components/Input";
import Button from "~/components/Button";
import InputTwoFa from "~/components/InputTwoFa";
import {validateEmail, validatePasswordLength} from "~/helpers/frontValidator";
import {signIn} from "~/api";
export default {
  name: "Signin",
  components: {
    Input,
    Button,
    InputTwoFa
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
  methods: {
    async signin() {
      if (
        (this.loginEmail.email || this.loginPhone.phone) &&
        (!this.loginEmail.loginEmailError && !this.loginPassword.loginPasswordError)
      ) {
        const res = await signIn({
          email: this.loginEmail.email,
          phone: this.loginPhone.phone,
          password: this.loginPassword.password,
          twofa: this.twofa.code.join('')
        })

        if (res.status === -1) {
          this.loginError = -1
          return
        }

        if (res.twofa) {
          this.twofa.show = true
        } else if (res.phone) {
          this.phone.show = true
        } else if (!res.status) {
          localStorage.setItem('token', res)
          localStorage.setItem('email', this.loginEmail.email)
          await this.$router.push({path: '/account'})
        } else if (this.twofa.code) {
          this.twofa.error = true
        } else {
          this.phone.error = true
        }
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
