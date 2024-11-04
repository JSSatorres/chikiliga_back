from config import COMUNIO_USER, PASSWORD
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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