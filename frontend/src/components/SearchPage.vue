<template>
  <b-container fluid>

    <search-component></search-component>

    <hr class="my-3">

    <b-row>
      <b-button class="ml-3" size="sm" variant="primary" name="fitness" @click="setFilter">Fitness</b-button>
      <b-button class="ml-3" size="sm" variant="success" name="wellness" @click="setFilter">Wellness</b-button>
      <b-button class="ml-3" size="sm" variant="warning" name="beauty" @click="setFilter">Beauty</b-button>
    </b-row>
    <br>

    <h1 class="text-left"><strong>{{title}}</strong> Businesses</h1>

    <br>

    <b-card-group>

      <b-card title="Hair Salon" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Beautiful hair with beautiful care
        </b-card-text>
        <b-button size="sm" variant="primary" href="/?#/search-listings">View</b-button>
      </b-card>

      <b-card title="Barber" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          A quality hair cut at a fair price.
        </b-card-text>
        <b-button size="sm" variant="primary" href="/?#/search-listings">View</b-button>
      </b-card>

      <b-card title="Fitness Gym Big Muscles" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Sponsored by Gym Shark.
        </b-card-text>
        <b-button size="sm" variant="primary" href="/?#/search-listings">View</b-button>
      </b-card>

      <b-card title="Other" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Other
        </b-card-text>
        <b-button size="sm" variant="primary" href="/?#/search-listings">View</b-button>
      </b-card>

      <b-card title="Other" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Other
        </b-card-text>
        <b-button size="sm" variant="primary" href="/?#/search-listings">View</b-button>
      </b-card>

      <b-card title="Other" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Other
        </b-card-text>
        <b-button size="sm" variant="primary" href="/?#/search-listings">View</b-button>
      </b-card>

      <b-card title="Other" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Other
        </b-card-text>
        <b-button size="sm" variant="primary" href="/?#/search-listings">View</b-button>
      </b-card>

      <b-card title="Other" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Other
        </b-card-text>
        <b-button size="sm" variant="primary" href="/?#/search-listings">View</b-button>
      </b-card>

      <b-card title="Other" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Other
        </b-card-text>
        <b-button size="sm" variant="primary" href="/?#/search-listings">View</b-button>
      </b-card>

      <b-card title="Other" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Other
        </b-card-text>
        <b-button size="sm" variant="primary" href="/?#/search-listings">View</b-button>
      </b-card>

      <b-card title="Other" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Other
        </b-card-text>
        <b-button size="sm" variant="primary" href="/?#/search-listings">View</b-button>
      </b-card>

      <b-card title="Other" img-src="https://picsum.photos/600/300/?image=25" style="min-width: 18rem;">
        <b-card-text>
          Other
        </b-card-text>
        <b-button size="sm" variant="primary" href="/?#/search-listings">View</b-button>
      </b-card>

    </b-card-group>

  </b-container>
</template>

<script>
import SearchComponent from './SearchComponent'


export default {
  name: 'SearchPage',
  components: {
    SearchComponent,
  },
  data: function() {
    return {
      filterBy: '',
      title: ''
    }
  },
  methods: {
    upper: function() {
      if(this.filterBy.length > 0) {
        const [head, ...rest] = this.filterBy.split("")
        // console.log(head)
        // console.log(rest)
        return head.toUpperCase() + rest.join("")
      }
      return ''
    },
    setFilter: function(e) {
      const type = e.target.name
      this.filterBy = type
      this.title = this.upper()
    }
  },
  mounted: function() {
    const filter = this.$route.params.filterBy
    console.log(filter)
    if(filter) {
      this.filterBy = filter
      this.title = this.upper()
    }
  }
}
</script>

<style scoped>

</style>