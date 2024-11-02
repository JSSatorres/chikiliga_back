# from fastapi import FastAPI
# from scraper.scraper import login_to_comunio
# app = FastAPI()

# USERNAME = "tu_usuario"
# PASSWORD = "tu_password"

# if __name__ == "__main__":
#     login_to_comunio()

# @app.get("/")
# def read_root():
#     return {"message": "Bienvenido a la API de Scraper de Comunio. Visita /docs para más información."}

# @app.get("/scrape")
# def scrape_dashboard():
#     try:
#         session = login_to_comunio(USERNAME, PASSWORD)
#         data = get_dashboard_data(session)
#         return {"success": True, "data": data}
#     except Exception as e:
#         return {"success": False, "error": str(e)}

from fastapi import FastAPI
from api.routes import router

app = FastAPI()

# Incluye las rutas de la API
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)