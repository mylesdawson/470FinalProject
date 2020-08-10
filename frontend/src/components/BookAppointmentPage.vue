<template>
  <b-container fluid>
    <b-row>
      <h1>Book: service-type</h1>
    </b-row>

    <b-row class="appointment-row">
      <b-col md="auto">
        <b-calendar v-model="value" @context="onContext" locale="en-US"></b-calendar>
      </b-col>
    </b-row>

    <b-row v-if="service_info">
      <b-col>
        <h3>Availability: {{ service_info.availability }}</h3>
      </b-col>

    </b-row>

    <b-row>
      <b-col>
        <h3>Timeslots: </h3>
      </b-col>

      <!-- <div
        v-for="time in service_info.details.times"
        v-bind:key="time"
      >
        {{ time }}
      </div> -->
    </b-row>

  </b-container>
</template>

<script>
import { getAvailableTimeSlots } from '../api/api'

export default {
  name: 'BookAppointmentPage',
  data: function() {
    return {
      business_id: null,
      service_id: null,
      value: '',
      context: null,
      service_info: null
    }
  },
  methods: {
    async onContext(ctx) {
      this.service_info= null
      this.context = ctx

      const ymd = ctx.selectedYMD

      if(ymd) {
        const [year, month, day] = ymd.split("-")
        const timeSlots = await getAvailableTimeSlots(parseInt(this.business_id), parseInt(year), parseInt(month), parseInt(day))

        // console.log(timeSlots)
        let correctService = timeSlots.services
        correctService = correctService.filter((item, index) => (correctService[index].id === parseInt(this.service_id)))[0]

        const service = {
          availability: timeSlots.availability,
          details: correctService
        }

        this.service_info = service
        console.log(this.service_info)
      }
    }
  },
  mounted: function() {
    const params = this.$route.params
    if(params.business_id && params.service_id) {
      this.business_id = params.business_id
      this.service_id = params.service_id
    }
  }
}
</script>

<style scoped>
  .appointment-row {
    margin-bottom: 1rem;
  }
</style>