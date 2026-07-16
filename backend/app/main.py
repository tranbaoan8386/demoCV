from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.cv_routes import router as cv_router

from app.models.cv import CV

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cv_router)


@app.get("/")
def root():
    return {"message": "Backend running"}