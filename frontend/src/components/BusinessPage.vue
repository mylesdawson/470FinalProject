<template>
  <div>
  
      <b-card bg-variant="light">
        <b-form-group
        label-cols-lg="3"
        label="Main information"
        label-size="lg"
        label-class="font-weight-bold pt-0"
        class="mb-0"
        >
        <b-form-group
          label-cols-sm="3"
          label="Name:"
          label-align-sm="right"
        >
          <b-form-input type="text" v-model="main.business_name" ></b-form-input>
        </b-form-group>

        <b-form-group
          label-cols-sm="3"
          label="Contact number:"
          label-align-sm="right"
        >
          <b-form-input type="telephone" v-model="main.phone_number"></b-form-input>
        </b-form-group>

        <b-form-group
          label-cols-sm="3"
          label="Contact e-mail:"
          label-align-sm="right"
        >
          <b-form-input type="email" v-model="main.contact_email"></b-form-input>
        </b-form-group>

        <b-form-group
          label-cols-sm="3"
          label="Category:"
          label-align-sm="right"
        >
          <b-form-select v-model="main.category" :options="categories"></b-form-select>
        </b-form-group>
        
        <b-form-group
          label-cols-sm="3"
          label="Short description:"
          label-align-sm="right"
        >
         <b-form-textarea
          v-model="main.short_description"
          rows="3"></b-form-textarea>
        </b-form-group>

         <b-form-group
          label-cols-sm="3"
          label="Long description:"
          label-align-sm="right"
        >
         <b-form-textarea
          v-model="main.long_description"
          rows="5"></b-form-textarea>
        </b-form-group>

          <b-button type="submit" variant="primary" v-on:click="">Save</b-button>
          <b-button variant="outline" v-on:click="">Cancel</b-button>

          </b-form-group>
      </b-form-group>
  </b-card>
  <br>

    <b-card bg-variant="light">
        <b-form-group
        label-cols-lg="3"
        label="Location information"
        label-size="lg"
        label-class="font-weight-bold pt-0"
        class="mb-0"
        >
        <b-form-group
          label-cols-sm="3"
          label="Address:"
          label-align-sm="right"
        >
          <b-form-input type="text" v-model="location.address" ></b-form-input>
        </b-form-group>

        <b-form-group
          label-cols-sm="3"
          label="City:"
          label-align-sm="right"
        >
          <b-form-input v-model="location.city"></b-form-input>
        </b-form-group>

        <b-form-group
          label-cols-sm="3"
          label="Province | State:"
          label-align-sm="right"
        >
          <b-form-input v-model="location.province"></b-form-input>
        </b-form-group>

        <b-form-group
          label-cols-sm="3"
          label="Postal code:"
          label-align-sm="right"
        >
           <b-form-input v-model="location.postal_code"></b-form-input>
        </b-form-group>

          <b-button type="submit" variant="primary" v-on:click="">Save</b-button>
          <b-button variant="outline" v-on:click="">Cancel</b-button>

          </b-form-group>
      </b-form-group>
  </b-card>

   <br>


 <b-card title="Business hours" class="text-center" bg-variant="light">

 <hr>

    <b-card-group columns>
      <b-card header="Monday" class="text-center">
         <b-form-checkbox v-model="hours.monday_open" name="check-button" switch>
          <b>Open on Monday</b>
        </b-form-checkbox>
        <br>
        <b-row  style="justify-content: center">
         <b-col md="auto">
            <b-form-group label="Opening time">
              <b-time v-model="hours.monday_opening_time" locale="en" ></b-time>
            </b-form-group>
          </b-col>
          <b-col md="auto">
            <b-form-group label="Closing time">
                <b-time v-model="hours.monday_closing_time" locale="en" ></b-time>
              </b-form-group>
          </b-col>
        </b-row>
      </b-card>

      <b-card header="Tuesday" class="text-center">
         <b-form-checkbox v-model="hours.tuesday_open" name="check-button" switch>
          <b>Open on Tuesday</b>
        </b-form-checkbox>
        <br>
        <b-row  style="justify-content: center">
         <b-col md="auto">
            <b-form-group label="Opening time">
              <b-time v-model="hours.tuesday_opening_time" locale="en" ></b-time>
            </b-form-group>
          </b-col>
          <b-col md="auto">
            <b-form-group label="Closing time">
                <b-time v-model="hours.tuesday_closing_time" locale="en" ></b-time>
              </b-form-group>
          </b-col>
        </b-row>
      </b-card>

       <b-card header="Wednesday" class="text-center">
         <b-form-checkbox v-model="hours.wednesday_open" name="check-button" switch>
          <b>Open on Wednesday</b>
        </b-form-checkbox>
        <br>
        <b-row  style="justify-content: center">
         <b-col md="auto">
            <b-form-group label="Opening time">
              <b-time v-model="hours.wednesday_opening_time" locale="en" ></b-time>
            </b-form-group>
          </b-col>
          <b-col md="auto">
            <b-form-group label="Closing time">
                <b-time v-model="hours.wednesday_closing_time" locale="en" ></b-time>
              </b-form-group>
          </b-col>
        </b-row>
      </b-card>

       <b-card header="Thursday" class="text-center">
         <b-form-checkbox v-model="hours.thursday_open" name="check-button" switch>
          <b>Open on Thursday</b>
        </b-form-checkbox>
        <br>
        <b-row  style="justify-content: center">
         <b-col md="auto">
            <b-form-group label="Opening time">
              <b-time v-model="hours.thursday_opening_time" locale="en" ></b-time>
            </b-form-group>
          </b-col>
          <b-col md="auto">
            <b-form-group label="Closing time">
                <b-time v-model="hours.thursday_closing_time" locale="en" ></b-time>
              </b-form-group>
          </b-col>
        </b-row>
      </b-card>

          <b-card header="Friday" class="text-center">
         <b-form-checkbox v-model="hours.friday_open" name="check-button" switch>
          <b>Open on Friday</b>
        </b-form-checkbox>
        <br>
        <b-row  style="justify-content: center">
         <b-col md="auto">
            <b-form-group label="Opening time">
              <b-time v-model="hours.friday_opening_time" locale="en" ></b-time>
            </b-form-group>
          </b-col>
          <b-col md="auto">
            <b-form-group label="Closing time">
                <b-time v-model="hours.friday_closing_time" locale="en" ></b-time>
              </b-form-group>
          </b-col>
        </b-row>
      </b-card>

       <b-card header="Saturday" class="text-center">
         <b-form-checkbox v-model="hours.saturday_open" name="check-button" switch>
          <b>Open on Saturday</b>
        </b-form-checkbox>
        <br>
        <b-row  style="justify-content: center">
         <b-col md="auto">
            <b-form-group label="Opening time">
              <b-time v-model="hours.saturday_opening_time" locale="en" ></b-time>
            </b-form-group>
          </b-col>
          <b-col md="auto">
            <b-form-group label="Closing time">
                <b-time v-model="hours.saturday_closing_time" locale="en" ></b-time>
              </b-form-group>
          </b-col>
        </b-row>
      </b-card>

        <b-card header="Sunday" class="text-center">
         <b-form-checkbox v-model="hours.sunday_open" name="check-button" switch>
          <b>Open on Sunday</b>
        </b-form-checkbox>
        <br>
        <b-row  style="justify-content: center">
         <b-col md="auto">
            <b-form-group label="Opening time">
              <b-time v-model="hours.sunday_opening_time" locale="en" ></b-time>
            </b-form-group>
          </b-col>
          <b-col md="auto">
            <b-form-group label="Closing time">
                <b-time v-model="hours.sunday_closing_time" locale="en" ></b-time>
              </b-form-group>
          </b-col>
        </b-row>
      </b-card>
 </b-card-group>

  <b-button type="submit" variant="primary" v-on:click="">Save</b-button>
  <b-button variant="outline" v-on:click="">Cancel</b-button>

  </b-card>
    
  </div>
</template>




<script>
  import {getBusiness} from '../api/services.js'
  export default {
     name: 'BusinessPage',
     data: function() {
      return {
         business: {},
         categories: [
            { value: 'all', text: 'All' },
            { value: 'fitness', text: 'Fitness' },
            { value: 'wellness', text: 'Wellness' },
            { value: 'beauty', text: 'Beauty' },
            { value: 'miscellaneous', text: 'Miscellaneous' }
         ],
         main: {
           business_name: '',
           category: '',
           contact_email: '',
           long_description: '',
           phone_number: '',
           short_description:'',
         },
         location: {
           address: '',
           city: '',
           province: '',
           postal_code: '',
         },
         hours: {
           monday_open: true,
           tuesday_open: true,
           wednesday_open: true,
           thursday_open: true,
           friday_open: true,
           saturday_open: false,
           sunday_open: false,

           monday_opening_time: '',
           monday_closing_time: '',

           tuesday_opening_time: '',
           tuesday_closing_time: '',

           wednesday_opening_time: '',
           wednesday_closing_time: '',

           thursday_opening_time: '',
           thursday_closing_time: '',

           friday_opening_time: '',
           friday_closing_time: '',

           saturday_opening_time: '',
           saturday_closing_time: '',

           sunday_opening_time: '',
           sunday_closing_time: '',
         }
      } 
    },
    mounted() {
     this.getBusiness();
    },
    methods: {
      showEdit: function(item, index) {
        console.log(item)
        this.$modal.show('serviceEdit');
      },
      showCreate: function() {
          this.$modal.show('serviceCreate');
      },
      hideAll: function() {
          this.$modal.hide('serviceCreate');
          this.$modal.hide('serviceEdit');
      },
      getBusiness: async function() {
        try {
            const res = await getBusiness();
            this.business = res;
            this.matchModel();
          } catch (error) {
            console.log(error);
          }
      },
      matchModel: function() {
        this.main.business_name = this.business.business_name;
        this.main.category = this.business.category;
        this.main.contact_email = this.business.contact_email;
        this.main.long_description = this.business.long_description;
        this.main.phone_number = this.business.phone_number;
        this.main.short_description = this.business.short_description;
        
        this.location.address = this.business.address;
        this.location.city = this.business.city;
        this.location.province = this.business.province;
        this.location.postal_code = this.business.postal_code;

        this.hours.monday_open = this.business.monday_open;
        this.hours.tuesday_open = this.business.tuesday_open;
        this.hours.wednesday_open = this.business.wednesday_open;
        this.hours.thursday_open = this.business.thursday_open;
        this.hours.friday_open = this.business.friday_open;
        this.hours.saturday_open = this.business.saturday_open;
        this.hours.sunday_open = this.business.sunday_open;

        this.hours.monday_opening_time = this.business.monday_opening_time;
        this.hours.monday_closing_time = this.business.monday_closing_time;

        this.hours.tuesday_opening_time = this.business.tuesday_opening_time;
        this.hours.tuesday_closing_time = this.business.tuesday_closing_time;

        this.hours.wednesday_opening_time = this.business.wednesday_opening_time;
        this.hours.wednesday_closing_time = this.business.wednesday_closing_time;

        this.hours.thursday_opening_time = this.business.thursday_opening_time;
        this.hours.thursday_closing_time = this.business.thursday_closing_time;

        this.hours.friday_opening_time = this.business.friday_opening_time;
        this.hours.friday_closing_time = this.business.friday_closing_time;

        this.hours.saturday_opening_time = this.business.saturday_opening_time;
        this.hours.saturday_closing_time = this.business.saturday_closing_time;

        this.hours.sunday_opening_time = this.business.sunday_opening_time;
        this.hours.sunday_closing_time = this.business.sunday_closing_time;

      },
      
      
    }
  
  }
</script>

<style scoped>

</style>