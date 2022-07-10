<template>
  <div>
    <Popup v-if="showPopup" :content="'Personal settings has been successfully updated!'" />
    <div class="account-preferences flex">

      <div class="fields">
        <div class="flex">
          <Input
            v-model="personalInfo.first_name"
            :title="'First name'"
            :title-class="'small'"
            :additional-class="'small'"
          />
          <Input
            v-model="personalInfo.last_name"
            :title="'Last name'"
            :title-class="'small'"
            :additional-class="'small'"
          />
        </div>
        <Textarea
          v-model="personalInfo.about_me"
          :title="'About'"
        />
        <div class="flex">
          <Input
            v-model="personalInfo.website_link"
            :title="'Website'"
            :title-class="'small'"
            :additional-class="'small'"
          />
          <Input
            v-model="personalInfo.twitter"
            :title="'Twitter'"
            :title-class="'small'"
            :additional-class="'small'"
          />
          <Input
            v-model="personalInfo.github"
            :title="'GitHub'"
            :title-class="'small'"
            :additional-class="'small'"
          />
        </div>
      </div>

      <div class="profile-picture flex">
        <div class="relative">
          <img class="picture" :src="require('../../../assets/img/testava.jpg')" alt="ava">
          <div style="bottom: 0; right: 0; position: absolute;">
            <Button :label="'Change avatar'" />
          </div>
        </div>
      </div>
    </div>

    <div class="account-preferences">
      <div class="button">
        <Button :label="'Save settings'" :additional-class="'min-width150 mt'" @click-handler="updatePersonalInfo" />
      </div>
    </div>

  </div>
</template>

<script>
import Input from '~/components/Input';
import Textarea from "~/components/Textarea";
import Button from "~/components/Button";
import Popup from "~/components/Popup";
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
      personalInfo: {},
      loading: false,
      showPopup: false
    }
  },
  async mounted() {
    if (sessionStorage.getItem('token')) await this.getUserPersonalSettings(sessionStorage.getItem('token'))
    else return this.$router.push('/')
  },
  methods: {
    async getUserPersonalSettings(token) {
      this.personalInfo = await getUserSettings(token, 'personal')

      if (this.personalInfo.status === -1)
        return this.$router.push('/')
    },
    async updatePersonalInfo() {
      this.loading = true

      const { status } = await updateUserPersonalInformation({ ...[this.personalInfo] })

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
@import "../../../assets/css/edit";
</style>
