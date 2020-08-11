<template>

  <div class="login-container">
        <b-overlay :show="show" rounded="sm">
         <b-card class="text-center" title="Login" :aria-hidden="show ? 'true' : null">

            <input v-model="username" type="text" placeholder="username" class="form-control login-input">
            <input v-model="password" type="password" placeholder="password" class="form-control login-input">
            <button type="button" class="btn btn-primary btn-lg login-input" v-on:click="logon">Login</button>

         </b-card>
      </b-overlay>
    </div>
</template>




<script>
import { login } from '../api/api.js'

export default {
  name: 'login-page',
  data: function() {
    return ({
      username: '',
      password: '',
      show: false
    })
  },
  methods: {
    logon: async function() {

      try {
        this.show = true;
        const res = await login(this.username, this.password)
        if (res.token) {
          this.$router.push('/')
        }
        this.show = false
      } catch(e) {
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
    margin-top: 24px;
  }

</style>