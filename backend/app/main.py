from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.health import router as health_router
from app.api.machine_routes import router as machine_router
from app.routes import user_routes
from app.routes import auth_routes

app = FastAPI(
    title="IndustrialOps API",
    version="0.1.0",
    description="Sistema industrial para gestión de operaciones y producción"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(machine_router)
app.include_router(user_routes.router)
app.include_router(auth_routes.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to IndustrialOps API"
    }