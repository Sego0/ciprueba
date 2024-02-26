<template>
 <div id="app">
        <h3 class="d-flex justify-content-center">
            CI Manage
        </h3>

        <nav class="navbar navbar-expand-sm bg-light navbar-dark" style="margin: 0 auto;">
            <ul class="navbar-nav">
            <li class="nav-item m-1">
                <router-link class="btn btn-primary"
                to="/">Home</router-link>
            </li>
            <li class="nav-item m-1">
                <router-link class="btn btn-light btn-outline-primary"
                to="/employee">Employees</router-link>
            </li>
            <li class="nav-item m-1">
                <router-link class="btn btn-light btn-outline-primary"
                to="/device">Devices</router-link>
            </li>
            <li class="nav-item m-1">
                <router-link class="btn btn-light btn-outline-primary"
                to="/employeedevice">Employees/device</router-link>
            </li>
            </ul>

        </nav>
        <router-view></router-view>

    </div>
    <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
    <div class="col-md-4 d-flex align-items-center">
    <ul class="nav col-md-4 justify-content-end list-unstyled d-flex">
        <li class="ms-3"><a class="text-body-secondary" >Developed by K0modoro</a></li>
    </ul>
      <a href="/" class="mb-3 me-2 mb-md-0 text-body-secondary text-decoration-none lh-1">
        <svg class="bi" width="30" height="24"><use xlink:href="#bootstrap"/></svg>
      </a>
      <span class="mb-3 mb-md-0 text-body-secondary">&copy; 2024 Nutrisco, Inc</span>
      <br>
    </div>


  </footer>

</template>

<script>

</script>

<style>

</style>
