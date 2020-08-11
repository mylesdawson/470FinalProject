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
              Start time: {{ appointment.start_time}}
            </p>
            <p>
              Duration: {{ appointment.service.duration }} minutes
            </p>
          </b-card-text>
        </b-card>
      </b-card-group>
    <b-row>

    </b-row>
  </b-container>
</template>

<script>
import { getCustomerAppointments } from '../api/api'

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
      const res = await getCustomerAppointments(accountId)
      console.log(res)
      this.appointments = res
    } catch(e) {
      console.log(e)
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
</style>