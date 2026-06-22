from minio import Minio

client = Minio(
    "localhost:9000",
    access_key="admin",
    secret_key="password123",
    secure=False
)

buckets = client.list_buckets()

print("Connected successfully!")
print("Buckets:", [bucket.name for bucket in buckets])