<template>
  <div>
    <h1>Login Page!</h1>

    <div>
      <p>Username: </p>
      <input v-model="username" type="text" placeholder="username">
    </div>
    <div class="password-section">
      <p>Password: </p>
      <input v-model="password" type="text" placeholder="password">
    </div>
    <div>
      <button v-on:click="logon">Login!</button>
    </div>
  </div>
</template>

<script>
import { login, users } from '../api/api.js'

export default {
  name: 'login-page',
  data: function() {
    return ({
      username: '',
      password: '',

    })
  },
  methods: {
    logon: async function() {
      try {
        await users()
        // await login(this.username, this.password)
      } catch(e) {
        console.log(e)
      }
    }
  }
}
</script>

<style scoped>
div.password-section {
  margin-bottom: 1rem;
}
</style>