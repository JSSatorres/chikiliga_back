# FastAPI Football Scraping Application

This project is a FastAPI application designed for scraping football player data from external sources, specifically from Comunio and Comunicate. The application allows users to register, create teams composed of players, and interact with a market of players.

## Project Structure

The project is organized into several contexts, each representing a different feature of the application:

- **Player Context**: Manages player-related operations.

  - Application: Contains use cases for creating, retrieving, and deleting players.
  - Domain: Defines the player entity and repository interface.
  - Infrastructure: Implements the player repository and scraping service.
  - Presentation: Handles HTTP requests related to players.

- **Team Context**: Manages team-related operations.

  - Application: Contains use cases for creating, retrieving, and deleting teams.
  - Domain: Defines the team entity and repository interface.
  - Infrastructure: Implements the team repository and scraping service.
  - Presentation: Handles HTTP requests related to teams.

- **Market Context**: Manages market-related operations.

  - Application: Contains use cases for creating, retrieving, and deleting markets.
  - Domain: Defines the market entity and repository interface.
  - Infrastructure: Implements the market repository and scraping service.
  - Presentation: Handles HTTP requests related to markets.

- **Shared**: Contains shared components such as database connections and value objects.

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd fastapi-app
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory and add your MongoDB connection string:

   ```
   MONGODB_URL=<your_mongodb_connection_string>
   ```

5. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

## Usage Examples

- **Register a User**: Endpoint to register a new user (to be implemented).
- **Create a Team**: Endpoint to create a new team.
- **Get All Players**: Endpoint to retrieve a list of all players.
- **Scrape Player Data**: The application will automatically scrape player data from external sources.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.
