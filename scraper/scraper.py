import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Autenticarse en Comunio utilizando Selenium
def login_to_comunio(username, password):
    # Configurar el driver de Selenium
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Abrir la página de login de Comunio
        driver.get("https://www.comunio.es/")
        time.sleep(3)  # Esperar unos segundos para que cargue la página

        # Aceptar la política de privacidad
        try:
            aceptar_cookies = driver.find_element(By.CLASS_NAME, "css-47sehv")
            aceptar_cookies.click()
            time.sleep(2)  # Esperar a que se cierre el modal de cookies
        except Exception as e:
            print("No se encontró el botón de aceptar cookies o ya estaba cerrado.")
            
        # Encontrar y hacer clic en el botón de login para abrir el modal
        boton_login = driver.find_element(By.XPATH, "//a[contains(@class, 'login-btn') and contains(@class, 'registration-btn-fill')]")
        boton_login.click()
        time.sleep(2)  # Esperar a que el modal de login se abra

        # Ingresar las credenciales
        username_input = driver.find_element(By.NAME, "input_login")
        password_input = driver.find_element(By.NAME, "input_pass")

        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)  # Esperar unos segundos para que se procese el login
        
        # Hacer clic en el botón de "Mercado"
        market_button = driver.find_element(By.XPATH, "//a[contains(@class, 'text_uppercase') and contains(@title, 'Mercado')]")
        market_button.click()
        time.sleep(3)  # Esperar para que cargue la página del mercado

        # Recoger la información de los jugadores
        players = driver.find_elements(By.XPATH, "//div[contains(@class, 'csspt-row') and contains(@ng-repeat, 'marketItem in vm.marketItems track by')]")
        for player in players:
            try:
                # Obtener el nombre del jugador
                player_name = player.find_element(By.XPATH, "//span[contains(@class, 'bg-wrapper basic')]//a[contains(@class, 'csspt-name')]//div[contains(@class, 'text-to-slide')]").text



                # Obtener el nombre del propietario
                # propietario = player.find_element(By.XPATH, ".//span[contains(@class, 'csspt-owner__text--unlinked')]").text
                # # Obtener el valor de mercado
                # valor_mercado = player.find_element(By.XPATH, ".//span[contains(@class, 'csspt-marketvalue')]").text
                # # Obtener la oferta mínima
                # oferta_minima = player.find_element(By.XPATH, ".//span[contains(@class, 'csspt-price')]").text

                print("Player Information:")
                print(f"Jugador: {player_name}")
                # print(f"Propietario: {propietario}")
                # print(f"Valor de mercado: {valor_mercado}")
                # print(f"Oferta mínima: {oferta_minima}")
                print("-----------------------------")
            except Exception as e:
                print("Error al extraer datos del jugador: ", str(e))

        # Mantener la ventana abierta para poder observar
        input("Presiona Enter para cerrar el navegador...")  # Mantener la ventana abierta hasta que el usuario lo indique

        return driver

    except Exception as e:
        print("Error durante la autenticación:", str(e))
        input("Presiona Enter para cerrar el navegador después del error...")  # Mantener la ventana abierta si falla
        driver.quit()
        return None

# Ejecutar directamente para probar Selenium
if __name__ == "__main__":
    USERNAME = "juansataz"
    PASSWORD = "VayaComunio"
    login_to_comunio(USERNAME, PASSWORD)