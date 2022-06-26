<template>
  <div class="login">

    <div class="login-content">
      <h1 class="login-title center" @click="redirect('/')">
        <span class="login-title-header">pNb</span>
      </h1>
      <div class="login-welcome-texts">
        <h2 class="center">Welcome, @username, feel free to join pNb community</h2>
        <ul class="login-community">
          <li>Be in charge of everything that happens in world of cybersecurity</li>
          <li>Teach and learn - share you knowledge and learn from other</li>
          <li>Feel free to rise up any topic you are interested in on forum</li>
          <li>Anybody can ask - anybody can answer</li>
        </ul>
      </div>
    </div>

    <div class="login-header">
      <p class="paragraph right">Already have account?
        <span class="paragraph link" @click="redirect('/signin')">Sign in!</span>
      </p>
    </div>

    <div class="login-inputs">
      <div v-if="status !== 1" class="login-inputs-container">
        <h1>Sign up</h1>
        <Input
          v-model="email.email"
          :oneerror="email.emailError"
          :title="'Email'"
          :type="'text'"
        />
        <Input
          v-model="password.password"
          :oneerror="passwordError.passwordMismatch || passwordError.passwordRequirement"
          :title="'Password'"
          :type="'password'"
        />
        <Input
          v-model="password.passwordRepeat"
          :oneerror="passwordError.passwordMismatch || passwordError.passwordRequirement"
          :title="'Repeat password'"
          :type="'password'"
        />
        <p v-if="passwordError.passwordMismatch" class="paragraph error">Passwords have to match!</p>
        <p v-if="passwordError.passwordRequirement" class="paragraph error">Password are requirement!</p>
        <div v-if="passwordError.passwordRules" class="password-requirement">

          <div v-for="rule in passwordRulesList" :key="rule.text" class="flex">
            <div v-for="(item, i) in Object.entries(rule)" :key="i">
              <p>
                <span v-if="item[0] === 'text'" class="paragraph">{{ item[1] }}</span>
                <span v-else>
                  <span v-if="item[1]" class="paragraph success">OK</span>
                  <span v-else class="paragraph error">NOT OK</span>
                </span>
              </p>
            </div>
          </div>
        </div>

        <Checkbox v-model="tac" :label="`I have read and accepted <a href='/'>terms and conditions.</a>`" />
        <p v-if="status === -1" class="paragraph error">User with this email already exists!</p>
        <Button :label="'Sign up'" :click-on="register" :disabled="!validFields()" :additional-class="'big'" />
      </div>
      <div v-else class="login-inputs-container">
        <h1>Confirmation email has been sent.</h1>
        <p class="paragraph medium">Please, follow the instruction in the email to complete registration process.</p>
        <p class="paragraph medium">The link will be valid for 24 hours.</p>
      </div>
    </div>

  </div>
</template>

<script>
import Input from "~/components/Input";
import Button from "~/components/Button";
import Checkbox from "~/components/Checkbox";
import {validateEmail, validatePassword, validatePasswordRules} from "~/helpers/frontValidator";
import {signUp} from "~/api";
export default {
  name: "Signup",
  components: {
    Input,
    Button,
    Checkbox
  },
  data() {
    return {
      email: {
        email: null,
        emailError: false,
      },

      password: {
        password: null,
        passwordRepeat: null,
      },

      status: null,
      tac: false,
      error: false,

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
      ]
    }
  },
  watch: {
    'password.password': {
      handler: function () {
        if (this.password.password === this.password.passwordRepeat) { this.passwordError.passwordMismatch = false }
        this.validPassword()
      }
    },
    'password.passwordRepeat': {
      handler: function () {
        if (this.password.password === this.password.passwordRepeat) { this.passwordError.passwordMismatch = false }
        this.validPassword()
      }
    },
    'email.email': {
      handler: function () {
        if (!validateEmail(this.email.email)) this.email.emailError = true
        else if (validateEmail(this.email.email) === 1) this.email.emailError = false
        else this.email.emailError = false
      }
    },
  },
  methods: {
    async redirect(path) {
      await this.$router.push({ path })
    },
    validFields() {
      return this.tac &&
        !this.email.emailError &&
        this.email.email && this.password.password && this.password.passwordRepeat &&
        (!this.passwordError.passwordMismatch && !this.passwordError.passwordRequirement && !this.passwordError.passwordRules)
    },
    validPassword() {
      const passwordRuleCheck = validatePasswordRules(this.password.password)
      Object.entries(passwordRuleCheck).forEach(item => {
        this.passwordRulesList.forEach(rule => {
          Object.entries(rule).forEach(x => {
            if (item[0] === x[0]) rule[item[0]] = item[1]
          })
        })
      })
      this.passwordError.passwordMismatch = !!((this.password.password && this.password.passwordRepeat) && (this.password.password !== this.password.passwordRepeat));
      this.passwordError.passwordRequirement = !this.password.password || !this.password.passwordRepeat;
      this.passwordError.passwordRules = !!(!validatePassword(this.password.password) || !validatePassword(this.password.passwordRepeat));
      if (!this.password.password && !this.password.passwordRepeat) {
        this.passwordError.passwordMismatch = false
        this.passwordError.passwordRequirement = false
        this.passwordError.passwordRules = false
      }
    },
    async register() {
      if (this.validFields()) {
        await signUp({
          email: this.email.email,
          password: this.password.password,
        }).then((res) => {
          if (res.status === -1) this.status = res.status
        }).catch(() => {
          this.status = -1
        })
      }
    }
  }
}
</script>

<style lang="scss">
@import '../assets/css/signup';
</style>
