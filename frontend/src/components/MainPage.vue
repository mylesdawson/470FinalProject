<template>
  <b-container fluid>
    <h1 class="text-center"><strong>Explore</strong> and <strong>book</strong> anything <strong>fitness</strong>, <strong>wellness</strong>, <strong>beauty</strong></h1>
    <br>
    <b-row>
      <b-col col md="3">
      </b-col>
      <b-col cols="6" ml="6" style="text-align: right">
	    <b-input-group>
	      <b-input-group-prepend is-text>
	      <b-icon icon="search"></b-icon>
	      </b-input-group-prepend>
	      <b-form-input aria-label="First name" placeholder="Search for anything"></b-form-input>
	      <b-form-input aria-label="Last name" placeholder="Location"></b-form-input>
	    </b-input-group>
      </b-col>
      <b-col col md="3" style="text-align: left">
	    <b-btn class="ma-2" variant="warning">
          <b-icon icon="search"></b-icon>
	    </b-btn>
      </b-col>
    </b-row>

    <h2 class="text-center">
      <br><strong>Explore</strong> Skedge
    </h2>
    <br>
    <b-row align-h="center">
      <b-button class="mr-5" size="lg" variant="primary" href="/?#/search">Fitness</b-button>
      <b-button class="mr-5" size="lg" variant="success" href="/?#/search">Wellness</b-button>
      <b-button class="mr-5" size="lg" variant="warning" href="/?#/search">Beauty</b-button>
    </b-row>

  </b-container>
</template>

<script>
export default {
  name: 'MainPage'
}
</script>

<style scoped>

</style>