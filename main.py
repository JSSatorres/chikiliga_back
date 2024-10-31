from fastapi import FastAPI
from backend.scraper.scraper import login_to_comunio, get_dashboard_data

app = FastAPI()

USERNAME = "tu_usuario"
PASSWORD = "tu_password"

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Scraper de Comunio. Visita /docs para más información."}

@app.get("/scrape")
def scrape_dashboard():
    try:
        session = login_to_comunio(USERNAME, PASSWORD)
        data = get_dashboard_data(session)
        return {"success": True, "data": data}
    except Exception as e:
        return {"success": False, "error": str(e)}