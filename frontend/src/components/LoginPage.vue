<template>

  <div class="login-container">
        <b-overlay :show="show" rounded="sm">
         <b-card class="text-center" title="Login" :aria-hidden="show ? 'true' : null">
            <b-form @submit="logon">
              <input v-model="username" type="text" placeholder="username" class="form-control login-input">
              <input v-model="password" type="password" placeholder="password" class="form-control login-input">
              <p class="error-message danger">{{ errorMsg }}</p>
              <button type="submit" class="btn btn-primary btn-lg login-input">Login</button>
            </b-form>
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
      show: false,
      errorMsg: '',
    })
  },
  methods: {
    logon: async function() {

      try {
        this.errorMsg = ''
        this.show = true;
        const res = await login(this.username, this.password)
        if (res.token) {
          this.$router.push('/')
        }
      } catch(e) {
        this.errorMsg = "Failed to Login, please try again"
      } finally {
        this.show = false
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
    margin-top: 1rem;
  }
  button.login-input {
    margin-top: 1rem;
  }

  .error-message {
    margin-top: .5rem;
    margin-bottom: 0;
    color: #dc3545;
    text-align: left;
  }

</style>