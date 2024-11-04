from scraper.utils import login_to_comunio, fetch_market_data

def get_dashboard_data():
    driver = login_to_comunio()
    if driver:
        players_data = fetch_market_data(driver)
        driver.quit()
        return players_data
    else:
        print("Login failed. Could not fetch market data.")
        return None