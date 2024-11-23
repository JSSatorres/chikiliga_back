from scraper.scraper_funtions import fetch_market_data, search_players_in_comuniate
import json
from scraper.connection_pages.connection_pages import login_to_comunio

def get_dashboard_data():
    """
    Main function to retrieve dashboard data from Comunio and fetch additional information from Comuniate.
    Requires login to Comunio and fetches market data.
    """
    # Realiza el login en Comunio
    driver = login_to_comunio()
    if driver:
        try:
            # Obtener datos del mercado de Comunio
            players_data = fetch_market_data(driver)
            
            # Extraer nombres de los jugadores
            player_names = [player["name"] for player in players_data]
            
            # Crear el JSON en el formato esperado para `search_players_in_comuniate`
            players_json = {
                "players": player_names
            }
            
            # Obtener datos adicionales de Comuniate
            comuniate_data = search_players_in_comuniate(players_json)
            
            # Retornar ambos conjuntos de datos para fines de verificación
            return  comuniate_data
            

        finally:
            # Asegura que el navegador se cierre después de completar el proceso
            driver.quit()
    else:
        print("Error: Falló el inicio de sesión. No se pudieron obtener los datos del mercado.")
        return None