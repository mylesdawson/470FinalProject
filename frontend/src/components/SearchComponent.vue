<template>
  <b-row>
    <b-col></b-col>

    <b-col>
      <b-input-group>
        <b-form-input placeholder="Search for anything"></b-form-input>
        <b-input-group-append>
          <b-btn class="ma-2" variant="warning" to="/search">
            <b-icon icon="search"></b-icon>
          </b-btn>
        </b-input-group-append>
      </b-input-group>
    </b-col>

    <b-col></b-col>
  </b-row>
</template>

<script>
export default {
  name: 'SearchComponent'
}
</script>

<style scoped>

</style>