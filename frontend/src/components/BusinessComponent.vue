<template>
  <b-card
    v-bind:title="business.business_name"
    class="w-25 mb-4"
    style="min-width: 21rem; max-width: 15%"
  >

    <b-card-text>
      <div>
        {{ business.short_description }}
      </div>
      <div class="mt-2">
        <b-button size="sm" style="width: 4rem; height: 30px; font-size: 16px; font-weight:bold;" @click="toBusinessPage">View</b-button>
      </div>
    </b-card-text>
    <template>
      <b-icon icon="geo-alt"></b-icon>
    </template>
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