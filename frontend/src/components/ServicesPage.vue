<template>
  <b-container fluid>
    <b-row>
<!-- FIRST COLUMN (SERVICES TABLE) -->
        <b-col cols="12" lg="8"> 
            <b-card>
              <b-row>
                    <b-col cols="12" md="3">
                    <h3>Services</h3>
                    </b-col>
                  <b-col cols="9" md="6">
                    <b-input-group>
                        <b-input-group-prepend is-text>
                        <b-icon icon="search"></b-icon>
                        </b-input-group-prepend>
                        <b-form-input placeholder="Search services"></b-form-input>
                    </b-input-group>
                  </b-col>
                  <b-col cols="3" md="3" style="text-align: right">
                  <b-button >
                    Add Service
                  </b-button>
                </b-col>
              </b-row>

              <br>
              
              <b-table striped hover :items="services"></b-table>
            </b-card>
        </b-col>

<!-- SECOND COLUMN (SERVICE) -->
    <b-col cols="12" lg="4">
            <b-card
      title=  "Service">
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

        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="submit" variant="outline">cancel</b-button>

      </b-form>
       </b-card>
    </b-col>
  </b-row>
</b-container>

</template>



<script>
 import services from '../api/services.js'
  export default {
   
    data () {
      return services.data();
      
    }
  
  }
</script>

<style scoped>

</style>