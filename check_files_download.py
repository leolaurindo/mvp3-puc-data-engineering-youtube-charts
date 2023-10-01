from google.cloud import storage
from dotenv import load_dotenv
import os

load_dotenv()

storage_client = storage.Client()

bucket_name = 'yt-charts-raw'

bucket = storage_client.bucket(bucket_name)

blobs = bucket.list_blobs()

print(f"Files in {bucket_name}:")

count = 0

for blob in blobs:
    print(blob.name)
    count +=1

print(f"{count} files")