from scraper.scraper_funtions import login_to_comunio, fetch_market_data, search_players_in_comuniate
import json

def get_dashboard_data():
    """
    Main function to retrieve dashboard data from Comunio and fetch additional information from Comuniate.
    Temporarily bypasses login and market data retrieval for testing.
    """
    
    # Uncomment the following lines to restore the full functionality
    # driver = login_to_comunio()
    # if driver:
    #     # Get market data from Comunio
    #     players_data = fetch_market_data(driver)
    #     driver.quit()
        
    #     # Extract player names directly from players_data
    #     player_names = [player["name"] for player in players_data]  # List of player names

    # Temporary code block for testing without login and market data retrieval
    if True:  # Replace with `if driver:` when you want to restore full functionality
        # Temporary: Read player names from a JSON file for testing
        with open("scraper/test_data.json", "r") as file:
            test_data = json.load(file)
        
        # Extract player names from the test JSON data
        player_names = [player["name"] for player in test_data["data"]]
        
        print(player_names)
        # Create the JSON format expected by search_players_in_comuniate
        players_json = {
            "players": player_names
        }
        
        # Call search_players_in_comuniate with the JSON to get additional data
        comuniate_data = search_players_in_comuniate(players_json)
        
        # Return both sets of data for testing purposes
        return {
            # "comunio_data": players_data,  # Uncomment this line when restoring full functionality
            "comuniate_data": comuniate_data
        }

    else:
        print("Login failed. Could not fetch market data.")
        return None