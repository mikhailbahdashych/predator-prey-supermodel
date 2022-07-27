<template>
  <div class="awesome-phone-input">

    <div :key="country" class="awesome-phone-input__country" @click="showDialList = !showDialList">
      <img v-if="country" :src="flagUrl" alt="Flag" />
      <img v-else src="../../assets/img/unknown.svg" alt="Unknown" />
    </div>

    <div v-if="showDialList" v-click-outside="clickOutsideList" class="country-container">

      <div class="country-container__dial-filter">
        <img
          src="../../assets/img/search.svg"
          class="country-container__input-loop"
          alt="Search"
        />
        <input
          ref="phoneInputDialFilter"
          v-model="dialCodeFilter"
          class="country-container__input"
          type="text"
        />
        <img
          v-if="dialCodeFilter"
          src="../../assets/img/close.svg"
          alt="Clear"
          @click="dialCodeFilter = null"
        />
      </div>

      <ul :key="dialCodeFilter" class="country-container__country-list">
        <li v-for="c in filteredDialCodes"
            :key="c.name"
            :class="{ active: false }"
            class="country-container__country-list-item"
            @click="inputSelectedCountry = c; showDialList = false;"
        >
          <img
            class="country-container__flag"
            :src="getFlagUrlByCode({ code: c.country.toLowerCase() })"
            alt="Flag"
          />
          <span>{{ c.name }}</span>
          <span>+ {{ c.dial }}</span>
        </li>
      </ul>
    </div>

    <client-only>
      <the-mask
        v-model="phoneNumber"
        type="text"
        class="phone"
        :name="'Phone Number'"
        :mask="inputMask"
        :tokens="numberToken"
        inputmode="numeric"
        pattern="[0-9]*"
      />
    </client-only>

  </div>
</template>

<script>
import {allCountries} from 'country-telephone-data'
import vClickOutside from 'v-click-outside'
import {getAvailableFlags} from '~/api'
export default {
  name: 'PhoneInput',
  directives: {
    clickOutside: vClickOutside.directive
  },
  data () {
    return {
      baseSrc: 'https://flagcdn.com/',
      country: null,
      availableFlags: [],
      flagUrl: null,

      phoneNumber: null,

      inputSelectedCountry: null,
      showDialList: false,
      dialCodeFilter: null,

      numberToken: {
        N: {
          pattern: /[0-9]/,
          transform: v => v
        }
      }
    }
  },
  computed: {
    inputMask () {
      if (this.phoneNumber && this.phoneNumber.slice(0, 2) === '86') {
        return ['+NN NNN NNNN NNNN']
      } else if (this.phoneNumber && this.phoneNumber.slice(0, 2) === '49') {
        return ['+NN NNN NNNNNNNN']
      }
      return this.inputSelectedCountry && this.inputSelectedCountry.format ? [this.inputSelectedCountry.format.replace(/\./g, 'N')] : ['+NNNNNNNNNNNNNNN']
    },
    dialCodes () {
      return allCountries.map(x => {
        return {
          dial: x.dialCode,
          name: x.name,
          format: x.format,
          country: x.iso2
        }
      })
    },
    filteredDialCodes () {
      return this.dialCodeFilter ? this.dialCodes.filter(
        x => x.name.toLowerCase().includes(this.dialCodeFilter?.toLowerCase()) || x.dial.includes(this.dialCodeFilter)
      ) : this.dialCodes
    }
  },
  watch: {
    showDialList (value) {
      if (value) {
        this.$nextTick(() => this.$refs.phoneInputDialFilter.focus())
      }
    },
    inputSelectedCountry ({ dial: newDial }, oldCountry) {
      if (oldCountry) {
        const oldDial = oldCountry.dial

        const oldNumberPart = this.phoneNumber.slice(oldDial.length, this.phoneNumber.length)
        this.phoneNumber = `${newDial}${oldNumberPart}`
      } else {
        this.phoneNumber = newDial
      }
    },
    country () {
      const selectedCountry = this.dialCodes.find(x => x.country === this.country)

      if (selectedCountry) {
        this.inputSelectedCountry = selectedCountry
      }
    },
    phoneNumber () {
      this.checkDial()
    }
  },
  async mounted () {
    this.checkDial()
    await this.saveAvailableFlags()
  },
  methods: {
    clickOutsideList ({target}) {
      if (target.className !== 'country' && target.parentElement.className !== 'country') {
        this.showDialList = false
      }
    },
    getFlagUrlByCode (data) {
      return this.baseSrc + data.code + '.svg'
    },
    checkIfFlagExist (data) {
      const {countryCode} = data

      for (const code of Object.keys(this.availableFlags)) {
        if (code.includes(countryCode)) {
          return true
        }
      }

      return false
    },
    async saveAvailableFlags () {
      this.availableFlags = await getAvailableFlags()
    },
    checkDial () {
      try {
        for (const dialCountry of this.dialCodes) {
          const {
            country,
            dial
          } = dialCountry

          const len = dial.length

          if (this.phoneNumber.length >= len) {
            const slice = this.phoneNumber.slice(0, len)

            if (dial === slice) {
              if (this.checkIfFlagExist({countryCode: country})) {
                this.country = country
                this.flagUrl = this.baseSrc + this.country + '.svg'

                this.errors.remove('dialCode')

                if (!this.errors.length) {
                  this.$emit('input', '+' + this.phoneNumber)
                } else {
                  this.$emit('input', null)
                }
                return
              } else {
                this.setError()
              }
            } else {
              this.setError()
            }
          } else {
            this.country = null
            this.flagUrl = '../../assets/img/unknown.svg'
          }
        }
      } catch (e) {

      }
    },
    setError () {
      this.$emit('input', null)

      this.errors.add({
        field: 'dialCode',
        msg: 'Dial code does not exist'
      })

      this.country = null
      this.flagUrl = '../../assets/img/unknown.svg'
    }
  }
}
</script>

<style lang="scss">
@import "../../assets/css/basicComponents/PhoneInput";
</style>
