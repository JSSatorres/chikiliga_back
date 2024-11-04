from fastapi import APIRouter
from scraper.scraper import get_dashboard_data

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Scraper de Comunio. Visita /docs para más información."}

@router.get("/scrape")
def scrape_dashboard():
    try:
        data = get_dashboard_data()
        return {"success": True, "data": data}
    
    except Exception as e:
        return {"success": False, "error": str(e)}