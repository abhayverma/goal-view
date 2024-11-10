<template>
  <div class="team-card" @click="selectTeam">
    <img v-bind:src="logoUrl" alt="Team Logo" @error="onImageError" :style="{ width: '100px', height: '100px' }" />
    <h3>{{ team.name }}</h3>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType, ref } from 'vue';

interface Team {
  id: number;
  name: string;
  logo_url: string;
}

export default defineComponent({
  name: 'TeamCard',
  props: {
    team: {
      type: Object as PropType<Team>,
      required: true,
    },
  },
  emits: ['selectTeam'],
  setup(props, { emit }) {
    const placeholderUrl = 'https://developers.elementor.com/docs/assets/img/elementor-placeholder-image.png'; // Fallback placeholder URL
    const logoUrl = ref(props.team.logo_url); // Set initial logo URL

    const selectTeam = () => {
      emit('selectTeam', props.team);
    };

    const onImageError = () => {
      console.log('Image failed to load. Replacing with placeholder.');
      logoUrl.value = placeholderUrl; // Replace with placeholder image on error
    };

    // Return logoUrl and selectTeam to make them available in the template
    return { logoUrl, selectTeam, onImageError };
  },
});
</script>

<style scoped>
.team-card {
  cursor: pointer;
  text-align: center;
  width: 150px;
}

.team-card img {
  width: 100%;
  height: auto;
}
</style>
