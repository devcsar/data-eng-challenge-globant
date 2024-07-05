import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ASTRA_DB_ID = os.getenv('ASTRA_DB_ID')
    ASTRA_DB_REGION = os.getenv('ASTRA_DB_REGION')
    ASTRA_DB_KEYSPACE = os.getenv('ASTRA_DB_KEYSPACE')
    ASTRA_DB_APPLICATION_TOKEN = os.getenv('ASTRA_DB_APPLICATION_TOKEN')
    ASTRA_DB_ENDPOINT = os.getenv('ASTRA_DB_ENDPOINT')
    ASTRA_DB_SECURE_CONNECT_BUNDLE = os.getenv('ASTRA_DB_SECURE_CONNECT_BUNDLE')
    ASTRA_DB_CLIENT_ID = os.getenv('ASTRA_DB_CLIENT_ID')
    ASTRA_DB_SECRET = os.getenv('ASTRA_DB_SECRET')
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_REGION = os.getenv('AWS_REGION')
    S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
    UPLOAD_FOLDER = 'temp'
