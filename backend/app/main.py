from fastapi import FastAPI

from app.core.database import Base
from app.core.database import engine
from app.api.routes.cv_routes import router as cv_router

# Import model để SQLAlchemy biết model này tồn tại
from app.models.cv import CV

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(cv_router)


@app.get("/")
def root():
    return {"message": "Backend running"}