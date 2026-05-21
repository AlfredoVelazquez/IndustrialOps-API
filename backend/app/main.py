from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title="IndustrialOps API",
    version="0.1.0",
    description="Sistema industrial para gestión de operaciones y producción"
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to IndustrialOps API"
    }