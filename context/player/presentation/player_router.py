from fastapi import APIRouter
from context.player.presentation.player_controller import PlayerController
from context.player.application.player_service import PlayerService
from context.player.infrastructure.repositories.player_repository_impl import PlayerRepositoryImpl

def get_player_router() -> APIRouter:
    """
    Factory function that creates and configures the player router
    with its dependencies properly injected.
    """
    # Create dependency chain
    player_repository = PlayerRepositoryImpl()
    player_service = PlayerService(player_repository)
    player_controller = PlayerController(player_service)
    
    # Return the configured router
    return player_controller.router