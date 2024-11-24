from fastapi import APIRouter
from api.api_utils import transform_object_id
from scraper.scraper import get_dashboard_data
from services.player_service import player_service

# from scraper.scraper import get_dashboard_data


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
    
@router.get("/players")
async def get_players():
    players = player_service.get_all_players()
    # Convertir cada ObjectId en los documentos
    return [transform_object_id(player) for player in players]

@router.post("/players")
async def add_player(player_data: dict):
    player_service.add_player(player_data)
    return {"success": True}

@router.get("/players/{name}")
async def get_player_by_name(name: str):
    player = player_service.find_player_by_name(name)
    if player:
        return transform_object_id(player)
    return {"error": "Player not found"}

@router.get("/team")
async def get_team():
    players = player_service.get_all_players()
    return [transform_object_id(player) for player in players]

@router.get("/rivals")
async def get_team():
    players = player_service.get_all_players()
    return [transform_object_id(player) for player in players]