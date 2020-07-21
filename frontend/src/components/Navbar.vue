<template>
  <div>
    <b-navbar >
      <b-navbar-brand>
        <img src="../assets/logo.png" id="skedge-logo" alt="Skedge">
      </b-navbar-brand>

      <b-navbar-nav>
        <b-nav-item to="/">Home</b-nav-item>
        <b-nav-item>Inbox</b-nav-item>
        <b-nav-item>Services</b-nav-item>
        <b-nav-item>Calendar</b-nav-item>
        <b-nav-item>Listings</b-nav-item>
        <b-nav-item to="/team">Team</b-nav-item>
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
            <b-dropdown-item>Logout</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-nav-item>
      </b-navbar-nav>


    </b-navbar>

  </div>
</template>

<script>
export default {
  name: 'Navbar',
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