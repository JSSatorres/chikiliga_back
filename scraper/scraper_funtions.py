import time
from selenium.webdriver.common.by import By
from scraper.connection_pages.connection_pages import accept_cookies_comuniate
from .utils.utils_scraper import remove_diacritics
from scraper.config.config_scrapper import configure_driver




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



def search_player(driver, player_name):
    icon_search = driver.find_element(By.XPATH, "//i[contains(@class, 'fa-search')]")
    icon_search.click()
    time.sleep(2)
    player_name_with_diacritics = remove_diacritics(player_name)
    driver.switch_to.active_element.send_keys(player_name_with_diacritics)
    time.sleep(1)


def select_first_suggestion(driver):    
    try:
        first_suggestion = driver.find_element(By.XPATH, "//*[@id='suggestions2']/div[1]")
        first_suggestion.click()
        time.sleep(3)
        return True
    except Exception as e:
        print("No se encontró sugerencia:", str(e))
        return False
    
def extract_player_data(driver):
    player_data = []
    try:
        # Encuentra el cuerpo de la tabla que contiene las jornadas
        tbody = driver.find_element(By.XPATH, "//table[@class='table']//tbody")
        rows = tbody.find_elements(By.TAG_NAME, "tr")
        
        # Recorre cada fila y extrae los datos de la jornada
        for row in rows:
            jornada_text, team_results, puntos, rating, icons = extract_row_data(row)
            row_data = {
                "jornada": jornada_text,
                "resultados": team_results,
                "puntos": puntos,
                "rating": rating,
                "icons": icons
            }
            player_data.append(row_data)
        
    except Exception as e:
        print("No se encontraron datos de la tabla para")

    return player_data


def extract_row_data(row):
    jornada_text, team_results, puntos, rating, icons = "", "", "", "", []

    try:
        # Verificar si es una fila de "Lesionado" o "No fue alineado"
        lesionado_o_no_alineado = row.find_elements(By.XPATH, ".//span[contains(@class, 'bg-danger') or contains(text(), 'No fue alineado')]")
        if lesionado_o_no_alineado:
            # Extraer texto de la celda que contiene la información de "Lesionado" o "No fue alineado"
            jornada_text = lesionado_o_no_alineado[0].text
            return jornada_text, team_results, "N/A", "N/A", icons  # Devuelve "N/A" para puntos y rating si el jugador no fue alineado o está lesionado

        # Si no es un caso especial, extraer información de la primera celda (jornada y resultados)
        jornada_cell = row.find_element(By.XPATH, ".//td[1]/div")
        jornada_text = jornada_cell.find_element(By.TAG_NAME, "strong").text
        team_results = jornada_cell.text
    except Exception as e:
        print(f"Error extrayendo jornada o resultados: {e}")

    try:
        puntos_cell = row.find_element(By.XPATH, ".//td[2]")

        # Intentar extraer puntos si existen
        try:
            puntos_element = puntos_cell.find_element(By.CLASS_NAME, "puntos")
            puntos = puntos_element.text if puntos_element else "N/A"
            print(f"Puntos: {puntos}")
        except Exception as e:
            print(f"Error extrayendo puntos: {e}")

        # Intentar extraer rating si existe
        try:
            rating_element = puntos_cell.find_element(By.XPATH, ".//div[contains(@style, 'color: #555;')]")
            rating = rating_element.text if rating_element else "N/A"
            print(f"Rating: {rating}")
        except Exception as e:
            print(f"Error extrayendo rating: {e}")

        # Extraer iconos adicionales, como tarjetas o sustituciones
        try:
            additional_icons = puntos_cell.find_elements(By.TAG_NAME, "i")
            icons = [icon.get_attribute("class") for icon in additional_icons]
            print(f"Icons: {icons}")
        except Exception as e:
            print(f"Error extrayendo iconos: {e}")

    except Exception as e:
        print(f"Error extrayendo datos de puntos o estado en la segunda celda: {e}")

    return jornada_text, team_results, puntos, rating, icons


def search_players_in_comuniate(players_json):
    driver = configure_driver()
    players_data = []  # Almacena todos los datos de los jugadores
    
    print("Jugadores a buscar:", players_json["players"])  # Confirma los jugadores que se procesarán

    try:
        # Abrir la página principal de Comuniate
        driver.get("https://www.comuniate.com/")
        time.sleep(3)
        accept_cookies_comuniate(driver)

        # Iterar sobre cada jugador en el JSON
        for player_name in players_json["players"]:
            try:
                print(f"Buscando jugador: {player_name}")  # Depuración: jugador actual
                search_player(driver, player_name)  # Buscar al jugador
                time.sleep(2)
                if select_first_suggestion(driver):  # Seleccionar la primera sugerencia
                    player_data = extract_player_data(driver)  # Extraer datos del jugador
                    print(f"Datos extraídos para {player_name}: {player_data}")  # Depuración: datos extraídos
                    time.sleep(2)
                    if player_data:  # Verifica que los datos no estén vacíos
                        players_data.append({player_name: player_data})  # Agregar los datos a la lista
                else:
                    print(f"No se encontró sugerencia para {player_name}")  # Depuración: sin sugerencia

                # Regresar a la página de búsqueda sin recargar
                driver.back()
                time.sleep(2)
            except Exception as e:
                print(f"Error al procesar {player_name}: {str(e)}")  # Mensaje de error específico para cada jugador

    except Exception as e:
        print("Error general en el proceso de búsqueda:", str(e))

    finally:
        driver.quit()

    return players_data


