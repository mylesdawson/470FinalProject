<template>
  <b-container fluid>

    <b-row>
      <b-col cols="6" ml="1" style="text-align: left">
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

    <hr class="my-3">

    <b-row align-h="left">
      <b-button class="ml-3" size="sm" variant="primary">Fitness</b-button>
      <b-button class="ml-3" size="sm" variant="success">Wellness</b-button>
      <b-button class="ml-3" size="sm" variant="warning">Beauty</b-button>
    </b-row>
    <br>

    <h1 class="text-left"><strong>Beauty</strong> Business in Location, <strong>BC</strong></h1>

    <br>

    <b-card-group>
    <b-card title="Hair Salon" img-src="https://placekitten.com/g/300/450" img-alt="Image" img-top>
      <b-card-text>
        Beautiful hair with beautiful care
      </b-card-text>
      <template v-slot:footer>
        <small class="text-muted">Walk-in customers allowed</small>
      </template>
    </b-card>

    <b-card title="Barber" img-src="https://placekitten.com/g/300/450" img-alt="Image" img-top>
      <b-card-text>
        A quality hair cut at a fair price.
      </b-card-text>
      <template v-slot:footer>
        <small class="text-muted">Same day bookings available</small>
      </template>
    </b-card>

    <b-card title="Fitness Gym Big Muscles" img-src="https://placekitten.com/g/300/450" img-alt="Image" img-top>
      <b-card-text>
        Sponsored by Gym Shark.
      </b-card-text>
      <template v-slot:footer>
        <small class="text-muted">Covid-19 approved</small>
      </template>
    </b-card>
  </b-card-group>


  </b-container>
</template>

<script>
export default {
  name: 'MainPage'
}
</script>

<style scoped>

</style>