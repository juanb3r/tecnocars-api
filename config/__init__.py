from fastapi import FastAPI
from config import routers


app = FastAPI(
    title="Tecnocars API services",
    description="API services for Tecnocars",
    version="0.1",
    redoc_url="/redoc"
)

app.include_router(
    routers.urls,
)
