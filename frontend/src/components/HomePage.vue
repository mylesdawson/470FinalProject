<template>
  <b-container fluid>
    <b-row>
<!-- FIRST COLUMN (APPOINTMENTS TABLE) -->
        <b-col cols="12" lg="6"> 
            <b-card >
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

            <hr>

            <b-row>
                <b-col>
                Service
                </b-col>
                <b-col>
                Member
                </b-col>
                <b-col>
                Time
                </b-col>
                <b-col>
                Date
                </b-col>
            </b-row>

            <hr>

            <b-row v-for="(appointment, index) in appointments">
                <b-col>
                {{appointment.service}}
                </b-col>
                <b-col>
                 {{appointment.member}}
                </b-col>
                <b-col>
                 {{appointment.time}}
                </b-col>
                <b-col>
                 {{appointment.date}}
                </b-col>
            </b-row>
            
            </b-card>
        </b-col>

<!-- SECOND COLUMN (CALENDAR) -->
    <b-col cols="12" lg="6">
            <b-card
            title="CALENDAR PLACEHOLDER"
            img-src="https://picsum.photos/600/300/?image=25"
            img-alt="Image"
            img-top
            tag="article"
           
            class="mb-2"
        >
            <b-card-text>
            Hopefully this will be a calendar soon
            </b-card-text>

            <b-button variant="primary">Go somewhere</b-button>
        </b-card>
    </b-col>
  </b-row>
</b-container>

</template>



<script>
 import appointments from '../api/home.js'
  export default {
   
    data () {
      return appointments.data();
      
    }
  
  }
</script>

<style scoped>

</style>