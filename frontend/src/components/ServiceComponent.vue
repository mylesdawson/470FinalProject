<template>
  <b-list-group-item>
    <b-row align-v="center">
      <b-col cols="2">
        <strong>{{ service.name }}</strong>
        <br>
        {{ service.duration }} minutes
      </b-col>
      <b-col cols="6">
        {{ service.description }}
      </b-col>
      <b-col cols="2" style="font-size: 1.5rem;">
        <strong>$ {{ service.price }}</strong>
      </b-col>
      <b-col cols="2">
        <b-button>Book Appointment</b-button>
      </b-col>
    </b-row>
  </b-list-group-item>
</template>

<script>
export default {
  props: [
    "service"
  ],
  name: 'ServiceComponent'
}
</script>

<style scoped>

</style>