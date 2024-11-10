# Goal View Project

This project consists of a **Flask API** backend and a **Vue.js** frontend. It is designed to handle goal view data and related functionalities.

## Project Structure

The project structure is as follows:

## Setup Instructions

Follow the steps below to set up the **Goal View** project on your local machine.

### Prerequisites

- Python 3.x
- Flask 3.x
- Node.js (for the Vue.js app)
- npm (for package management)
- Git (for version control)

### 1. **Setting Up Flask API Backend**

#### Install Python Dependencies

1. Clone the repository:
   ```
   git clone https://github.com/your-repository/goal-view.git
   cd goal-view/api
   ```
2. Set up a Python virtual environment:

```
python -m venv .venv
```
if using python3
```
python3 -m venv .venv
```
3. Activate the virtual environment:

- On Windows:
```
.venv\Scripts\activate
```
- On macOS/Linux:
```
source .venv/bin/activate
```
4. Install the required Python dependencies:

```
pip install -r requirements.txt
```
5. Run the Flask API:

```
flask run
```
The API will be available at http://localhost:5000.

### 2. **Setting Up Vue.js Frontend**
#### Install Node.js Dependencies
1. Navigate to the frontend directory:

```
cd ../webapp
```
2. Install dependencies using npm:

```
npm install
```
#### Run Vue.js Development Server
1. Start the Vue.js development server:
```
npm run dev
```
The Vue.js app will be available at http://localhost:3000.

### 3. **Folder Structure Breakdown**
```
goal-view/
├── .gitignore               # Git ignore file for the project
├── api/                     # Flask API Backend
│   ├── __pycache__/         # Python bytecode cache files
│   ├── .venv                # Virtual environment for Flask
│   ├── #                    # Placeholder or system files
│   ├── a/                   # Additional files (if any)
│   ├── Create/              # Data creation or migration scripts
│   ├── environment/         # Environment-specific configurations
│   ├── instance/            # Instance-specific configurations (e.g., database settings)
│   ├── migrations/          # Database migrations folder
│   ├── models/              # Database models (Player, Team, etc.)
│   │   ├── __pycache__/     # Python bytecode cache files
│   │   ├── __init__.py      # Init file for models package
│   │   ├── area.py          # Model for Area
│   │   ├── match.py         # Model for Match
│   │   ├── player.py        # Model for Player
│   │   └── team.py          # Model for Team
│   ├── routes/              # API route definitions
│   │   ├── __pycache__/     # Python bytecode cache files
│   │   ├── __init__.py      # Init file for routes package
│   │   ├── areas.py         # Route for Area-related API calls
│   │   ├── matches.py       # Route for Match-related API calls
│   │   ├── player_details.py# Route for Player details API calls
│   │   ├── players.py       # Route for Player-related API calls
│   │   └── teams.py         # Route for Team-related API calls
│   ├── static/              # Static assets for the API (e.g., Swagger UI, etc.)
│   │   └── swagger.yaml     # Swagger API definition file
│   ├── venv/                # Another virtual environment folder (if present)
│   ├── virtual/             # Another directory related to virtual environment
│   ├── __init__.py          # Init file for API package
│   ├── app.py               # Main entry point for the Flask application
│   ├── config.py            # Configuration file for Flask app (e.g., DB config)
│   ├── goalview.db          # Database file (SQLite, etc.)
│   ├── README.md            # README file for Flask API backend
│   └── requirements.txt     # Python dependencies for the Flask app
├── instance/                # Instance-specific configuration files
├── webapp/                   # Vue.js Frontend
│   ├── .vscode/             # VSCode specific settings for the frontend
│   ├── node_modules/        # Node.js dependencies
│   ├── public/              # Public static files (e.g., images, icons, etc.)
│   ├── src/                 # Source code for Vue.js components, views, services
│   │   ├── assets/          # Static assets (images, CSS, etc.)
│   │   ├── components/      # Reusable Vue.js components
│   │   ├── views/           # Vue.js views (pages)
│   │   └── services/        # API service methods for backend communication
│   ├── index.html           # Main HTML file for Vue.js frontend
│   ├── package-lock.json    # Lock file for NPM dependencies
│   ├── package.json         # NPM dependencies and scripts
│   ├── tsconfig.app.json    # TypeScript configuration for Vue app
│   ├── tsconfig.json        # Main TypeScript configuration
│   ├── tsconfig.node.json   # TypeScript config for Node.js (if needed)
│   └── vite.config.ts       # Vite configuration for building the frontend
└── README.md                # Global README for the whole project
```
### 4. **Running the Full Application**
1. Start the Flask API backend (api/app.py) using flask run.
2. Start the Vue.js frontend (/webapp) using npm run dev.
3. The frontend will communicate with the Flask backend API, and the app will be fully functional.
