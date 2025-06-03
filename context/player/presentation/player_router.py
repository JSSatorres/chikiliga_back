from fastapi import APIRouter
from context.player.presentation.player_controller import PlayerController
from context.player.infrastructure.repositories.player_repository_impl import PlayerRepositoryImpl

# Importar casos de uso individuales
from context.player.application.create_player import CreatePlayer
from context.player.application.get_player import GetPlayer
from context.player.application.get_all_players import GetAllPlayers
from context.player.application.delete_player import DeletePlayer

def get_player_router() -> APIRouter:
    """
    Factory function that creates and configures the player router
    with its dependencies properly injected.
    """
    # 1. Crear el repositorio
    player_repository = PlayerRepositoryImpl()
    
    # 2. Crear todos los casos de uso
    create_player_use_case = CreatePlayer(player_repository)
    get_player_use_case = GetPlayer(player_repository)
    get_all_players_use_case = GetAllPlayers(player_repository)
    delete_player_use_case = DeletePlayer(player_repository)
    
    # 3. Crear el controlador e inyectar los casos de uso
    player_controller = PlayerController(
        create_player_use_case=create_player_use_case,
        get_player_use_case=get_player_use_case,
        get_all_players_use_case=get_all_players_use_case,
        delete_player_use_case=delete_player_use_case
    )
    
    # 4. Devolver el router configurado
    return player_controller.router