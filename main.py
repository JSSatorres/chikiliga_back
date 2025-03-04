import uvicorn
from fastapi import FastAPI
from context.player.presentation.player_controller import PlayerController
from context.team.presentation.team_controller import TeamController
from context.market.presentation.market_controller import MarketController
from starlette.responses import RedirectResponse

app = FastAPI(
  title="Football Stats API",
  description="API to fetch football player stats from Comunio and Comuniazo",
  version="1.0"
)

player_controller = PlayerController()
team_controller = TeamController()
market_controller = MarketController()

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

app.include_router(player_controller.router, prefix="/players", tags=["players"])
app.include_router(team_controller.router, prefix="/teams", tags=["teams"])
app.include_router(market_controller.router, prefix="/markets", tags=["markets"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)