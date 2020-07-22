<template>
  <div>
    <b-navbar >
      <b-navbar-brand>
        <img  src="../assets/logo.png" id="skedge-logo" alt="Skedge">
      </b-navbar-brand>
      
      <template v-if="showtabs">
        <b-navbar-nav>
          <b-nav-item :active='$route.name =="HomePage"' to="/home">Home</b-nav-item>
          <b-nav-item :active='$route.name =="ServicesPage"' to="/services">Services</b-nav-item>
          <b-nav-item :active='$route.name =="CalendarPage"' to="/calendar">Calendar</b-nav-item>
          <b-nav-item :active='$route.name =="ListingsPage"' to="/listings">Listings</b-nav-item>
          <b-nav-item :active='$route.name =="TeamPage"' to="/team">Team</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto">
          <b-nav-item>
            <b-button variant="outline-primary" type="submit" to="/new-listing">Create New Listing</b-button>
          </b-nav-item>
          <b-nav-item>
            <b-nav-item-dropdown
              class="profile-dropdown"
              right
              text="Your Account">
              <b-dropdown-item>Settings</b-dropdown-item>
              <b-dropdown-item to="/login">Logout</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-nav-item>
        </b-navbar-nav>
      </template>

    </b-navbar>

  </div>
</template>

<script>
export default {
  name: 'Navbar',
  computed:{
      showtabs(){
          return this.$route.path != '/login'
      },
      
  }
}

</script>

<style scoped>
  #skedge-logo {
    width: 40px;
    height: 40px;
  }

  /* #profile-dropdown {
    border-radius: 50%;
    width: 40px;
    height: 40px;
  } */
</style>