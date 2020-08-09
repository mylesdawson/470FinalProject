<template>
  <b-row>
    <b-col></b-col>

    <b-col>
      <b-form @submit="searchWithProps">
        <b-input-group>
          <b-form-input placeholder="Search for anything" id="search-input" v-model="search"></b-form-input>
          <b-input-group-append>
            <b-btn type="submit" class="ma-2" variant="warning">
              <b-icon icon="search"></b-icon>
            </b-btn>
          </b-input-group-append>
        </b-input-group>
      </b-form>
    </b-col>

    <b-col></b-col>
  </b-row>
</template>

<script>
export default {
  name: 'SearchComponent',
  data: function() {
    return {
      search: ''
    }
  },
  methods: {
    searchWithProps: function(e) {
      this.$router.push({
        name: 'SearchPage',
        params: {
          search: this.search
        }
      })
    },
  }
}
</script>

<style scoped>

</style>