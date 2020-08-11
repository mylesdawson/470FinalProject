<template>
  <b-container fluid class="no-top-margin">
        <div>
          <h1 style="border-radius: 20px; padding: 16px 0px;" v-bind:class="business_info.category"><strong>{{ business_info.business_name }}</strong></h1>
        </div>
    <b-row>
      <b-col>
        <b-card title="Information">
        <hr>
          <div class="info-div">
            <h5>
              <b-icon-clock v-bind:class="business_info.category">
              </b-icon-clock>
              Hours of Operation
            </h5>
            <p>Closed: {{ closed_days }}</p>
            <p>
              Open: {{ open_hours }}
            </p>
          </div>

          <div class="info-div">
            <h5>
              <b-icon-map v-bind:class="business_info.category">
              </b-icon-map>
              Location
            </h5>
            <p>
              {{ business_info.address }}, {{ business_info.city }}, {{ business_info.province }}, {{ business_info.postal_code }}
            </p>
          </div>

          <div class="info-div">
            <h5>
              <b-icon-info-circle v-bind:class="business_info.category">
              </b-icon-info-circle>
              About
            </h5>
            <p>{{ business_info.long_description }}</p>
          </div>

          <div class="info-div">
            <h5>
              <b-icon-telephone v-bind:class="business_info.category">
              </b-icon-telephone>
              Contact
            </h5>
            <p>
              Email: {{ business_info.contact_email }}<br>
              Phone: {{ business_info.phone_number }}
            </p>
          </div>
        </b-card>
      </b-col>
      
          <b-col style="text-align: left; " class="services-section">
          <b-card title="Services">
            <hr>
                   

                    <b-list-group>
                      <service-component
                        v-for="business_service in business_services"
                        v-bind:key="business_service.id"
                        v-bind:service="business_service"
                        v-bind:businessId="business_info.id"
                      ></service-component>
                    </b-list-group>
                    </b-card>
          </b-col>
    </b-row>

  </b-container>
</template>

<script>
import ServiceComponent from './ServiceComponent'
import { getBusinessInfo, getServicesByBusiness } from '../api/api'

export default {
  name: 'SearchListingsPage',
  components: {
    ServiceComponent
  },
  data: function() {
    return {
      business_info: {},
      business_services: [],
      open_days: null,
      closed_days: null,
      open_hours: null,
    }
  },
  mounted: async function() {
    const params = this.$route.params
    if (params.id) {
      // this should be in try/catch block...
      const businessInfo = await getBusinessInfo(params.id)
      console.log(businessInfo)
      this.business_info = businessInfo

      const businessServices = await getServicesByBusiness(params.id)
      this.business_services = businessServices
      console.log(businessServices)

      const days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

      const closed = days.filter(day => this.business_info[day + "_open"] === false)
      const open = days.filter(day => this.business_info[day + "_open"] === true)

      this.closed_days = closed.join(", ")
      this.open_days = open

      // for now we assume that each day has same opening and closing hours
      const firstOpenDay = days.find(day => this.business_info[day + "_open"] === true)
      this.open_hours = this.business_info[`${firstOpenDay}_opening_time`] + " - " + this.business_info[`${firstOpenDay}_closing_time`]
    }
  }
}
</script>

<style scoped>
  h1 {
    text-align: center;
    padding: .5rem;
  }
  p {
    margin-bottom: 0;
  }
  .info-div {
    margin-top: 1rem;
  }
  .services-section {
    margin: 0 auto;
  }
  .fitness {
    color: #3471eb;
  }
  .wellness {
    color: #169e1f;
  }
  .beauty {
    color: #e8ba00;
  }

  h1.fitness {
    color: white;
    background-color: #3471eb;
  }
  h1.wellness {
    color: white;

    background-color: #169e1f;
  }
  h1.beauty {
    color: black;
    background-color: #e8ba00;
  }

  .no-top-margin {
    margin-top: 0;
  }
</style>