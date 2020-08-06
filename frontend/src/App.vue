<template>
  <div id="app">
    <Navbar />
    <b-container fluid style="margin-top: 15px;">
      <router-view/>
    </b-container>
  </div>
</template>

<script>
import Navbar from './components/Navbar'

export default {
  name: 'App',
  components: {
    Navbar
  },
  data: {
    token: ''
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
}
</style>
