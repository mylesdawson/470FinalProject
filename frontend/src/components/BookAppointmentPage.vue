<template>
  <b-container fluid class="book-appointment-container">
    <b-row v-if="service">
      <b-col>
        <h1>{{ service.name }}</h1>
      </b-col>
    </b-row>

    <b-row class="appointment-row">
      <b-col md="auto">
        <b-calendar v-model="value" @context="onContext" locale="en-US"></b-calendar>
      </b-col>
    </b-row>

    <b-row v-if="service_availability">
      <b-col>
        <h3>Availability: {{ service_availability }}</h3>
      </b-col>
    </b-row>

    <b-row v-if="service_details">
      <b-col>
        <h3>Timeslots </h3>
      </b-col>
    </b-row>

    <b-row v-if="service_details" class="appointment-row">
      <b-col>
        <b-form-select v-model="selectedTime" :options="service_details.times">
        </b-form-select>
      </b-col>
    </b-row>

    <b-row v-if="selectedTime" class="appointment-row">
      <b-col>
        <b-button variant="outline-primary" @click="bookAppointment">Book an Appointment</b-button>
      </b-col>
    </b-row>

  </b-container>
</template>

<script>
import {
  getAvailableTimeSlots,
  getServicesByBusiness,
  createCustomerAppointment,
} from '../api/api'

export default {
  name: 'BookAppointmentPage',
  data: function() {
    return {
      business_id: null,
      service_id: null,
      value: '',
      context: null,
      service_availability: null,
      service_details: null,
      selectedTime: null,
      business: null,
      service: null,
    }
  },
  methods: {
    async onContext(ctx) {
      this.service_availability = null
      this.selectedTime = null
      this.service_details = null
      this.context = ctx

      const ymd = ctx.selectedYMD

      if(ymd) {
        const [year, month, day] = ymd.split("-")
        const timeSlots = await getAvailableTimeSlots(parseInt(this.business_id), parseInt(year), parseInt(month), parseInt(day))

        // console.log(timeSlots)
        let correctService = timeSlots.services
        correctService = correctService.filter((item, index) => (correctService[index].id === parseInt(this.service_id)))[0]

        this.service_details = correctService
        this.service_availability = timeSlots.availability
        // console.log(this.service_details)
      }
    },
    async bookAppointment() {
      const ymd = this.context.activeYMD
      const duration = this.service_details.duration
      const startTime = this.selectedTime

      const [startHour, startMin] = this.selectedTime.split(":")
      let hours = 0
      let minutes = 0
      if(startMin !== '00') {
        const total = parseInt(startMin) + duration
        hours = Math.floor(total / 60)
        minutes = Math.floor(total % 60)
      } else {
        hours = Math.floor(duration / 60)
        minutes = Math.floor(duration % 60)
      }

      const endHours = parseInt(startHour) + hours
      const endTime = endHours  + ':' + minutes
      const accountId = localStorage.getItem("account_id")

      try {
        const res = await createCustomerAppointment(ymd, startTime, endTime, accountId, this.business_id, this.service_id)
        console.log(res)
        if(res.id) {
          this.$router.push("/appointments")
        }
      } catch(e) {
        console.log(e)
      }
    }
  },
  mounted: async function() {
    const params = this.$route.params
    if(params.business_id && params.service_id) {
      this.business_id = params.business_id
      this.service_id = params.service_id

      const res = await getServicesByBusiness(parseInt(this.business_id))
      const correctService = res.filter((item, index) => (res[index].id === parseInt(this.service_id)))[0]

      this.service = correctService
      // console.log(this.service)
    }
  }
}
</script>

<style scoped>
  .appointment-row {
    margin-bottom: 1rem;
  }

  .book-appointment-container {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
</style>