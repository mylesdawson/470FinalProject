<template>
<div>
    <b-card no-body>
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
                 
                  <b-col style="text-align: right">
                  <b-button variant="success" v-on:click="showCreate">
                    Add Event
                  </b-button>
                </b-col>
              </b-row>
            </b-card-header>
            <b-card-body>
            <h4> Events </h4>
             <b-list-group>
                <b-list-group-item button class="flex-column align-items-start" v-on:click="showEdit">
                  <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">List group item heading</h5>
                    <small>3 days ago</small>
                  </div>

                  <p class="mb-1">
                    Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.
                  </p>

                  <small>Donec id elit non mi porta.</small>
                </b-list-group-item>
              </b-list-group>

             
            </b-card-body>
            </b-card>
    </modal>
</template>


<!-- EDIT MODAL -->
<template>
    <modal name="eventEdit"
          :width="800"
          :height="800"
          :adaptive="true" >
           <b-card no-body style="border: none" :title="selectedDateFormatted">
            <b-card-header>
            <b-row>
                    <b-col >
                    <h3>Edit Event </h3>
                    </b-col>
                 
                  <b-col style="text-align: right">
                  <b-button variant="danger" style="margin-right: 80px" v-on:click="hideAll">
                      Delete
                  </b-button>
                  <b-button variant="outline-secondary" v-on:click="hideAll">
                      Cancel
                  </b-button>
                  <b-button variant="success">
                    Save
                  </b-button>
                </b-col>
              </b-row>
            </b-card-header>
            <b-card-body>
           
            <b-form>
              <b-form-group
                id="input-group-1"
                label="Title: "
                label-for="input-1">
                <b-form-input
                  id="input-1"
                  type="email"
                  required
                  placeholder="Title"></b-form-input>
              </b-form-group>

              <b-form-group
                id="input-group-1"
                label="Description: "
                label-for="input-1">
                <b-form-textarea
                  id="input-1"
                  type="email"
                  required
                  placeholder="Description of listing"></b-form-textarea>
              </b-form-group>

              <b-form-group
                id="input-group-1"
                label="Services: "
                label-for="input-1">
                <b-form-input
                  id="input-1"
                  type="email"
                  required></b-form-input>
              </b-form-group>

              <b-form-group
                id="input-group-1"
                label="Members: "
                label-for="input-1">
                <b-form-input
                  id="input-1"
                  type="email"
                  required></b-form-input>
              </b-form-group>

           </b-form>
        </b-card-body>
      </b-card>
    </modal>
</template>


<!-- CREATE MODAL -->
<template>
    <modal name="eventCreate"
          :width="800"
          :height="800"
          :adaptive="true" >
           <b-card no-body style="border: none" :title="selectedDateFormatted">
            <b-card-header>
            <b-row>
                    <b-col >
                    <h3>New Event </h3>
                    </b-col>
                 
                  <b-col style="text-align: right">
                  <b-button variant="outline-secondary" v-on:click="hideAll">
                      Cancel
                  </b-button>
                  <b-button variant="success">
                    Save
                  </b-button>
                </b-col>
              </b-row>
            </b-card-header>
            <b-card-body>
           
            <b-form>
              <b-form-group
                id="input-group-1"
                label="Title: "
                label-for="input-1">
                <b-form-input
                  id="input-1"
                  type="email"
                  required
                  placeholder="Title"></b-form-input>
              </b-form-group>

              <b-form-group
                id="input-group-1"
                label="Description: "
                label-for="input-1">
                <b-form-textarea
                  id="input-1"
                  type="email"
                  required
                  placeholder="Description of listing"></b-form-textarea>
              </b-form-group>

              <b-form-group
                id="input-group-1"
                label="Services: "
                label-for="input-1">
                <b-form-input
                  id="input-1"
                  type="email"
                  required></b-form-input>
              </b-form-group>

              <b-form-group
                id="input-group-1"
                label="Members: "
                label-for="input-1">
                <b-form-input
                  id="input-1"
                  type="email"
                  required></b-form-input>
              </b-form-group>

           </b-form>
        </b-card-body>
      </b-card>
    </modal>
</template>

</div>

</template>

<script>
  import {getAppointments, getAppointmentsByDay} from '../api/events.js'
  import moment from 'moment'
 
  export default {
    name: 'CalendarPage',
    methods: {
        showDisplay: function() {
           this.hideAll();
           return this.$modal.show('eventDisplay');
        },
        showEdit: function() {
            this.hideAll();
            return this.$modal.show('eventEdit');
        },
        showCreate: function() {
            this.hideAll();
            return this.$modal.show('eventCreate');
        },
        hideAll: function() {
            this.$modal.hide('eventDisplay');
            this.$modal.hide('eventEdit');
            this.$modal.hide('eventCreate');
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
            } catch (error) {
              console.log(error);
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
            eventClick: function(info) {
              console.log(info)
            }.bind(this),
            select: function(date) {
              this.selectedDateObj = moment(date).toObject();
              this.selectedDateFormatted = moment(date).format('ddd MMM DD, YYYY');
              this.getAppointmentsByDay(this.selectedDateObj);
              this.showDisplay();
            }.bind(this),
            businessHours: {
                // days of week. an array of zero-based day of week integers (0=Sunday)
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