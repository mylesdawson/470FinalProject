<template>
<div>

<!-- FIRST COLUMN (SERVICES TABLE) -->
        
            <b-card bg-variant="light">
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
                  <b-button variant="primary" v-on:click="showCreate">
                    Add Service
                  </b-button>
                </b-col>
              </b-row>

              <br>
              
              <b-table 
                    responsive 
                    flex 
                    striped 
                    hover
                    :fields="fields"
                    :items="services"
                    @row-clicked="showEdit"
                    ></b-table>
            </b-card>
    



<template>
    <modal name="serviceCreate"
          :width="800"
          :height="800"
          :adaptive="true" >
           <b-card no-body style="border: none">
            <b-card-header>
            <b-row>
                    <b-col >
                    <h3>New service</h3>
                    </b-col>
                 
              </b-row>
            </b-card-header>
            <b-card-body>
           
             <b-form>
        <b-form-group
          label="Name">
          <b-form-input
            type="text"
            required
            v-model="newService.name"
            placeholder="Service name"></b-form-input>
        </b-form-group>

        <b-form-group
          label="Description">
          <b-form-textarea
            type="text"
            required
            v-model="newService.description"
            placeholder="Service description"></b-form-textarea>
        </b-form-group>


        <b-form-group
          label="Price $">
          <b-form-spinbutton
              min="0"
              max="100000"
              step="0.25"
              v-model="newService.price">
            </b-form-spinbutton>
           
        </b-form-group>

        <b-form-group
          label="Duration (minutes)">
            <b-form-select v-model="newService.duration" :options="timeOptions"></b-form-select>
        </b-form-group>

        <b-button type="submit" variant="primary" v-on:click="createService">Save</b-button>
        <b-button variant="outline" v-on:click="cancelCreation">Cancel</b-button>

      </b-form>
        </b-card-body>
      </b-card>
    </modal>
</template>


<template>
    <modal name="serviceEdit"
          :width="800"
          :height="800"
          :adaptive="true" >
           <b-card no-body style="border: none">
            <b-card-header>
            <b-row>
                    <b-col >
                    <h3>{{selectedItem.name}}</h3>
                    </b-col>
                 
                  <b-col style="text-align: right">
                    <b-button variant="danger" v-on:click="deleteService">
                      Delete
                    </b-button>
                </b-col>
              </b-row>
            </b-card-header>
            <b-card-body>
           
             <b-form>
        <b-form-group
          label="Name">
          <b-form-input
            disabled
            v-model="selectedItem.name"
            placeholder="Service name"></b-form-input>
        </b-form-group>

        <b-form-group
          label="Description">
          <b-form-textarea
             disabled
            v-model="selectedItem.description"
            placeholder="Service description"></b-form-textarea>
        </b-form-group>


        <b-form-group
          label="Price $">
          <b-form-spinbutton
          disabled
              min="0"
              max="100000"
              step="0.25"
              v-model="selectedItem.price">
            </b-form-spinbutton>
           
        </b-form-group>

        <b-form-group
          label="Duration (minutes)">
             <b-form-spinbutton
             disabled
              wrap
              min="0"
              max="180"
              step="5"
              v-model="selectedItem.duration">
            </b-form-spinbutton>
        </b-form-group>

        <b-button variant="primary" v-on:click="hideAll">Cancel</b-button>

      </b-form>
        </b-card-body>
      </b-card>
    </modal>
</template>
</div>

</template>



<script>
 import {getServices, createService, editService, deleteService} from '../api/services.js'
  export default {
   
     data: function() {
      return {
         fields: ['name', 'description', 'price', 'duration'],
         selectedItem: {
           name: '',
           description: '',
           price: 0,
           duration: 0,
         },
         newService: {
           name: '',
           description: '',
           price: 0,
           duration: 0,
         },
         services: [],
         timeOptions: [
          { value: 15, text: '15 mins' },
          { value: 30, text: '30 mins' },
          { value: 45, text: '45 mins' },
          { value: 60, text: '1:00 hour' },
          { value: 90, text: '1:30 hours' },
          { value: 120, text: '2:00 hours' },
          { value: 150, text: '2:30 hours' },
          { value: 180, text: '3:00 hours' }
        ]
      } 
    },
    mounted() {
     this.getServices();
    },
    methods: {
      showEdit: function(item, index) {
        console.log(item)
          const body = {id: item.id ,business: item.business,name: item.name, description: item.description, price: Number(item.price), duration: item.duration};
          this.selectedItem = body;
          this.$modal.show('serviceEdit');
      },
      showCreate: function() {
          this.$modal.show('serviceCreate');
      },
      hideAll: function() {
          this.$modal.hide('serviceCreate');
          this.$modal.hide('serviceEdit');
      },
      getServices: async function() {
        try {
            const res = await getServices();
            this.services = res;
          } catch (error) {
            console.log(error);
          }
      },
      createService: async function() {
          console.log(this.newService)
          // this.newService.price = String(this.newService.price);
          try {
            const res = await createService(this.newService);
            this.newService = {name: '', description: '', price: 0, duration: 0 };
            this.getServices();
            this.hideAll();
          } catch (error) {
            console.log(error);
          }
      },
      cancelCreation: function() {
          var result = confirm("Are you sure cancel creating this service?");
          if (result) {
              this.newService = {name: '', description: '', price: 0, duration: 0 };
              this.hideAll();
          }
      },
      deleteService: async function() {
          console.log(this.selectedItem)
          var result = confirm("Are you sure you want to delete this service?");
          if (result) {
              try {
                const res = await deleteService(this.selectedItem.id);
                this.getServices();
                //reload data
                this.hideAll();
              } catch (error) {
                console.log(error);
              }
              
          }
      }
      
    }
  
  }
</script>

<style scoped>

</style>