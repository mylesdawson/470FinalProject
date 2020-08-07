<template>
  <div class="login-container">
      <b-card title="Create an Account" :aria-hidden="show ? 'true' : null">
        <b-form>
          <b-form-group class="account-type">
              <b-form-radio v-model="form.selected" value="customer">
                User Account
              </b-form-radio>
              <b-form-radio v-model="form.selected" value="business">
                Business Account
              </b-form-radio>
          </b-form-group>

          <b-form-group label="Username" label-for="username">
            <b-form-input
              id="username"
              v-model="form.username"
              required
              placeholder="Enter Username"
            ></b-form-input>
          </b-form-group>

          <b-form-group label="Password" label-for="password">
            <b-form-input
              id="password"
              v-model="form.password"
              required
              placeholder="Enter Password"
              type="password"
            ></b-form-input>
          </b-form-group>


          <b-form-group
            label="Business Name"
            label-for="businessName"
            v-if="form.selected === 'business'"
          >
            <b-form-input
              id="businessName"
              v-model="form.business.name"
              required
              placeholder="Enter Business Name"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            label="Business Type"
            label-for="businessType"
            v-if="form.selected === 'business'"
          >
            <b-form-select
              id="businessType"
              v-model="form.business.selectedType"
              :options="form.business.businessTypes"
              required
            ></b-form-select>
          </b-form-group>

          <b-overlay :show="show" rounded="sm">
            <button type="submit" class="btn btn-primary btn-lg login-input" v-on:click="logon">
              Create Account!
            </button>
          </b-overlay>

        </b-form>


      </b-card>
  </div>
</template>




<script>
import { createCustomerAccount, createBusinessAccount } from '../api/api.js'

export default {
  name: 'login-page',
  data: function() {
    return {
      show: false,
      form: {
        selected: 'customer',
        username: '',
        password: '',
        customer: {

        },
        business: {
          name: '',
          selectedType: null,
          businessTypes: [
            { value: null, text: 'please select a business type'},
            { value: 'fitness', text: 'fitness'},
            { value: 'wellness', text: 'wellness'},
            { value: 'beauty', text: 'beauty'},
          ],
        },

      }
    }
  },
  methods: {
    logon: async function() {

      try {
        this.show = true
        if (this.form.selected === 'customer') {
          const res = await createCustomerAccount(this.form.username, this.form.password, this.form.customer)
          // TODO: go to account created successfully page with login component embeded!
          // Right now it has no feedback message on account created successfully
          if(res.username) {
            this.$router.push('/login')
          }
        } else {
          const businessInfo = {
            "business_name": this.form.business.name,
            "category": this.form.business.selectedType
          }
          const res = await createBusinessAccount(this.form.username, this.form.password, businessInfo)
          if(res.username) {
            this.$router.push('/login')
          }
        }

        this.show = false
      } catch(e) {
        this.show = false
        console.log(e)
      }
    }
  }
}
</script>

<style scoped>
  div.login-container {
    max-width: 500px;
    margin: auto;
  }

  .login-input {
    width: 100%;
    margin-top: 1.5rem;
    text-align: center;
  }

  .account-type {
    text-align: left;
  }

  .card-title {
    text-align: center;
    margin-bottom: 2rem;
  }

</style>