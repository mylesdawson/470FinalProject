<template>
<div>
    <b-card no-body bg-variant="light">
      <b-card-body>
        <full-calendar :config="config" :events="appointments"/>
      </b-card-body>
    </b-card>

<!-- DISPLAY MODAL -->
<template>
    <modal name="eventDisplay"
          :width="800"
          :height="800"
          :adaptive="true" >
           <b-card no-body style="border: none" :title="selectedDateFormatted">
            <b-card-header>
            <b-row>
                    <b-col >
                    <h3>{{selectedDateFormatted}}</h3>
                    </b-col>
                 
                  
              </b-row>
            </b-card-header>
            <b-card-body>
            <h4> Events </h4>
             <b-list-group>

                <b-list-group-item 
                 v-for="(item, index) in appointmentsByDay"
                 :key="index"
                 >
                 <b-row>
                    <b-col>
                    <h5 >{{item.service.name}}</h5>
                    </b-col>
                 
                      <b-col style="text-align: right">
                      <b-badge v-if="!item.cancelled && !item.cancelled_by_business && !item.cancelled_by_customer" variant="primary">{{item.service.duration}} mins</b-badge>
                      <b-badge v-if="item.cancelled || item.cancelled_by_business" variant="warning">Cancelled</b-badge>
                      <b-badge v-if="item.cancelled_by_customer" variant="danger">Customer cancelled</b-badge>
                    </b-col>
                  </b-row>
                 
                  <b-row>
                    <b-col sm> <b>{{item.service.description}}</b></b-col>
                    <b-col sm>Price: <b>$ {{item.service.price}} </b></b-col>
                    <b-col sm>Customer: <b>{{item.customer.user.username}}</b></b-col>
                  </b-row>
              
                  <small>{{item.start_time}} - {{item.end_time}}</small>
                  
                  <div style="margin-top: 8px;">
                    <b-button variant="outline-danger"
                    v-if="!item.cancelled && !item.cancelled_by_business && !item.cancelled_by_customer"
                    v-on:click="onCancelSelectedAppointment(item)" >
                    Cancel appointment
                    </b-button>
                  </div>

                </b-list-group-item>
              </b-list-group>

            </b-card-body>
            </b-card>
    </modal>
</template>


</div>

</template>

<script>
  import {getAppointments, getAppointmentsByDay, onCancelAppointment} from '../api/events.js'
  import moment from 'moment'
 
  export default {
    name: 'CalendarPage',
    methods: {
        showDisplay: function() {
           this.hideAll();
           return this.$modal.show('eventDisplay');
        },
        hideAll: function() {
            this.$modal.hide('eventDisplay');
        },
        getAppointments: async function() {
          try {
              const res = await getAppointments();
              this.appointments = res;
            } catch (error) {
              console.log(error);
            }
        },
        getAppointmentsByDay: async function(dateObj) {
            try {
                const res = await getAppointmentsByDay(dateObj);
                this.appointmentsByDay = res;
                console.log(this.appointmentsByDay)
                
              } catch (error) {
                console.log(error);
              }
        },
        onCancelAppointment: async function(app_id) {
            try {
                const res = await onCancelAppointment(app_id);
                this.getAppointmentsByDay(this.selectedDateObj);
              } catch (error) {
                console.log(error);
              }
        },
        onCancelSelectedAppointment: function(item) {
          console.log("item", item)
          this.selectedAppointment = item;
          var result = confirm(`Are you sure you want to cancel\nthe ${item.service.name} appointment \nfrom ${item.start_time}-${item.end_time}?`);
            if (result) {
                this.onCancelAppointment(item.id); 
            }
        },
        
          
    },
    mounted() {
     this.getAppointments();
    },
    data: function() {
      return {
          selectedDateObj: null,
          selectedDateFormatted: null,
          appointmentsByDay: [],
          appointments: [],
          config: {
            weekends: true,
            selectable: true,
            defaultView: 'month',
            eventRender: function(event, element) {
              console.log(event)
            },
            eventClick: function(date) {
              console.log(moment(date.start).toObject())
              this.selectedDateObj = moment(date.start).toObject();
              this.selectedDateFormatted = moment(date.start).format('ddd MMM DD, YYYY');
              this.getAppointmentsByDay(this.selectedDateObj);
              this.showDisplay();
            }.bind(this),
            select: function(date) {
              this.selectedDateObj = moment(date).toObject();
              this.selectedDateFormatted = moment(date).format('ddd MMM DD, YYYY');
              this.getAppointmentsByDay(this.selectedDateObj);
              this.showDisplay();
            }.bind(this),
            businessHours: {
                daysOfWeek: [ 1, 2, 3, 4, 5 ], // Monday - Thursday
                startTime: '9:00', // a start time (9am in this example)
                endTime: '17:00', // an end time (5pm in this example)
            }
          },
        }
    },
  }
</script>

<style scoped>

</style>