<template>
  <div class="account-preferences">
    <Popup v-if="showPopup" :content="'Personal settings has been successfully updated!'" />

    <h1 class="account-preferences__header">Public profile</h1>
    <hr>
    <div class="account-preferences__fields-wrap">
      <div class="account-preferences__fields">
        <p class="account-preferences__subtitle">Personal information</p>
        <hr>
        <Input
          v-model="personalInformation.first_name"
          :title="'First name'"
          :input-class="'bi--basic-input__small'"
        />
        <Input
          v-model="personalInformation.last_name"
          :title="'Last name'"
          :input-class="'bi--basic-input__small'"
        />
        <Input
          v-model="personalInformation.user_status"
          :title="'Status'"
          :input-class="'bi--basic-input__small'"
        />
        <div class="account-preferences__annotation">
          <span class="source-sans-pro opacity">
            Your first and last name will be shown only in your profile.
            You can remove it anu time you want.
          </span>
        </div>
        <Input
          v-model="personalInformation.company"
          :title="'Company'"
          :input-class="'bi--basic-input__small'"
        />
        <Input
          v-model="personalInformation.location"
          :title="'Location'"
          :input-class="'bi--basic-input__small'"
        />
        <Textarea
          v-model="personalInformation.about_me"
          :title="'About'"
        />
        <div class="account-preferences__annotation">
          <span class="source-sans-pro opacity">You can
            <span class="source-sans-pro bold">@mention</span>
            your company’s PNB organization to link it.</span>
        </div>
        <p class="account-preferences__subtitle">Social media</p>
        <hr>
        <Input
          v-model="personalInformation.website_link"
          :title="'Website'"
          :input-class="'bi--basic-input__small'"
        />
        <Input
          v-model="personalInformation.twitter"
          :title="'Twitter'"
          :input-class="'bi--basic-input__small'"
        />
        <Input
          v-model="personalInformation.github"
          :title="'GitHub'"
          :input-class="'bi--basic-input__small'"
        />
        <div class="account-preferences__button">
          <Checkbox
            v-model="personalInformation.show_email"
            :label="`Show my email as public email for contact`"
          />
          <Button :label="'Save settings'" @click-handler="updatePersonalInfo" />
        </div>
      </div>

      <div class="account-preferences__profile-picture">
        <div class="account-preferences__box">
          <img class="account-preferences__picture" :src="require('../../../assets/img/testava.jpg')" alt="ava">
          <div class="account-preferences__picture-button">
            <Button :label="'Change avatar'" />
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import Input from "~/components/basicComponents/Input";
import Textarea from "~/components/basicComponents/Textarea";
import Checkbox from "~/components/basicComponents/Checkbox";
import Button from "~/components/basicComponents/Button";
import Popup from "~/components/basicComponents/Popup";
import {
  updateUserPersonalInformation,
  getRefreshedTokens,
  getUserSettings,
  logout
} from '~/api'
export default {
  name: 'PersonalInformation',
  components: {
    Input,
    Textarea,
    Checkbox,
    Button,
    Popup
  },
  data() {
    return {
      personalInformation: {},
      loading: false,
      showPopup: false
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
  async mounted() {
    await this.getUserPersonalSettings()
  },
  methods: {
    async logout() {
      await logout(sessionStorage.getItem('_at') )
      sessionStorage.removeItem('_at')
      return this.$router.push('/')
    },
    async getUserPersonalSettings() {
      const token = sessionStorage.getItem('_at')
      this.personalInformation = await getUserSettings(token, 'personal')
      console.log('this.personalInformation', this.personalInformation)

      if (this.personalInformation.error?.errorMessage === 'token-expired') {
        const refreshedToken = await getRefreshedTokens()

        if (refreshedToken.error?.errorMessage === 'invalid-token') return await this.logout()
        else sessionStorage.setItem('_at', refreshedToken._at)

        this.personalInformation = await getUserSettings(refreshedToken._at, 'personal')
      } else if (this.personalInformation.error?.errorMessage === 'invalid-token') {
        await this.logout()
      }
    },
    async updatePersonalInfo() {
      this.loading = true

      const { message } = await updateUserPersonalInformation({
        ...this.personalInformation
      }, sessionStorage.getItem('_at'))

      if (message === 'success') {
        this.showPopup = true

        setTimeout(() => {
          this.showPopup = false
        }, 1500)
      }

      this.loading = false
    }
  },
}
</script>

<style lang="scss">
@import "../../../assets/css/pages/account/settings";
</style>
