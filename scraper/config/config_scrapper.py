from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def configure_driver():
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    
    # Set user agent to mimic a real browser
    chrome_options.add_argument("user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
    
    # Ignore SSL certificate errors
    chrome_options.add_argument("--ignore-certificate-errors")
    
    # Disable web security
    chrome_options.add_argument("--disable-web-security")
    
    # Allow running insecure content
    chrome_options.add_argument("--allow-running-insecure-content")
    
    # Run Chrome in headless mode (without GUI)
    chrome_options.add_argument("--headless")
    
    # Disable GPU hardware acceleration
    chrome_options.add_argument("--disable-gpu")
    
    # Disable extensions
    chrome_options.add_argument("--disable-extensions")
    
    # Disable sandboxing (useful for some environments)
    chrome_options.add_argument("--no-sandbox")
    
    return webdriver.Chrome(service=service, options=chrome_options)