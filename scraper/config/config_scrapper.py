from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def configure_driver():
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
    chrome_options.add_argument("--ignore-certificate-errors")  # Ignora errores de certificado SSL
    chrome_options.add_argument("--disable-web-security")       # Desactiva seguridad web
    chrome_options.add_argument("--allow-running-insecure-content")  # Permite contenido no seguro
    return webdriver.Chrome(service=service, options=chrome_options)