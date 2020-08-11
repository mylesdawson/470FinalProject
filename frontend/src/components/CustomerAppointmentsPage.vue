<template>
  <b-container fluid>
    <b-row>
      <h1 class="title">Your Booked Appointments</h1>
    </b-row>
      <b-card-group deck>
        <b-card
          v-for="appointment in appointments"
          v-bind:key="appointment.id"
        >
          <b-card-title>
            {{ appointment.service.name }}
          </b-card-title>
          <hr>
          <b-card-text>
            <p>
              {{ appointment.service.description }}
            </p>
            <br>
            <p>
              Date: {{ appointment.date }}
            </p>
            <p>
              Start time: {{ appointment.start_time}}
            </p>
            <p>
              Duration: {{ appointment.service.duration }} minutes
            </p>

            <hr>
            <b-button @click="cancelAppointment(appointment.id)">Cancel Appointment</b-button>
          </b-card-text>
        </b-card>
      </b-card-group>
    <b-row>

    </b-row>
  </b-container>
</template>

<script>
import { getCustomerAppointments, cancelCustomerAppointment } from '../api/api'

export default {
  name: 'CustomerAppointmentsPage',
  data: function() {
    return {
      appointments: null
    }
  },
  mounted: async function() {
    const accountId = localStorage.getItem("account_id")

    try {
      let res = await getCustomerAppointments(accountId)
      res = res.filter(appt => !appt.cancelled)
      console.log(res)
      this.appointments = res
    } catch(e) {
      console.log(e)
    }
  },
  methods: {
    async cancelAppointment(appointmentId) {
      const custId = localStorage.getItem("account_id")
      try {
        const res = await cancelCustomerAppointment(custId, appointmentId)
        console.log(res)
        this.appointments = this.appointments.filter(appt => appt.id !== res.id)
      } catch (error) {
        console.log(error)
      }
    }
  }
}
</script>

<style scoped>
  h1.title {
    width: 100%;
    text-align: center;
  }
  p {
    margin-bottom: 0;
  }
  h1 {
    margin-bottom: 2rem;
  }
</style>