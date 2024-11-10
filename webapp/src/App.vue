<template>
  <Homepage />
</template>

<script lang="ts">
import Homepage from './components/Homepage.vue';

export default {
  name: 'App',
  components: {
    Homepage,
  }
};
</script>

<style scoped>
/* Remove the outer box */
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 0; /* No margin for top */
}

/* If you want to style Goal View, do it here */
h1 {
  font-size: 3rem;
  font-weight: bold;
  color: #fff; /* Adjust color */
  margin-top: 20px; /* Space above the title */
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* Optional shadow */
}
</style>
