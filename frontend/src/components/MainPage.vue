<template>
  <b-container fluid>
    <h1 class="text-center"><strong>Explore</strong> and <strong>book</strong> anything <strong>fitness</strong>, <strong>wellness</strong>, <strong>beauty</strong></h1>

    <!-- <search-component></search-component> -->

    <h2 class="text-center">
      <br><strong>Explore</strong> Skedge
    </h2>
    <br>
    <b-row align-h="center">
      <b-button class="mr-5" size="lg" name="fitness" variant="primary" @click="searchWithProps">Fitness</b-button>
      <b-button class="mr-5" size="lg" name="wellness" variant="success" @click="searchWithProps">Wellness</b-button>
      <b-button class="mr-5" size="lg" name="beauty" variant="warning" @click="searchWithProps">Beauty</b-button>
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