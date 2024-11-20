import time
from ..config.config_scrapper import configure_driver
from selenium.webdriver.common.by import By
from config.settings import settings
from selenium.webdriver.common.keys import Keys

def login_to_comunio():
    driver = configure_driver()

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
        username_input.send_keys(settings.comunio_user)
        time.sleep(2)

        password_input.clear()
        password_input.send_keys(settings.comunio_password)
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)
        
        return driver

    except Exception as e:
        print("Error during login:", str(e))
        driver.quit()
        return None
      
def accept_cookies_comuniate(driver):
    try:
        accept_cookies = driver.find_element(By.XPATH, "//button[span[text()='ACEPTO']]")
        accept_cookies.click()
        time.sleep(2)
    except Exception:
        print("Cookie acceptance button not found or already dismissed.")