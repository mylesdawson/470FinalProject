<template>
  <b-list-group-item>
    <b-row align-v="center">
      <b-col sm lg="2" style="text-align: left">
        <strong>{{ service.name }}</strong>
        <br>
        {{ service.duration }} minutes
      </b-col>
      <b-col sm lg="6" style="text-align: left">
        {{ service.description }}
      </b-col>
      <b-col sm lg="2" style="font-size: 1.5rem; text-align: right">
        <strong>$ {{ service.price }}</strong>
      </b-col>
      <b-col sm lg="2" style="text-align: right">
        <b-button variant="primary" style="font-size: 18px; width: 120px; height: 48px" name="all" @click="toBookAppointment">Book</b-button>
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
  data: function() {
    return {
      showModal: false,
    }
  },
  name: 'ServiceComponent',
  methods: {
    toBookAppointment: function() {
      if(!localStorage.getItem("token")) {
        this.$router.push("/login")
      } else {
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
}
</script>

<style scoped>

</style>