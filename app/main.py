from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.api.v1.endpoints.player import router as player_router
from app.core.config import settings
from app.api.routes import router as old_router  # Asegúrate de actualizar la ruta real

app = FastAPI()

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include new and old routers
app.include_router(player_router, prefix="/api/v1/players", tags=["players"])
app.include_router(old_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI DDD Hexagonal Architecture Project!"}

if __name__ == "__main__":
    # Para ejecutar la aplicación
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)