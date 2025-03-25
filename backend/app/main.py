from fastapi import FastAPI
from app.routes import error_routes, auth_routes, stats_routes

app = FastAPI()

app.include_router(auth_routes.router, prefix="/api/auth")
app.include_router(error_routes.router, prefix="/api/errors")
app.include_router(stats_routes.router, prefix="/api/stats")

@app.get("/")
async def root():
    return {"message": "Welcome to Error Logger API"}
