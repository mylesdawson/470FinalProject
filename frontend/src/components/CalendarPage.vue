<template>
  <div>
    <b-card>
      <b-row>
        <b-col>
          <h3>Members</h3>
        </b-col>
        <b-col>
          <b-input-group>
            <b-input-group-prepend is-text>
              <b-icon icon="search"></b-icon>
            </b-input-group-prepend>
            <b-form-input></b-form-input>
          </b-input-group>
        </b-col>
        <b-col>
          <b-button>
            Add Member
          </b-button>
        </b-col>
      </b-row>

      <hr>

      <b-row>
        <b-col>
          Members
        </b-col>
        <b-col>
          Username
        </b-col>
        <b-col>
          Email
        </b-col>
      </b-row>

      <hr>

      <!-- For loop over members of signed-in org -->
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'CalendarPage',
}
</script>

<style scoped>

</style>