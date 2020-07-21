<template>
  <div>
    <b-card>
      <b-row>
        <b-col>
          <p>10 members</p>
        </b-col>
        <b-col>
          <b-input-group
            prepend="Search"
          >
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
  name: 'TeamPage',
}
</script>

<style scoped>

</style>