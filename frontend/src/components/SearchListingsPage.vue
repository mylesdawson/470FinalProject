<template>
  <b-container fluid>

    <hr class="my-3">

    <b-row>
      <b-col col style="text-align: left">
        <h1><strong>{{ business_info.business_name }}</strong></h1>
        <div>
          <span>{{ business_info.city }} </span>
          <span>{{ business_info.province }} </span>
          <span>{{ business_info.address }} </span>
          <span>{{ business_info.postal_code }} </span>
          <span></span>
        </div>

        <h4>Contact information</h4>
        <p>{{ business_info.contact_email }}</p>
        <p>{{ business_info.phone_number }}</p>
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