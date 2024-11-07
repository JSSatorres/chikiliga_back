from config import COMUNIO_USER, PASSWORD
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from scraper.utils_scraper import remove_diacritics

def login_to_comunio():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://www.comunio.es/")
        time.sleep(3)

        try:
            acept_cookies = driver.find_element(By.CLASS_NAME, "css-47sehv")
            acept_cookies.click()
            time.sleep(2)
        except Exception:
            print("error finding cookies prompt")

        # Find and click the login button to open the modal
        boton_login = driver.find_element(By.XPATH, "//a[contains(@class, 'login-btn') and contains(@class, 'registration-btn-fill')]")
        boton_login.click()
        time.sleep(2)

        # Enter credentials and log in
        username_input = driver.find_element(By.NAME, "input_login")
        password_input = driver.find_element(By.NAME, "input_pass")

        username_input.clear()
        username_input.send_keys(COMUNIO_USER)
        time.sleep(2)

        password_input.clear()
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)
        
        return driver

    except Exception as e:
        print("Error during login:", str(e))
        driver.quit()
        return None

def fetch_market_data(driver):
    players_data = []

    try:
        # Click on the "Mercado" button to open the market page
        market_button = driver.find_element(By.XPATH, "//a[contains(@class, 'text_uppercase') and contains(@title, 'Mercado')]")
        market_button.click()
        time.sleep(3)

        # Extract player data
        players = driver.find_elements(By.XPATH, "//div[contains(@class, 'csspt-row') and contains(@ng-repeat, 'marketItem in vm.marketItems track by')]")
        for player in players:
            try:
                player_name = player.find_element(By.XPATH, ".//div[contains(@class, 'text-to-slide')]").text
                owner = player.find_element(By.XPATH, ".//span[contains(@class, 'csspt-owner__text--unlinked')]").text
                if owner.lower() == "computer":
                    market_value = player.find_element(By.XPATH, ".//span[contains(@class, 'csspt-marketvalue')]").text
                    minimum_offer = player.find_element(By.XPATH, ".//span[contains(@class, 'csspt-price')]").text

                    player_info = {
                        "name": player_name,
                        "owner": owner,
                        "market_value": market_value,
                        "minimum_offer": minimum_offer
                    }
                    players_data.append(player_info)

            except Exception as e:
                print("Error extracting player data:", str(e))

    except Exception as e:
        print("Error accessing market data:", str(e))

    return players_data

def accept_cookies_comuniate(driver):
    try:
        accept_cookies = driver.find_element(By.XPATH, "//button[span[text()='ACEPTO']]")
        accept_cookies.click()
        time.sleep(2)
    except Exception:
        print("Cookie acceptance button not found or already dismissed.")

def search_players_in_comuniate(players_json):
    # Configure Selenium driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Array to store data of the found players
    players_data = []

    try:
        # Open the Comuniate page
        driver.get("https://www.comuniate.com/")
        time.sleep(3)  # Wait a few seconds for the page to load

        # Accept cookies
        accept_cookies_comuniate(driver)

        # Iterate over each player in the JSON
        for player_name in players_json["players"]:

            
            # Locate the search icon and click it to open the search box
            icon_search = driver.find_element(By.XPATH, "//i[contains(@class, 'fa-search')]")
            icon_search.click()
            time.sleep(2)
            
            # Directly type the player's name, assuming the search box is now focused
            player_name_with_diacritics = remove_diacritics(player_name)
            print(player_name_with_diacritics)
            driver.switch_to.active_element.send_keys(player_name_with_diacritics)
            time.sleep(1)  # Wait for suggestions to load
            
            # Select and click the first suggestion if present
            try:
                first_suggestion = driver.find_element(By.XPATH, "//*[@id='suggestions2']/div[1]")
                first_suggestion.click()
                time.sleep(3)  # Wait for the player's profile to load

                # Extract player information (modify as needed based on page structure)
                tbody = driver.find_element(By.TAG_NAME, "tbody")
                rows = tbody.find_elements(By.TAG_NAME, "tr")  # Obtener todas las filas

                # Iterar sobre cada fila y extraer los datos
                for row in rows:
                    # Extraer jornada y resultados (primera columna)
                    jornada_cell = row.find_element(By.XPATH, ".//td[1]/div")
                    print(jornada_cell)
                    jornada_text = jornada_cell.find_element(By.TAG_NAME, "strong").text
                    print(jornada_text)# Extraer texto de la jornada
                    team_results = jornada_cell.text  # Esto incluye la jornada y el resultado de los equipos

                    # Extraer puntos y detalles adicionales (segunda columna)
                    puntos_cell = row.find_element(By.XPATH, ".//td[2]")
                    puntos = puntos_cell.find_element(By.CLASS_NAME, "puntos").text  # Extraer puntos
                    rating = puntos_cell.find_element(By.XPATH, ".//div[contains(@style, 'color: #555;')]").text  # Rating entre paréntesis

                    # Buscar iconos adicionales (amarilla, roja, etc.) y su presencia
                    additional_icons = puntos_cell.find_elements(By.TAG_NAME, "i")
                    icons = [icon.get_attribute("class") for icon in additional_icons]  # Obtener todas las clases de iconos presentes

                    # Guardar datos de cada fila
                    row_data = {
                        "jornada": jornada_text,
                        "resultados": team_results,
                        "puntos": puntos,
                        "rating": rating,
                        "icons": icons
                    }
                    players_data.append(row_data)

            except Exception as e:
                print(f"No data found for {player_name}. Error: {str(e)}")
            
            # Return to the main page for the next player
            driver.get("https://www.comuniate.com/")
            time.sleep(2)

    except Exception as e:
        print("Error accessing Comuniate:", str(e))
    
    finally:
        # Keep the browser open for inspection
        input("Press Enter to close the browser...")  # Wait for user input before closing
        driver.quit()  # Close the browser after pressing Enter
        
    for player in players_data:
        print(player)
    
    return players_data



# def search_players_in_comuniate(players_json):
    

#     # Configure Selenium driver
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)

#     # Array to store data of the found players
#     players_data = []

#     try:
#         # Open the Comuniate page
#         driver.get("https://www.comuniate.com/")
#         time.sleep(3)  # Wait a few seconds for the page to load

#         # Accept cookies if the button is present
#         try:
#             accept_cookies = driver.find_element(By.XPATH, "//button[span[text()='ACEPTO']]")
#             accept_cookies.click()
#             time.sleep(2)
#         except Exception:
#             print("Cookie acceptance button not found or already dismissed.")

#         # Iterate over each player in the JSON
#         for player_name in players_json["players"]:
#             print(f"Searching data for player: {player_name}")
            
#             # Locate the search icon and click it to open the search box
#             icon_search = driver.find_element(By.XPATH, "//i[contains(@class, 'fa-search')]")
#             icon_search.click()
#             time.sleep(2)
            
#               # Directly type the player's name, assuming the search box is now focused
#             # driver.switch_to.active_element.send_keys(player_name)
#             driver.switch_to.active_element.send_keys('asano')
#             time.sleep(1)  # Wait for suggestions to load
            
#             # Select and click the first suggestion if present
#             try:
#                 first_suggestion = driver.find_element(By.XPATH, "//*[@id='suggestions2']/div[1]")
#                 first_suggestion.click()
#                 time.sleep(3)  # Wait for the player's profile to load

#                 # Extract player information (modify as needed based on page structure)
#                 player_data = {}
#                 player_data["name"] = player_name
#                 player_data["team"] = driver.find_element(By.CLASS_NAME, "team-name").text  # Adjust selector as needed
#                 player_data["market_value"] = driver.find_element(By.CLASS_NAME, "market-value").text  # Adjust selector as needed

#                 # Add player data to the list
#                 players_data.append(player_data)

#             except Exception as e:
#                 print(f"No data found for {player_name}. Error: {str(e)}")
            
#             # Return to the main page for the next player
#             driver.get("https://www.comuniate.com/")
#             time.sleep(2)

#     except Exception as e:
#         print("Error accessing Comuniate:", str(e))
    
#     finally:
#         # Keep the browser open for inspection
#         input("Press Enter to close the browser...")  # Wait for user input before closing
#         driver.quit()  # Close the browser after pressing Enter

#     return players_data
