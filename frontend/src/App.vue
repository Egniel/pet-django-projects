<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Roboto');
body {
   margin: 0;
   padding: 0;
   /* font: normal 75% Arial, Helvetica, sans-serif; */
   font-family: 'Roboto', sans-serif;
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: 100vh;
  overflow: hidden;
 }
</style>
