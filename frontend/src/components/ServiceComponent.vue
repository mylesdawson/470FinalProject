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
        <b-button style="background-color: #ebebeb; color: black; border: none; width: 6rem; height: 40px; font-size: 16px; font-weight:bold;" name="all" @click="toBookAppointment">Book</b-button>
      </b-col>
    </b-row>
  </b-list-group-item>
</template>

<script>
export default {
  props: [
    "service",
    "businessId"
  ],
  name: 'ServiceComponent',
  methods: {
    toBookAppointment: function() {
      this.$router.push({
        path: `/search-listing/${this.businessId}/book/${this.service.id}`,
        params: {
          service: this.service,
          business: this.business
        },
      })
    }
  }
}
</script>

<style scoped>

</style>