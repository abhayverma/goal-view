<template>
  <div class="match-card" @click="selectMatch">
    <h4>{{ match.name }}</h4>
    <p>{{ match.date }}</p>
    <p>{{ match.location }}</p>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue';

interface Match {
  id: number;
  date: string;
  team1: string;
  team2: string;
  location: string;
}

export default defineComponent({
  name: 'MatchCard',
  props: {
    match: {
      type: Object as PropType<Match>,
      required: true,
    },
  },
  emits: ['selectMatch'],
  setup(props, { emit }) {
    const selectMatch = () => {
      emit('selectMatch', props.match);
    };

    return {
      selectMatch,
    };
  },
});
</script>

<style scoped>
.match-card {
  cursor: pointer;
  border: 1px solid #ccc;
  padding: 10px;
  width: 200px;
}
</style>
