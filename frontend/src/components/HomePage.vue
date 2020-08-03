<template>
  <b-container fluid>
    <b-row>
<!-- FIRST COLUMN (APPOINTMENTS TABLE) -->
        <b-col cols="12" lg="6"> 
            <b-card>
              <b-row>
                    <b-col>
                    <h3>Appointments</h3>
                    </b-col>
                  <b-col>
                    <b-input-group>
                        <b-input-group-prepend is-text>
                        <b-icon icon="search"></b-icon>
                        </b-input-group-prepend>
                        <b-form-input placeholder="Search appointments"></b-form-input>
                    </b-input-group>
                  </b-col>
              </b-row>

              <br>
              
              <b-table striped hover :items="apps.appointments"></b-table>
            </b-card>
        </b-col>

<!-- SECOND COLUMN (CALENDAR) -->
    <b-col cols="12" lg="6">
           <b-card no-body>
            <b-card-header>
            <b-row >
                  <b-col>
                    <b-dropdown  text="Select Team Calendar" variant="success" >
                      <b-dropdown-item href="#">Action</b-dropdown-item>
                      <b-dropdown-item href="#">Another action</b-dropdown-item>
                      <b-dropdown-item href="#">Something else here</b-dropdown-item>
                    </b-dropdown>
                  </b-col>
                  <b-col style="text-align: right">
                    <b-button variant="primary"  to="/calendar">Go to calendar</b-button>
                </b-col>
            </b-row>
            </b-card-header>
            <b-card-body>
            <full-calendar :config="config" :events="events"/>
            </b-card-body>
            </b-card>
          

            
      
    </b-col>
  </b-row>
</b-container>

</template>

<script>
  import moment from 'moment'
  import appointments from '../api/home.js'
 
  export default {
   
    data () {
      return {
          apps: appointments.data(),
          events: [
            {
              title: 'test',
              allDay: true,
              start: moment(),
              end: moment().add(1, 'd'),
            },
            {
              title: 'another test',
              start: moment().add(2,'d'),
              end: moment().add(2, 'd').add(2, 'h'),
            },
          ],
          config: {
            defaultView: 'month',
            eventRender: function(event, element) {
              console.log(event)
            }
          },
        }
    }
    
  
  }
</script>

<style scoped>

</style>