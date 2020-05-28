<template>
  <mdb-navbar expand="large" dark color="blue" position="top">
    <mdb-navbar-brand>
      <router-link :to="{path: '/'}">
        <img src="@/assets/brand.png" class="zoom overlay" height="45px"/>
      </router-link>
    </mdb-navbar-brand>
    <mdb-navbar-toggler>
      <mdb-navbar-nav>
        <mdb-nav-item href="#" active>Home</mdb-nav-item>
        <router-link :to="{name: 'PlayUrl'}"><mdb-nav-item>Play with url</mdb-nav-item></router-link>
        <router-link :to="{name: 'ParseM3u'}"><mdb-nav-item>Parse</mdb-nav-item></router-link>
        <!-- <mdb-dropdown tag="li" class="nav-item">
          <mdb-dropdown-toggle tag="a" navLink color="stylish" slot="toggle" waves-fixed>Dropdown</mdb-dropdown-toggle>
          <mdb-dropdown-menu>
            <mdb-dropdown-item>Action</mdb-dropdown-item>
            <mdb-dropdown-item>Another action</mdb-dropdown-item>
            <mdb-dropdown-item>Something else here</mdb-dropdown-item>
          </mdb-dropdown-menu>
        </mdb-dropdown> -->
      </mdb-navbar-nav>
    </mdb-navbar-toggler>
  </mdb-navbar>
</template>

<style scoped>
  img {
    cursor: pointer;
  }
</style>

<script>
  import { mdbDropdown, mdbDropdownToggle, mdbDropdownMenu, mdbDropdownItem, mdbContainer, mdbNavbar, mdbNavbarBrand, mdbNavbarToggler, mdbNavbarNav, mdbNavItem } from 'mdbvue';
  export default {
    name: 'NavBar',
    components: {
      mdbNavbar,
      mdbNavbarBrand,
      mdbNavbarToggler,
      mdbNavbarNav,
      mdbNavItem,
      mdbContainer,
      mdbDropdown,
      mdbDropdownToggle,
      mdbDropdownMenu,
      mdbDropdownItem
    }
  }
</script>