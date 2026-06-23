from app.core.database import SessionLocal
from app.models.cv import CV

db = SessionLocal()

new_cv = CV(
    filename="test.pdf"
)

db.add(new_cv)

db.commit()

print("Insert success")