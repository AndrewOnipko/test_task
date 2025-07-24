from fastapi import FastAPI
from app.routers import report_routes, test_routes

app = FastAPI(title="Log Report API")

app.include_router(report_routes.router)
app.include_router(test_routes.router)