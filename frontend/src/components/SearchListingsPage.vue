<template>
  <b-container fluid>

    <hr class="my-3">

    <b-row>
      <b-col col style="text-align: left">
        <h1><strong>Business Name</strong></h1>
        <p>Address, number, city, province, ZIP<br>
        Contact information<br>
        Email<br>
        Phone number</p>
      </b-col>
    </b-row>

    <hr class="my-3">

    <b-row>
      <b-col cols="10" style="text-align: left; ">
        <h1><strong>Services</strong></h1>

        <b-list-group>
          <b-list-group-item>
            <b-row align-v="center">
              <b-col cols="8">
                <strong>Service 1</strong><br>30 min details
              </b-col>
              <b-col cols="2" style="font-size: 1.5rem;">
                <strong>$20</strong>
              </b-col>
              <b-col cols="2">
                <b-button>Book</b-button>
              </b-col>
            </b-row>
          </b-list-group-item>
          <b-list-group-item>
            <b-row align-v="center">
              <b-col cols="8">
                <strong>Service 2</strong><br>30 min details
              </b-col>
              <b-col cols="2" style="font-size: 1.5rem;">
                <strong>$25</strong>
              </b-col>
              <b-col cols="2">
                <b-button>Book</b-button>
              </b-col>
            </b-row>
          </b-list-group-item>
          <b-list-group-item>
            <b-row align-v="center">
              <b-col cols="8">
                <strong>Service 3</strong><br>30 min details
              </b-col>
              <b-col cols="2" style="font-size: 1.5rem;">
                <strong>$30</strong>
              </b-col>
              <b-col cols="2">
                <b-button>Book</b-button>
              </b-col>
            </b-row>
          </b-list-group-item>
        </b-list-group>
      </b-col>
    </b-row>


  </b-container>
</template>

<script>
export default {
  name: 'SearchListingsPage'
}
</script>

<style scoped>

</style>