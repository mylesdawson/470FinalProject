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

      <b-card title="Hair Salon" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Beautiful hair with beautiful care
        </b-card-text>
        <b-button size="sm" variant="primary">View</b-button>
      </b-card>

      <b-card title="Barber" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          A quality hair cut at a fair price.
        </b-card-text>
        <b-button size="sm" variant="primary">View</b-button>
      </b-card>

      <b-card title="Fitness Gym Big Muscles" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Sponsored by Gym Shark.
        </b-card-text>
        <b-button size="sm" variant="primary">View</b-button>
      </b-card>

      <b-card title="Other" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Other
        </b-card-text>
        <b-button size="sm" variant="primary">View</b-button>
      </b-card>

      <b-card title="Other" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Other
        </b-card-text>
        <b-button size="sm" variant="primary">View</b-button>
      </b-card>

      <b-card title="Other" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Other
        </b-card-text>
        <b-button size="sm" variant="primary">View</b-button>
      </b-card>

      <b-card title="Other" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Other
        </b-card-text>
        <b-button size="sm" variant="primary">View</b-button>
      </b-card>

      <b-card title="Other" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Other
        </b-card-text>
        <b-button size="sm" variant="primary">View</b-button>
      </b-card>

      <b-card title="Other" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Other
        </b-card-text>
        <b-button size="sm" variant="primary">View</b-button>
      </b-card>

      <b-card title="Other" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Other
        </b-card-text>
        <b-button size="sm" variant="primary">View</b-button>
      </b-card>

      <b-card title="Other" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Other
        </b-card-text>
        <b-button size="sm" variant="primary">View</b-button>
      </b-card>

      <b-card title="Other" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Other
        </b-card-text>
        <b-button size="sm" variant="primary">View</b-button>
      </b-card>

    </b-card-group>

  </b-container>
</template>

<script>
export default {
  name: 'SearchPage'
}
</script>

<style scoped>

</style>