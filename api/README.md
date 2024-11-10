# Flask Goal View API

A simple Flask application that displays teams, matches, and players, with functionalities for searching teams, viewing players from a selected team, and browsing through upcoming matches.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [File Structure](#file-structure)
- [Running the App](#running-the-app)

## Description

This Flask application is designed to showcase football-related data, including:

- **Teams**: Display a list of teams.
- **Matches**: Show upcoming and past matches.
- **Players**: Fetch and display players for a selected team.
- **Search**: Search for teams and players.

The app uses APIs to fetch teams, matches, and players. It also includes search functionality for dynamic fetching of data.

## Features

- Displays a list of football teams and matches.
- Fetches and shows players when a team is selected.
- Allows users to search for teams and players.
- Provides pagination to handle large data sets.
- Displays match details and allows navigation between matches.

## Prerequisites

Before running this app, you need to have the following software installed:

- **Python 3.x**: [Download from Python's official website](https://www.python.org/downloads/)
- **Virtualenv** (optional, but recommended for creating isolated environments)
- **pip** (Python's package installer)

### Installing Python on Windows

1. **Download and Install Python**:
   - Go to the [official Python website](https://www.python.org/downloads/).
   - Download the latest stable version of Python for Windows.
   - During installation, make sure to check the box that says **"Add Python to PATH"** before clicking "Install Now".

2. **Install pip**:
   - `pip` is bundled with Python versions 3.4 and above. To check if `pip` is installed, open Command Prompt and run:

   ```
   pip --version
   ```
If it's not installed, you can install it by running:
```
python3 -m ensurepip --upgrade
```
# Installation
Follow these steps to install and run the app:

### Step-by-Step Installation:
#### 1. Clone the repository:

Open Command Prompt or PowerShell and run:

```
git clone <your-repository-url>
cd <your-repository-folder>
```
#### 2. Create a virtual environment (optional but recommended):

- Open Command Prompt or PowerShell and navigate to the project folder.
- Run the following command to create a virtual environment:
```
python3 -m venv venv
```
- Activate the virtual environment:
#### For Command Prompt:
```
venv\Scripts\activate
```
#### For PowerShell:

```
.\venv\Scripts\Activate
```
#### 3. Install required dependencies:

###### With the virtual environment activated, install the dependencies from requirements.txt:
```
pip install -r requirements.txt
```
#### 4. Run the application:

Once the dependencies are installed, run the Flask application:
```
python3 app.py
```
or
```
flask run
```

This will start the Flask development server on your local machine. By default, it should be accessible at http://127.0.0.1:5000.

Open your web browser and navigate to this address to view the application in action.

# File Structure
```
api/
├── __init__.py                  # Initialization file for the API package
├── app.py                        # Main entry point for the application
├── config.py                     # Configuration settings for the application
├── goalview.db                   # SQLite database file (if used)
├── migrations/                   # Folder for database migrations
├── models/                       # Folder for database models
│   ├── __pycache__/              # Compiled Python bytecode
│   ├── __init__.py               # Initialization file for models
│   ├── area.py                   # Model for the "area" entity
│   ├── match.py                  # Model for the "match" entity
│   ├── player.py                 # Model for the "player" entity
│   └── team.py                   # Model for the "team" entity
├── routes/                       # Folder for API route definitions
│   ├── __pycache__/              # Compiled Python bytecode
│   ├── __init__.py               # Initialization file for routes
│   ├── areas.py                  # Route for handling "area" related API endpoints
│   ├── matches.py                # Route for handling "match" related API endpoints
│   ├── player_details.py         # Route for player detail-related API endpoints
│   ├── players.py                # Route for handling "player" related API endpoints
│   └── teams.py                  # Route for handling "team" related API endpoints
├── static/                       # Folder for static files like images, CSS, etc.
│   └── swagger.yaml              # Swagger API documentation file
├── instance/                     # Folder for instance-specific files (e.g., instance configuration)
├── requirements.txt              # Python dependencies for the project
├── README.md                     # Project documentation
├── venv/                         # Virtual environment for Python dependencies
└── virtual/                      # Possibly another environment folder or virtual environment
```

# Running the App
To run the app locally:

1. Activate your virtual environment (if using one).

2. Start the Flask development server:
```
python3 app.py
```
OR
```
flask run
```

3. Open your browser and visit http://127.0.0.1:5000. 
\
The homepage will display a carousel with upcoming matches, a search bar for teams, and a list of teams with clickable options to view players.