<template>
  <div>
    <div v-if="!showReopeningScreen.status" class="login">

      <div class="login-inputs">
        <div v-if="!phone.show && !twoFa.show" class="login-inputs-container">
          <h1 class="source-sans-pro bold">Sign In</h1>

          <div class="options">
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
          <p v-if="loginError" class="error">Wrong credentials!</p>
          <div class="sign-in-btn">
            <Button
              :label="'Sign In'"
              :disabled="loginEmail.loginEmailError || loginPassword.loginPasswordError || !loginPassword.password || !loginEmail.email"
              :additional-class="'high-height'"
              @click-handler="signin"
            />
            <p class="link" @click="redirect('reset-password')">Forgot password?</p>
          </div>

        </div>

        <div v-if="twoFa.show" class="login-inputs-container">
          <div class="two-fa">
            <h1>Two-Factor authentication</h1>
            <p class="paragraph">Please, provide Google Authenticator code to continue</p>
            <InputTwoFa :twofa="twoFa.code" @returnTwoFa="returnTwoFa" />
            <p v-if="twoFa.error" class="error">Wrong code!</p>
            <p class="paragraph link">Unable to login with 2FA?</p>
          </div>
        </div>

        <div v-else-if="phone.show" class="login-inputs-container"></div>

      </div>

      <div class="login-content">
        <h1 class="source-sans-pro bold">Welcome back, @username, glad to see you again</h1>
      </div>

      <div class="login-header">
        <div class="login-header-btn">
          <p class="paragraph">Don't have account yet?
            <span class="link" @click="redirect('/signup')">Sign up now!</span>
          </p>
        </div>
        <h1 class="login-title" @click="redirect('/')">pNb</h1>
      </div>

    </div>

    <div v-if="showReopeningScreen.status" class="reopening">
      <div class="reopening-block">
        <h1>There you are! Nice to see you again, {{ showReopeningScreen.username }}!</h1>
        <Button
          :label="'Here we go'"
          :additional-class="'big modal-size'"
          @click-handler="redirect(`/account/${personalId}`)"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Input from "~/components/basicComponents/Input";
import Button from "~/components/basicComponents/Button";
import InputTwoFa from "~/components/basicComponents/InputTwoFa";
import { validateEmail, validatePasswordLength } from "~/helpers/frontValidator";
import { verifyToken } from "~/helpers/crypto";
import { signIn } from "~/api";
export default {
  name: "Signin",
  components: {
    Input,
    Button,
    InputTwoFa
  },
  layout: 'empty',
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
      twoFa: { code: [], show: false, error: false, normalCode: null },
      phone: { phone: null, show: false, error: false },

      showReopeningScreen: { status: false, username: null },

      loading: true,
      personalId: null
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
  created() {
    this.$nextTick(() => { this.loading = false })
  },
  mounted() {
    this.chooseLogin('email')
  },
  methods: {
    async signin() {
      if (!this.loginEmail.loginEmailError && !this.loginPassword.loginPasswordError) {
        this.loading = true

        const payload = { email: this.loginEmail.email, password: this.loginPassword.password }
        if (this.loginPhone.phone) payload.phone = this.loginPhone.phone
        if (this.twoFa.normalCode) payload.twoFa = this.twoFa.normalCode

        const res = await signIn(payload)

        if (res.status === -1) {
          this.loginError = true
          this.loading = false
          return
        }
        if (res.status === -2) {
          this.twoFa.error = true
          this.loading = false
          return
        }

        if (res.twoFa)
          this.twoFa.show = true
        else if (res.phone)
          this.phone.show = true
        else if (!res.status) {
          sessionStorage.setItem('_at', res._at)
          this.loading = false
          const { personalId } = verifyToken(res._at)
          this.personalId = personalId

          if (res.reopening) {
            this.showReopeningScreen.status = true
            this.showReopeningScreen.username = res.reopening
            return
          }

          return this.$router.push(`/account/${this.personalId}`)
        }
        this.loading = false
      }
    },
    redirect(path) {
      return this.$router.push(path)
    },
    async returnTwoFa(twoFa) {
      if (twoFa.length !== 6 || twoFa.join('').length !== 6) return
      this.twoFa.normalCode = twoFa.join('')
      await this.signin()
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
@import "../assets/css/pages/signup";
</style>
