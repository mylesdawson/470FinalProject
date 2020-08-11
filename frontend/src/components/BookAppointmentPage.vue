<template>
  <b-container fluid style="max-width:1500px;margin-top: 0px autopx">
    
    <b-card style="border:none">
      <b-card-title v-if="service">{{ service.name }}</b-card-title>
      <hr>
    <b-row>
      <b-col style="min-width:320px;margin-top: 24px" cols="12" md="3">
          <b-calendar v-model="value" @context="onContext" locale="en-US" width="320px"></b-calendar>
      </b-col>
    
     <b-col cols="12" md="9" style="margin-top: 24px;">
     <b-card v-if="service_availability" bg-variant="light">
     <b-card-title>Availability: <b>{{ service_availability }}</b> </b-card-title>
       
       
     
     <b-form-group
      v-if="service_details"
          label="Timeslots:">
          <b-form-select  v-if="service_details" v-model="selectedTime" :options="service_details.times">
        </b-form-select>
        </b-form-group>
 

        <b-button v-if="selectedTime" variant="outline-primary" @click="bookAppointment">Book an Appointment</b-button>
         </b-card>
      </b-col>
      </b-row>
    </b-card>

   
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