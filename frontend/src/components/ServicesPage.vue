<template>
<div>

<!-- FIRST COLUMN (SERVICES TABLE) -->
        
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
                  <b-button v-on:click="showCreate">
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
             <b-form-spinbutton
              wrap
              min="0"
              max="180"
              step="5"
              v-model="newService.duration">
            </b-form-spinbutton>
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
                    <b-button variant="outline-danger" v-on:click="deleteService">
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
            v-model="selectedItem.name"
            placeholder="Service name"></b-form-input>
        </b-form-group>

        <b-form-group
          label="Description">
          <b-form-textarea
            v-model="selectedItem.description"
            placeholder="Service description"></b-form-textarea>
        </b-form-group>


        <b-form-group
          label="Price $">
          <b-form-spinbutton
              min="0"
              max="100000"
              step="0.25"
              v-model="selectedItem.price">
            </b-form-spinbutton>
           
        </b-form-group>

        <b-form-group
          label="Duration (minutes)">
             <b-form-spinbutton
              wrap
              min="0"
              max="180"
              step="5"
              v-model="selectedItem.duration">
            </b-form-spinbutton>
        </b-form-group>

        <b-button type="submit" variant="primary" v-on:click="saveEditedService">Save</b-button>
        <b-button variant="outline" v-on:click="hideAll">Cancel</b-button>

      </b-form>
        </b-card-body>
      </b-card>
    </modal>
</template>
</div>

</template>



<script>
 import {getServices, createService, editService} from '../api/services.js'
  export default {
   
     data: function() {
      return {
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
         services: []
      } 
    },
    mounted() {
     this.getServices();
    },
    methods: {
      showEdit: function(item, index) {
          const body = {name: item.name, description: item.description, price: Number(item.price), duration: item.duration};
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
          try {
            const res = await createService(this.newService);
            //reload data
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
      saveEditedService: async function() {
        console.log(this.selectedItem);
        try {
          const res = await editService(this.selectedItem);
          //reload data
          this.hideAll();
        } catch (error) {
          console.log(error);
        }
      },
      deleteService: function() {
          var result = confirm("Are you sure you want to delete this service?");
          if (result) {
              // delete logic
              // reload data
              this.hideAll();
          }
      }
      
    }
  
  }
</script>

<style scoped>

</style>