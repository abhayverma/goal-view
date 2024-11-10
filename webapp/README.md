# Football Theme Vue App

This is a football-themed Vue.js application that allows users to view and interact with teams, players, and matches. The app provides features like searching for teams, viewing players in a modal popup, and navigating between matches.

## Features

- **Team Cards:** Displays football teams with logos.
- **Player Modal:** View players for a selected team in a modal with detailed information.
- **Match Slider:** Displays a hero banner with match details and the ability to navigate between matches.
- **Search Bar:** Allows searching for teams and players.
- **Responsive Layout:** The app is designed to be responsive, adapting to different screen sizes.

## Project Setup

### Prerequisites

Before running the app, make sure you have the following installed:

- [Node.js](https://nodejs.org/)
- [Vue CLI](https://cli.vuejs.org/) or a similar build tool (e.g., Vite, Webpack)

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/abhayverma/goal-view.git
   ```
Navigate to the project directory:
```
cd goal-view/webapp
```

Install the required dependencies:
```
npm install
```

Development Server

To run the development server:

```
npm run dev
```
The app will be accessible at http://localhost:3000 (or a different port, depending on your configuration).

Build for Production

To build the app for production:
```
npm run build
```
This will generate a dist/ folder containing the production-ready files.

File Structure
```
webapp/
├── src/
│   ├── assets/               # Static assets like images
│   ├── components/           # Vue components like TeamCard, MatchCard, PlayerCard, HomePage
│   ├── services/             # API service calls (fetchTeams, fetchPlayers, etc.)
│   └── App.vue               # Root component
├── package.json              # Project dependencies and scripts
└── README.md                 # This file

```
Components

TeamCard: Displays information about a football team (name, logo).

MatchCard: Displays information about a football match (teams, date, location).

PlayerCard: Displays player details (name, position, photo).

HomePage: The main page of the app, which contains the team and match sections.

Modal: Displays players for a selected team in a modal popup.

Services

apiService.js: Contains functions to fetch data for teams, players, and matches. 

Example functions include:

fetchTeams(): Fetches a list of football teams.

fetchPlayers(teamId): Fetches players for a selected team.

fetchMatches(): Fetches a list of football matches.

Styling
The app uses custom CSS for a football theme. The design includes:

A hero banner with match information.

Player cards in a responsive grid layout.

Modal with player details.

Global Styles

The app uses a football theme with green and white colors.

Buttons and inputs are styled with a simple and modern look.

Player cards have a clean design with images, names, and positions.

Troubleshooting

Error Fetching Data

If you encounter issues with fetching data, ensure that the API endpoints are correctly set up and that your network connection is active.

Check the console for any error messages related to API calls.

License

This project is licensed under the MIT License.