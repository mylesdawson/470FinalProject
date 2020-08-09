<template>
  <b-container fluid>

    <!-- <search-component></search-component> -->

    <hr class="my-3">

    <b-row>
      <b-button class="ml-3" size="sm" variant="primary" name="fitness" @click="setFilter">Fitness</b-button>
      <b-button class="ml-3" size="sm" variant="success" name="wellness" @click="setFilter">Wellness</b-button>
      <b-button class="ml-3" size="sm" variant="warning" name="beauty" @click="setFilter">Beauty</b-button>
    </b-row>
    <br>

    <h1 class="text-left"><strong>{{title}}</strong> Businesses</h1>

    <br>

    <b-card-group deck>
      <business-component
        v-for="business in businesses"
        v-bind:business="business"
        v-bind:key="business.name"
      ></business-component>
    </b-card-group>

  </b-container>
</template>

<script>
import SearchComponent from './SearchComponent'
import BusinessComponent from './BusinessComponent'
import { getBusinessesByCategory } from '../api/api'

export default {
  name: 'SearchPage',
  components: {
    SearchComponent,
    BusinessComponent
  },
  data: function() {
    return {
      filterBy: '',
      title: '',
      search: '',
      businesses: [],
    }
  },
  methods: {
    upper: function() {
      if(this.filterBy.length > 0) {
        const [head, ...rest] = this.filterBy.split("")
        return head.toUpperCase() + rest.join("")
      }
      return ''
    },
    setFilter: function(e) {
      const type = e.target.name
      this.businesses = []
      this.filterBy = type
      this.title = this.upper()
      this.getBusinesses()
    },
    getBusinesses: async function() {
      const category = this.filterBy ? this.filterBy : 'all'
      const res = await getBusinessesByCategory(category)
      console.log(res)
      this.businesses = res
    }
  },
  mounted: async function() {
    const params = this.$route.params
    const filter = params.filterBy
    console.log(filter)
    if(filter) {
      this.filterBy = filter
      this.title = this.upper()
    }

    this.getBusinesses()
  }
}
</script>

<style scoped>

</style>