<template>
  <b-card
    v-bind:title="business.business_name"
    img-src="https://picsum.photos/600/300/?image=25"
    class="card"
  >
    <b-card-text>
      <div>
        {{ business.short_description }}
      </div>
      <div>
        <b-button size="sm" variant="primary" href="/?#/search-listings">View</b-button>
      </div>
    </b-card-text>
    <template v-slot:footer>
      <small class="text-muted">Business type might go here</small>
    </template>
  </b-card>
</template>

<script>
export default {
  name: 'BusinessComponent',
  props: ['business'],

}
</script>

<style scoped>
  .card {
    /* width: 18rem; */
    /* height: 18rem; */
  }
</style>