<template>
    <div class="player-card">
      <img :src="player.photo_url" alt="Player" />
      <h5>{{ player.name }}</h5>
      <p>Position: {{ player.position }}</p>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, PropType } from 'vue';
  
  interface Player {
    name: string;
    position: string;
    photo_url: string;
  }
  
  export default defineComponent({
    name: 'PlayerCard',
    props: {
      player: {
        type: Object as PropType<Player>,
        required: true,
      },
    },
  });
  </script>
  
  <style scoped>
  .player-card {
    border: 1px solid #ccc;
    padding: 10px;
    text-align: center;
    width: 150px;
  }
  .player-card img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
  }
  </style>
  