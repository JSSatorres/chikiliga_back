import uvicorn
from fastapi import FastAPI
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.responses import RedirectResponse

# from context.teams.infrastructure.routes import team_router
# from context.players.infrastructure.routes import player_router

app = FastAPI(
    title="Football Stats API",
    description="API to fetch football player stats from Comunio and Comuniazo",
    version="1.0"
)

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

# app.include_router(team_router, prefix="/teams", tags=["Teams"])
app.include_router(player_router, prefix="/players", tags=["Players"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
