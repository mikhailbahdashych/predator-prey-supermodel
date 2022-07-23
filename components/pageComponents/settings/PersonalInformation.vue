<template>
  <div class="account-preferences">
    <Popup v-if="showPopup" :content="'Personal settings has been successfully updated!'" />

    <div class="account-preferences__fields-wrap">
      <div class="account-preferences__fields-wrap__fields">
        <div class="account-preferences__fields-wrap">
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
        </div>
        <div class="account-preferences__fields-wrap">
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
        </div>
        <Input
          v-model="personalInformation.status"
          :title="'Status'"
          :input-class="'bi--basic-input__small'"
        />
        <Textarea
          v-model="personalInformation.about_me"
          :title="'About'"
        />
      </div>

      <div class="account-preferences__profile-picture">
        <div class="account-preferences__profile-picture__box">
          <img class="account-preferences__profile-picture__box__picture" :src="require('../../../assets/img/testava.jpg')" alt="ava">
          <div class="account-preferences__profile-picture__box__button">
            <Button :label="'Change avatar'" />
          </div>
        </div>
      </div>
    </div>

    <div class="account-preferences__button">
      <Button :label="'Save settings'" :btn-class="'basic-button--min-width'" @click-handler="updatePersonalInfo" />
    </div>

  </div>
</template>

<script>
import Input from '~/components/basicComponents/Input';
import Textarea from "~/components/basicComponents/Textarea";
import Button from "~/components/basicComponents/Button";
import Popup from "~/components/basicComponents/Popup";
import {
  updateUserPersonalInformation,
  getUserSettings
} from "~/api";
export default {
  name: 'PersonalInformation',
  components: {
    Input,
    Textarea,
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
    async getUserPersonalSettings() {
      const token = sessionStorage.getItem('_at')
      this.personalInformation = await getUserSettings(token, 'personal')

      if (this.personalInformation.status === -1 || this.personalInformation.status === 401)
        return this.$router.push('/signin')
    },
    async updatePersonalInfo() {
      this.loading = true

      const { status } = await updateUserPersonalInformation({
        ...this.personalInformation
      }, sessionStorage.getItem('_at'))

      if (status === 1) {
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
