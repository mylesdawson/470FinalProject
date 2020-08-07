<template>
  <div>
    <b-navbar >
      <b-navbar-brand>
        <b-nav-item to="/home">
          <img  src="../assets/logo.png" id="skedge-logo" alt="Skedge">
        </b-nav-item>
      </b-navbar-brand>

      <template v-if="token">
        <b-navbar-nav>
          <b-nav-item :active='$route.name =="HomePage"' to="/home">Home</b-nav-item>
          <b-nav-item :active='$route.name =="CalendarPage"' to="/calendar">Calendar</b-nav-item>
          <b-nav-item :active='$route.name =="ServicesPage"' to="/services">Services</b-nav-item>
          <b-nav-item :active='$route.name =="TeamPage"' to="/team">Team</b-nav-item>
          <b-nav-item :active='$route.name =="ListingsPage"' to="/listings">Listings</b-nav-item>
          <b-nav-item :active='$route.name =="BusinessPage"' to="/business">Business</b-nav-item>
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


      <template v-if="!token">
        <b-navbar-nav class="ml-auto">
          <b-nav-item>
            <b-button variant="outline-primary" type="submit" to="/new-account">Create An Account</b-button>
          </b-nav-item>
          <b-nav-item>
            <b-button variant="outline-success" type="submit" to="/login">Login</b-button>
          </b-nav-item>
        </b-navbar-nav>
      </template>
    </b-navbar>

  </div>
</template>

<script>
const token = '';

export default {
  name: 'Navbar',
  computed:{
      showtabs(){
          return this.$route.path != '/login'
      },
  },
  data: function(){
    return {
      token: token
    }
  }
}

</script>

<style scoped>
  li {
    list-style: none;
  }

  #skedge-logo {
    width: 40px;
    height: 40px;
  }

  #skedge-logo:hover {
    position: relative;
    top: -.1rem;
  }

  /* #profile-dropdown {
    border-radius: 50%;
    width: 40px;
    height: 40px;
  } */
</style>