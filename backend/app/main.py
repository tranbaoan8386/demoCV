from fastapi import FastAPI

from app.core.database import Base
from app.core.database import engine

# Import model để SQLAlchemy biết model này tồn tại
from app.models.cv import CV

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Backend running"}