<template>
  <div>
    <b-card
      title=  "New Listing"
    >
      <b-form>
        <b-form-group
          id="input-group-1"
          label="Title: "
          label-for="input-1"
        >
          <b-form-input
            id="input-1"
            type="email"
            required
            placeholder="Title"
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="input-group-1"
          label="Description: "
          label-for="input-1"
        >
          <b-form-textarea
            id="input-1"
            type="email"
            required
            placeholder="Description of listing"
          ></b-form-textarea>
        </b-form-group>


        <b-form-group
          id="input-group-1"
          label="Services: "
          label-for="input-1"
        >
          <b-form-input
            id="input-1"
            type="email"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="input-group-1"
          label="Members: "
          label-for="input-1"
        >
          <b-form-input
            id="input-1"
            type="email"
            required
          ></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="submit" variant="outline">cancel</b-button>

      </b-form>

    </b-card>

  </div>
</template>

<script>
export default {
  name: 'NewListingPage'
}
</script>

<style scoped>

</style>