from app.models.cv import CV

# Create a CV instance in-memory without touching the DB engine
new_cv = CV(
    original_filename="test.pdf",
    object_name="cvs/test.pdf",
    status="PENDING",
)

assert new_cv.original_filename == "test.pdf"

print("Create success")