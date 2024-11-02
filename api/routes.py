from fastapi import APIRouter
from scraper.scraper import login_to_comunio, get_dashboard_data

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Scraper de Comunio. Visita /docs para más información."}

@router.get("/scrape")
def scrape_dashboard():
    try:
        # Inicia el scraping
        driver = login_to_comunio()
        data = get_dashboard_data(driver)
        driver.quit()  # Asegúrate de cerrar el navegador después de obtener los datos
        return {"success": True, "data": data}
    except Exception as e:
        return {"success": False, "error": str(e)}