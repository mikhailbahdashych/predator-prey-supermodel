<template>
  <div class="account-preferences">
    <Popup v-if="showPopup" :content="'Personal settings has been successfully updated!'" />
    <div class="flex">

      <div class="fields">
        <div class="flex">
          <Input
            v-model="personalInformation.first_name"
            :title="'First name'"
            :title-class="'small'"
            :additional-class="'small'"
          />
          <Input
            v-model="personalInformation.last_name"
            :title="'Last name'"
            :title-class="'small'"
            :additional-class="'small'"
          />
        </div>
        <div class="flex">
          <Input
            v-model="personalInformation.website_link"
            :title="'Website'"
            :title-class="'small'"
            :additional-class="'small'"
          />
          <Input
            v-model="personalInformation.twitter"
            :title="'Twitter'"
            :title-class="'small'"
            :additional-class="'small'"
          />
          <Input
            v-model="personalInformation.github"
            :title="'GitHub'"
            :title-class="'small'"
            :additional-class="'small'"
          />
        </div>
        <Textarea
          v-model="personalInformation.about_me"
          :title="'About'"
        />
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

    <div class="button">
      <Button :label="'Save settings'" :additional-class="'min-width150 mt'" @click-handler="updatePersonalInfo" />
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
