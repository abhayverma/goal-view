import axios from 'axios';

// Define the base URL (assuming a local backend server)
const API_BASE_URL = 'http://127.0.0.1:5000/api';

export const api = axios.create({
  baseURL: API_BASE_URL,
  headers: { 'Content-Type': 'application/json' },
});

// Functions to fetch data from the backend
export const fetchTeams = (page: number = 1, perPage: number = 10, searchQuery: string = '') => {
  return axios.get(`${API_BASE_URL}/teams`, {
    params: { page, per_page: perPage, search: searchQuery },
  });
};

export const fetchMatches = (page: number = 1, perPage: number = 10, searchQuery: string = '') => {
  return axios.get(`${API_BASE_URL}/matches`, {
    params: { page, per_page: perPage, search: searchQuery },
  });
};

export const fetchPlayers = (teamId: number, page: number = 1, perPage: number = 10, searchQuery: string = '') => {
  return axios.get(`${API_BASE_URL}/players`, {
    params: { teamId, page, per_page: perPage, search: searchQuery },
  });
};

export const fetchPlayerDetails = (playerId: number) => {
  return axios.get(`${API_BASE_URL}/players/${playerId}`);
};

export const fetchAreas = (page: number = 1, perPage: number = 10, searchQuery: string = '') => {
  return api.get('/areas', {
    params: { page, per_page: perPage, search: searchQuery },
  });
};
