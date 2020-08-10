<template>
  <b-container fluid>

    <hr class="my-3">

    <b-row>
      <b-col col style="text-align: left">
        <div>
          <h1 style="margin-bottom: 0"><strong>{{ business_info.business_name }}</strong></h1>
          <p style="margin-bottom: 0.5rem;">{{ business_info.address }}, {{ business_info.city }}, {{ business_info.province }}, {{ business_info.postal_code }}</p>
          <p>{{ business_info.long_description }}</p>
        </div>

        <div style="margin-top: 1rem;">
          <h4>Contact</h4>
          <p>
            Email: {{ business_info.contact_email }}<br>
            Phone: {{ business_info.phone_number }}
          </p>
        </div>
      </b-col>
    </b-row>

    <hr class="my-3">

    <b-row>
      <b-col cols="10" style="text-align: left; ">
        <h1><strong>Services</strong></h1>

        <b-list-group>
          <service-component
            v-for="business_service in business_services"
            v-bind:key="business_service.id"
            v-bind:service="business_service"
          ></service-component>
        </b-list-group>
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
      business_services: []
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
    }
  }
}
</script>

<style scoped>

</style>