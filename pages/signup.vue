<template>
  <div class="login">

    <div class="login-content">
      <h1 class="login-title center" @click="redirect('/')">
        <span class="login-title-header">pNb</span>
      </h1>
      <div class="login-welcome-texts">
        <h1 class="center">Welcome, @username, feel free to join pNb community</h1>
        <ul class="login-community">
          <li>Be in charge of everything that happens in world of cybersecurity</li>
          <li>Teach and learn - share you knowledge and learn from other</li>
          <li>Feel free to rise up any topic you are interested in on forum</li>
          <li>Anybody can ask - anybody can answer</li>
        </ul>
      </div>
    </div>

    <div v-if="!showPersonalInformationFields" class="login-header">
      <p class="paragraph right account-having">Already have account?
        <span class="paragraph link" @click="redirect('/signin')">Sign in!</span>
      </p>
    </div>

    <div v-if="!showPersonalInformationFields" class="login-inputs">
      <div class="login-inputs-container">
        <h1>Sign up</h1>
        <Input
          v-model="email.email"
          :oneerror="email.emailError"
          :disabled="disabledField"
          :title="'Email'"
          :type="'text'"
        />
        <Input
          v-model="username.username"
          :oneerror="username.usernameError"
          :disabled="disabledField"
          :title="'Username'"
          :type="'text'"
        />
        <Input
          v-model="password.password"
          :oneerror="passwordError.passwordMismatch || passwordError.passwordRequirement"
          :disabled="disabledField"
          :title="'Password'"
          :type="'password'"
        />
        <Input
          v-model="password.passwordRepeat"
          :oneerror="passwordError.passwordMismatch || passwordError.passwordRequirement"
          :disabled="disabledField"
          :title="'Repeat password'"
          :type="'password'"
        />
        <p v-if="passwordError.passwordMismatch" class="paragraph error">Passwords have to match!</p>
        <p v-if="passwordError.passwordRequirement" class="paragraph error">Password are requirement!</p>
        <div v-if="passwordError.passwordRules" class="password-requirement">

          <div v-for="rule in passwordRulesList" :key="rule.text" class="flex">
            <div v-for="(item, i) in Object.entries(rule)" :key="i">
              <p class="password-requirement-item">
                <span v-if="item[0] === 'text'" class="paragraph">{{ item[1] }}</span>
                <span v-else>
                  <img v-if="item[1]" class="status" src="../assets/img/greencircle.svg" alt="OK" />
                  <img v-else class="status" src="../assets/img/redcircle.svg" alt="NOT OK" />
                </span>
              </p>
            </div>
          </div>
        </div>

        <Checkbox v-model="tac" :input-value="tac" :label="`I have read and accepted <a href='/'>terms and conditions.</a>`" />
        <Button :label="'Sign up'" :disabled="!validFields()" :additional-class="'high-height'" @click-handler="showPersonalInfoFields" />
      </div>
    </div>

    <div v-if="showPersonalInformationFields" class="login-inputs personal-information">
      <div v-if="status !== 1" class="login-inputs-container personal-information">
        <h3>Tell us a little about yourself</h3>
        <p>Don't worry, you can skip this step and fill information you want later</p>
        <hr>
        <div class="flex">
          <Input
            v-model="personalInformation.first_name"
            :disabled="loading"
            :title="'First name'"
            :title-class="'small'"
            :additional-class="'small mrl'"
          />
          <Input
            v-model="personalInformation.last_name"
            :disabled="loading"
            :title="'Last name'"
            :title-class="'small'"
            :additional-class="'small'"
          />
        </div>
        <p>Provide your nickname or link</p>
        <hr>
        <Input
          v-model="personalInformation.twitter"
          :disabled="loading"
          :title="'Twitter'"
          :title-class="'small'"
          :additional-class="'small'"
        />
        <Input
          v-model="personalInformation.github"
          :disabled="loading"
          :title="'GitHub'"
          :title-class="'small'"
          :additional-class="'small'"
        />
        <Input
          v-model="personalInformation.website_link"
          :disabled="loading"
          :title="'Personal website'"
          :title-class="'small'"
          :additional-class="'small'"
        />
        <p>What do you want to tell this world?</p>
        <hr>
        <Input
          v-model="personalInformation.title"
          :disabled="loading"
          :title="'Title (will be shown as status in your account)'"
          :title-class="'small'"
          :additional-class="'small'"
        />
        <Textarea
          v-model="personalInformation.about_me"
          :disabled="loading"
          :title="'Bio'"
        />
        <Checkbox
          v-model="personalInformation.show_email"
          :input-value="personalInformation.show_email"
          :disabled="loading"
          :label="`Show my email as public email for contact`"
        />
        <div class="flex">
          <Button
            :label="'Go back'"
            :additional-class="'mt transparent mrl'"
            :disabled="loading"
            @click-handler="signUpStepBack"
          />
          <Button
            :label="'Skip'"
            :additional-class="'mt transparent mrl'"
            :disabled="loading"
            @click-handler="signUpWithoutInfo"
          />
          <Button
            :label="'Sign up'"
            :additional-class="'mt mrl'"
            :disabled="loading"
            @click-handler="signUpWithInfo"
          />
        </div>
        <p v-if="status === -1" class="paragraph error">User with this email already exists!</p>
        <p v-else-if="status === -2" class="paragraph error">User with this username already exists!</p>
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
import Textarea from "~/components/Textarea";
import { validateEmail, validatePassword, validatePasswordRules } from "~/helpers/frontValidator";
import { signUp } from "~/api";
import { verifyUserByToken } from "~/helpers/auth";
export default {
  name: "Signup",
  components: {
    Input,
    Button,
    Checkbox,
    Textarea
  },
  layout: 'empty',
  data() {
    return {
      username: {
        username: null,
        usernameError: false
      },

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
      ],

      showPersonalInformationFields: false,
      personalInformation: {
        first_name: null,
        last_name: null,
        title: null,
        about_me: null,
        website_link: null,
        twitter: null,
        github: null,
        show_email: false
      },

      disabledField: false,

      loading: true
    }
  },
  watch: {
    'password.password': {
      handler: function () {
        if (this.password.password === this.password.passwordRepeat)
          this.passwordError.passwordMismatch = false
        this.validPassword()
      }
    },
    'password.passwordRepeat': {
      handler: function () {
        if (this.password.password === this.password.passwordRepeat)
          this.passwordError.passwordMismatch = false
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
    'username.username': {
      handler: function () {
        this.username.usernameError = !this.username.username;
      }
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
  async mounted() {
    await verifyUserByToken(this.$router, sessionStorage.getItem('accessToken'), true)
  },
  methods: {
    redirect(path) {
      return this.$router.push(path)
    },
    validFields() {
      return this.tac &&
        !this.email.emailError &&
        this.email.email && this.password.password && this.password.passwordRepeat && this.username.username &&
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
    async signUpWithInfo() {
      this.loading = true

      const { status } = await signUp({
        email: this.email.email,
        password: this.password.password,
        username: this.username.username,
        personalInformation: this.personalInformation
      })

      if (status) this.status = status
      if (status === 1) this.disabledField = true

      this.loading = false
    },
    async signUpWithoutInfo() {
      this.loading = true

      const { status } = await signUp({
        email: this.email.email,
        password: this.password.password,
        username: this.username.username
      })

      if (status) this.status = status
      if (status === 1) this.disabledField = true

      this.loading = false
    },
    signUpStepBack() {
      this.showPersonalInformationFields = false
    },
    showPersonalInfoFields() {
      if (this.validFields()) {
        this.showPersonalInformationFields = true
      }
    }
  }
}
</script>

<style lang="scss">
@import '../assets/css/signup';
</style>
