<template>
  <b-container fluid>

    <p style="font-size: 60px; text-align: center;"><strong>Skedge</strong></p>

    <b-row align-h="center" class="mb-5">
      <img center src="../assets/logo.png" width="200px" height="200px" class="center">
    </b-row>

    <br>

    <p style="font-size: 30px; text-align: center;"><strong>Explore</strong> and <strong>book</strong> anything <strong>fitness</strong>, <strong>wellness</strong>, <strong>beauty</strong></p>

    <!-- <search-component></search-component> -->

    <br>
    <br>

    <b-row align-h="center" class="mb-5">
      <b-button class="mr-5" size="lg" name="fitness" style="background-color: #0091EA; color: black; width: 16rem; height: 140px; border-radius: 30px; font-size: 40px; font-weight:bold; border: none; margin-bottom: 20px;" @click="searchWithProps">Fitness</b-button>
      <b-button class="mr-5" size="lg" name="wellness" style="background-color: #00E676; color: black; width: 16rem; height: 140px; border-radius: 30px; font-size: 40px; font-weight:bold; border: none; margin-bottom: 20px" @click="searchWithProps">Wellness</b-button>
      <b-button class="mr-5" size="lg" name="beauty" style="background-color: #FF9E80; color: black; width: 16rem; height: 140px; border-radius: 30px; font-size: 40px; font-weight:bold; border: none" @click="searchWithProps">Beauty</b-button>
    </b-row>

  </b-container>
</template>

<script>
import SearchComponent from './SearchComponent'

export default {
  name: 'MainPage',
  components: {
    SearchComponent,
  },
  methods: {
    searchWithProps: function(e) {
      this.$router.push({
        name: 'SearchPage',
        params: {
          filterBy: e.target.name
        }
      })
    },
  }
}
</script>

<style scoped>

</style>