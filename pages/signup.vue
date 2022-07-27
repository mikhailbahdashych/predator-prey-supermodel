<template>
  <div>
    <Popup
      v-if="showPopup"
      :content="status === -1 ? 'User with this email already exists!' : 'User with this username already exists!'"
    />

    <div class="login">

      <div class="login-content">
        <div class="login-content__community-text">
          <h1 class="source-sans-pro bold">Welcome, @username, feel free to join pNb community</h1>
          <ul class="login-content__community-points">
            <li>Be in charge of everything that happens in world of cybersecurity</li>
            <li>Teach and learn - share you knowledge and learn from other</li>
            <li>Feel free to rise up any topic you are interested in on forum</li>
            <li>Anybody can ask - anybody can answer</li>
          </ul>
        </div>
      </div>

      <div v-if="step === 0" class="login-header">
        <h1 class="login-header__login-title" @click="redirect('/')">pNb</h1>
        <div class="login-header__login-header-btn">
          <p>Already have account?
            <span class="link" @click="redirect('/signin')">Sign in!</span>
          </p>
        </div>
      </div>

      <div v-if="step === 0" class="login-inputs">
        <div class="login-inputs__login-inputs-container">
          <h1 class="source-sans-pro bold">Sign up</h1>
          <Input
            v-model="email.email"
            :on-error="email.emailError"
            :disabled="disabledField"
            :title="'Email'"
            :type="'text'"
          />
          <Input
            v-model="username.username"
            :on-error="username.usernameError"
            :disabled="disabledField"
            :title="'Username'"
            :type="'text'"
          />
          <Input
            v-model="password.password"
            :on-error="passwordError.passwordMismatch || passwordError.passwordRequirement"
            :disabled="disabledField"
            :title="'Password'"
            :type="'password'"
          />
          <Input
            v-model="password.passwordRepeat"
            :on-error="passwordError.passwordMismatch || passwordError.passwordRequirement"
            :disabled="disabledField"
            :title="'Repeat password'"
            :type="'password'"
          />
          <p v-if="passwordError.passwordMismatch" class="error">Passwords have to match!</p>
          <p v-if="passwordError.passwordRequirement" class="error">Password are requirement!</p>

          <div v-if="passwordError.passwordRules" class="login-inputs__password-requirement">
            <div v-for="rule in passwordRulesList" :key="rule.text" class="login-inputs__password-requirements">
              <div v-for="(item, i) in Object.entries(rule)" :key="i">
                <p class="login-inputs__password-requirement-item">
                  <span v-if="item[0] === 'text'">{{ item[1] }}</span>
                  <span v-else>
                  <img v-if="item[1]" class="login-inputs__status" src="../assets/img/greencircle.svg" alt="OK" />
                  <img v-else class="login-inputs__status" src="../assets/img/redcircle.svg" alt="NOT OK" />
                </span>
                </p>
              </div>
            </div>
          </div>

          <div class="login-inputs__sign-in-btn">
            <Checkbox v-model="tac" :input-value="tac" :label="`I have read and accepted <a href='/'>terms and conditions.</a>`" />
            <Button
              :label="'Sign up'"
              :disabled="!validFields()"
              :btn-class="'basic-button--high-height'"
              @click-handler="signUpStepUp"
            />
          </div>
        </div>
      </div>

      <div v-if="step === 1" class="login-inputs login-inputs--personal-information">
        <div v-if="status !== 1" class="login-inputs__login-inputs-container login-inputs__login-inputs-container--personal-information">
          <h3 class="source-sans-pro bold">Tell us a little about yourself</h3>
          <p>Don't worry, you can skip this step and fill information you want later</p>
          <div class="flex">
            <Input
              v-model="personalInformation.first_name"
              :disabled="loading"
              :title="'First name'"
              :input-class="'bi--basic-input__small'"
            />
            <Input
              v-model="personalInformation.last_name"
              :disabled="loading"
              :title="'Last name'"
              :input-class="'bi--basic-input__small'"
            />
          </div>
          <p class="source-sans-pro bold">Provide your nickname or link</p>
          <hr>
          <Input
            v-model="personalInformation.twitter"
            :disabled="loading"
            :title="'Twitter'"
            :input-class="'bi--basic-input__small'"
          />
          <Input
            v-model="personalInformation.github"
            :disabled="loading"
            :title="'GitHub'"
            :input-class="'bi--basic-input__small'"
          />
          <Input
            v-model="personalInformation.website_link"
            :disabled="loading"
            :title="'Personal website'"
            :input-class="'bi--basic-input__small'"
          />
          <p class="source-sans-pro bold">What do you want to tell this world?</p>
          <hr>
          <Input
            v-model="personalInformation.user_status"
            :disabled="loading"
            :title="'Title (will be shown as status in your account)'"
            :input-class="'bi--basic-input__small'"
          />
          <Textarea
            v-model="personalInformation.about_me"
            :disabled="loading"
            :title="'Bio'"
          />
          <div class="login-inputs__buttons">
            <Checkbox
              v-model="personalInformation.show_email"
              :input-value="personalInformation.show_email"
              :disabled="loading"
              :label="`Show my email as public email for contact`"
            />
          </div>
          <div class="login-inputs__buttons">
            <Button
              :label="'Go back'"
              :btn-class="'basic-button--transparent'"
              :disabled="loading"
              @click-handler="signUpStepBack"
            />
            <div class='login-inputs__btn'>
              <Button
                :label="'Skip'"
                :btn-class="'basic-button--transparent'"
                :disabled="loading"
                @click-handler="signUpWithoutInfo"
              />
            </div>
            <Button
              :label="'Next'"
              :disabled="loading"
              @click-handler="signUpStepUp"
            />
          </div>
        </div>
        <div v-else class="login-inputs__login-inputs-container">
          <h1>Confirmation email has been sent.</h1>
          <p>Please, follow the instruction in the email to complete registration process.</p>
          <p>The link will be valid for 24 hours.</p>
          <Button
            :label="'Go to sign in'"
            :btn-class="'basic-button--transparent basic-button--high-height'"
            @click-handler="redirect('/signin')"
          />
        </div>
      </div>

      <div v-if="step === 2" class="login-inputs login-inputs--personal-information">
        <div v-if="status !== 1" class="login-inputs__login-inputs-container login-inputs__login-inputs-container--personal-information">
          <h3 class="source-sans-pro bold">All your location and place of work</h3>
          <p>Don't worry, you can skip this step and fill information you want later</p>
          <div class="flex">
            <Input
              v-model="personalInformation.location"
              :title="'Location'"
              :input-class="'bi--basic-input__small'"
            />
            <Input
              v-model="personalInformation.company"
              :title="'Company'"
              :input-class="'bi--basic-input__small'"
            />
          </div>
          <div class="login-inputs__buttons login-inputs__buttons--step">
            <Button
              :label="'Go back'"
              :btn-class="'basic-button--transparent'"
              @click-handler="signUpStepBack"
            />
            <div class='login-inputs__btn'>
              <Button
                :label="'Skip'"
                :btn-class="'basic-button--transparent'"
                @click-handler="signUpWithoutInfo"
              />
            </div>
            <Button
              :label="'Sign up'"
              @click-handler="signUpWithInfo"
            />
          </div>
        </div>
        <div v-else class="login-inputs__login-inputs-container">
          <h1>Confirmation email has been sent.</h1>
          <p>Please, follow the instruction in the email to complete registration process.</p>
          <p>The link will be valid for 24 hours.</p>
          <Button
            :label="'Go to sign in'"
            :btn-class="'basic-button--transparent basic-button--high-height'"
            @click-handler="redirect('/signin')"
          />
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import Popup from '~/components/basicComponents/Popup'
import Input from "~/components/basicComponents/Input";
import Button from "~/components/basicComponents/Button";
import Checkbox from "~/components/basicComponents/Checkbox";
import Textarea from "~/components/basicComponents/Textarea";
import { validateEmail, validatePassword, validatePasswordRules } from "~/helpers/frontValidator";
import { signUp } from "~/api";
export default {
  name: "Signup",
  components: {
    Popup,
    Input,
    Button,
    Checkbox,
    Textarea,
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
      step: 0,
      personalInformation: {
        first_name: null,
        last_name: null,
        user_status: null,
        about_me: null,
        website_link: null,
        twitter: null,
        github: null,
        show_email: false,
        company: null,
        location: null
      },
      disabledField: false,
      loading: true,
      showPopup: false,
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
      if (status === -1 || status === -2) {
        this.showPopup = true
        setTimeout(() => {
          this.showPopup = false
        }, 1500)
      }

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
      if (status === -1 || status === -2) {
        this.showPopup = true
        setTimeout(() => {
          this.showPopup = false
        }, 1500)
      }

      this.loading = false
    },
    signUpStepBack() {
      this.step -= 1
    },
    signUpStepUp() {
      this.step += 1
    }
  }
}
</script>

<style lang="scss">
@import '../assets/css/pages/signup';
</style>
