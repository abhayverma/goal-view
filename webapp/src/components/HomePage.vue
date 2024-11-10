<template>
  <div class="football-theme">
    <!-- Hero Banner with Sliding Effect -->
    <div class="hero-banner">
      <div class="match-info">
        <p v-if="selectedMatch">
          Match: {{ selectedMatch.name }} | Date: {{ selectedMatch.date }}
        </p>
        <p v-else>No match selected yet.</p>
      </div>
      <div class="carousel-controls">
        <button @click="previousMatch">Prev</button>
        <button @click="nextMatch">Next</button>
      </div>
    </div>

    <!-- Search Bar -->
    <div class="search-bar">
      <input v-model="searchQuery" @input="search" type="text" placeholder="Search teams..." />
    </div>

    <!-- Teams Section -->
    <h2>Teams</h2>
    <div class="teams">
      <TeamCard v-for="team in teams" :key="team.id" :team="team" @selectTeam="loadPlayersFromTeam" />
    </div>

    <!-- Modal for displaying Players -->
    <div v-if="isModalVisible" class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop>
        <h2>Players for {{ selectedTeam.name }}</h2>
        <div class="players-list">
          <div v-for="player in players" :key="player.id" class="player-card">
            <img :src="player.photo" alt="Player" class="player-photo" />
            <div class="player-details">
              <h3>{{ player.name }}</h3>
              <p>{{ player.position }}</p>
            </div>
          </div>
        </div>
        <button @click="closeModal" class="close-modal">Close</button>
      </div>
    </div>

    <!-- Matches Section -->
    <h2>Matches</h2>
    <div class="matches">
      <MatchCard v-for="match in matches" :key="match.id" :match="match" @selectMatch="setSelectedMatch" />
    </div>

    <!-- Players Section -->
    <div v-if="selectedTeam" class="players">
      <h2>Players</h2>
      <PlayerCard v-for="player in players" :key="player.id" :player="player" />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import TeamCard from './TeamCard.vue';
import MatchCard from './MatchCard.vue';
import PlayerCard from './PlayerCard.vue';
import { fetchTeams, fetchMatches, fetchPlayers, searchTeams, searchPlayers } from '../services/apiService';

interface Team {
  id: number;
  name: string;
  logo_url: string;
}

interface Match {
  id: number;
  date: string;
  team1: string;
  team2: string;
  location: string;
}

interface Player {
  id: number;
  name: string;
  position: string;
  photo_url: string;
}

export default defineComponent({
  name: 'HomePage',
  components: { TeamCard, MatchCard, PlayerCard },
  setup() {
    const teams = ref<Team[]>([]);
    const matches = ref<Match[]>([]);
    const players = ref<Player[]>([]);
    const selectedTeam = ref<Team | null>(null);
    const selectedMatch = ref<Match | null>(null);
    const searchQuery = ref<string>('');
    const matchIndex = ref(0);
    const isModalVisible = ref(false); // Controls the visibility of the modal
    const modalTeam = ref<Team | null>(null); // Holds selected team for modal

    // Fetch teams and matches when component is mounted
    onMounted(async () => {
      try {
        const teamsResponse = await fetchTeams();
        teams.value = teamsResponse.data.teams;

        const matchesResponse = await fetchMatches();
        matches.value = matchesResponse.data.matches;
        selectedMatch.value = matches.value[matchIndex.value];
      } catch (error) {
        console.error('Error fetching teams or matches:', error);
      }
    });

    // Fetch players based on selected team
    const loadPlayersFromTeam = async (team: Team) => {
      try {
        const playersResponse = await fetchPlayers(team.id);
        players.value = playersResponse?.data?.players;
        selectedTeam.value = team;
        modalTeam.value = team; // Store selected team for modal
        isModalVisible.value = true; // Show the modal
      } catch (error) {
        console.error('Error fetching players:', error);
      }
    };

    // Set the selected match for the hero banner
    const setSelectedMatch = (match: Match) => {
      selectedMatch.value = match;
    };

    // Slide to the next match
    const nextMatch = () => {
      matchIndex.value = (matchIndex.value + 1) % matches.value.length;
      selectedMatch.value = matches.value[matchIndex.value];
    };

    // Slide to the previous match
    const previousMatch = () => {
      matchIndex.value = (matchIndex.value - 1 + matches.value.length) % matches.value.length;
      selectedMatch.value = matches.value[matchIndex.value];
    };

    // Search for teams or players
    const search = async () => {
      try {
        if (searchQuery.value) {
          // Search for teams
          const teamsResponse = await fetchTeams(1, 10, searchQuery.value);
          teams.value = teamsResponse.data.teams;

          // Fetch players based on selected team and search query
          if (selectedTeam.value) {
            const playersResponse = await fetchPlayers(selectedTeam.value.id, 1, 10, searchQuery.value);
            players.value = playersResponse.data.players;
          }
        } else {
          // If no query, fetch all teams and players
          const teamsResponse = await fetchTeams();
          teams.value = teamsResponse.data.teams;

          // Fetch players for selected team (if any)
          if (selectedTeam.value) {
            const playersResponse = await fetchPlayers(selectedTeam.value.id);
            players.value = playersResponse.data.players;
          }
        }
      } catch (error) {
        console.error('Error fetching search results:', error);
      }
    };

    // Close the modal
    const closeModal = () => {
      isModalVisible.value = false;
    };

    return {
      teams,
      matches,
      players,
      selectedTeam,
      selectedMatch,
      searchQuery,
      loadPlayersFromTeam,
      setSelectedMatch,
      search,
      nextMatch,
      previousMatch,
      isModalVisible,
      modalTeam,
      closeModal,
    };
  },
});
</script>

<style scoped>
/* Global Football Theme */
.football-theme {
  font-family: 'Arial', sans-serif;
  background-color: #f7f7f7;
  color: #333;
  padding: 20px;
  max-width: 100%;
}

/* Hero Banner Styles */
.hero-banner {
  background-color: #00a859;
  padding: 40px;
  text-align: center;
  color: white;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
  position: relative;
  margin-bottom: 40px;
}

.hero-banner h2 {
  font-size: 3rem;
  font-weight: bold;
  margin-bottom: 10px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.hero-banner p {
  font-size: 1.2rem;
}

/* Carousel controls */
.carousel-controls {
  position: absolute;
  top: 50%;
  width: 100%;
  display: flex;
  justify-content: space-between;
  transform: translateY(-50%);
  left: 0;
}

.carousel-controls button {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 1rem;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.carousel-controls button:hover {
  background-color: #45a049;
}

/* Search Bar */
.search-bar {
  margin: 20px 0;
  text-align: center;
}

.search-bar input {
  width: 60%;
  padding: 10px;
  font-size: 1.2rem;
  border-radius: 5px;
  border: 2px solid #00a859;
  background-color: white;
  color: #333;
}

/* Teams, Matches, Players Layout */
.teams,
.matches,
.players {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}

h2 {
  font-size: 2rem;
  text-align: center;
  margin-bottom: 20px;
  font-weight: bold;
  color: #00a859;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  font-size: 1rem;
}

button:hover {
  background-color: #45a049;
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  padding: 30px;
  border-radius: 10px;
  width: 80%;
  max-width: 1000px;
  overflow-y: auto;
}

.close-modal {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 1.2rem;
  cursor: pointer;
  border-radius: 5px;
  margin-top: 20px;
  width: 100%;
}

.close-modal:hover {
  background-color: #e53935;
}

.players-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 15px;
}

.player-card {
  background-color: #f7f7f7;
  padding: 15px;
  border-radius: 10px;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.player-photo {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 5px;
}

.player-details h3 {
  font-size: 1.2rem;
  color: #00a859;
}

.player-details p {
  color: #666;
}
</style>
