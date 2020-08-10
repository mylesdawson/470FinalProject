<template>
  <b-card
    v-bind:title="business.business_name"
    img-src="https://picsum.photos/600/300/?image=25"
    class="card"
    style="max-width: 20rem;"
  >
    <b-card-text>
      <div>
        {{ business.short_description }}
      </div>
      <div>
        <b-button size="sm" variant="primary" @click="toBusinessPage">View</b-button>
      </div>
    </b-card-text>
    <template v-slot:footer>
      <small class="text-muted">{{ business.address }}, {{ business.city }}, {{ business.province }}</small><br>
    </template>
  </b-card>
</template>

<script>
export default {
  name: 'BusinessComponent',
  props: ['business'],
  methods: {
    toBusinessPage: function(e) {
      this.$router.push({
        path: `/search-listing/${this.business.id}`
      })
    },
  }
}
</script>

<style scoped>
  .card {
    /* width: 18rem; */
    /* height: 18rem; */
  }
</style>