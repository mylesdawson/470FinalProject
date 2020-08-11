<template>
<div>
    <b-row>
      <h1 class="title">Your Booked Appointments</h1>
      </b-row>
      <hr>
          <b-row style="margin-bottom: 16px;" v-for="appointment in appointments" v-bind:key="appointment.id">
          <b-col style="max-width: 500px; margin: 0px auto;">
          <b-card 
              bg-variant="light"
              :header="appointment.date"
            >

                  <b-row>
                      <b-col>
                       <b-card-title>{{appointment.service.name}}</b-card-title>
                       <b-card-sub-title class="mb-2">{{appointment.service.description}}</b-card-sub-title>
                      </b-col>
                  
                      <b-col style="text-align: right">
                      <b-badge v-if="!appointment.cancelled && !appointment.cancelled_by_business && !appointment.cancelled_by_customer" variant="primary">{{appointment.service.duration}} mins</b-badge>
                      <b-badge v-if="appointment.cancelled_by_business" variant="danger">Business cancellation</b-badge>
                      <b-badge v-if="appointment.cancelled_by_customer" variant="warning">Customer cancellation</b-badge>
                    </b-col>
                  </b-row>
              <br>
              <p>
                Date: <b>{{ appointment.date }}</b>
              </p>
              <p>
                Time: <b> {{ appointment.start_time}} - {{ appointment.end_time}}</b>
              </p>
              <p>
                Price: <b> ${{ appointment.service.price }} </b>
              </p>
              
              <span  v-if="!appointment.cancelled">
              <hr>
              <b-button variant="warning" @click="cancelAppointment(appointment.id)">Cancel Appointment</b-button>
              </span>
          </b-card>
        </b-col>
      </b-row>
    
      <b-row>
      <h3 style="margin: 36px auto">Your Cancelled Appointments</h3>
      </b-row>
      <hr>
          <b-row style="margin-bottom: 16px;" v-for="appointment in cancellations" v-bind:key="appointment.id">
          <b-col style="max-width: 500px; margin: 0px auto;">
          <b-card 
              bg-variant="secondary" text-variant="white" 
              :header="appointment.date"
            >
                  <b-row>
                      <b-col>
                       <b-card-title>{{appointment.service.name}}</b-card-title>
                       <p style="color:#fff" >{{appointment.service.description}}</p>
                      </b-col>
                  
                      <b-col style="text-align: right">
                      <b-badge v-if="!appointment.cancelled && !appointment.cancelled_by_business && !appointment.cancelled_by_customer" variant="primary">{{appointment.service.duration}} mins</b-badge>
                      <b-badge v-if="appointment.cancelled_by_business" variant="danger">Business cancellation</b-badge>
                      <b-badge v-if="appointment.cancelled_by_customer" variant="warning">Customer cancellation</b-badge>
                    </b-col>
                  </b-row>
              <br>
              <p>
                Date: <b>{{ appointment.date }}</b>
              </p>
              <p>
                Time: <b> {{ appointment.start_time}} - {{ appointment.end_time}}</b>
              </p>
              <p>
                Price: <b> ${{ appointment.service.price }} </b>
              </p>
              
              <span  v-if="!appointment.cancelled">
              <hr>
              <b-button variant="warning" @click="cancelAppointment(appointment.id)">Cancel Appointment</b-button>
              </span>
          </b-card>
        </b-col>
      </b-row>
</div>
</template>

<script>
import { getCustomerAppointments, cancelCustomerAppointment } from '../api/api'

export default {
  name: 'CustomerAppointmentsPage',
  data: function() {
    return {
      appointments: [],
      cancellations: []
    }
  },
  mounted: async function() {
  this.getAppointments();
  },
  
  methods: {
    getAppointments: async function() {
        try {
          let res = await getCustomerAppointments()
          console.log(res)
          this.appointments = res.filter(appt => !appt.cancelled);
          this.cancellations = res.filter(appt => appt.cancelled);
        } catch(e) {
          console.log(e)
        }
      },
    async cancelAppointment(appointmentId) {
      var result = confirm("Are you sure you want to cancel this appointment?");
        if (result) {
          try {
            const res = await cancelCustomerAppointment(appointmentId)
            console.log(res)
            this.getAppointments();
          } catch (error) {
            alert(error)
            console.log(error)
          }
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