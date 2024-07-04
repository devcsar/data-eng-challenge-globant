import os
import boto3
import pandas as pd
from datetime import datetime
from fastapi import APIRouter, UploadFile, File, HTTPException
from botocore.exceptions import NoCredentialsError
from .models import Department, Job, HiredEmployee
from .db import astra_client
from config import Config

router = APIRouter()

# Inicializa el cliente de S3
s3_client = boto3.client(
    's3',
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    region_name=Config.AWS_REGION
)

def upload_to_s3(file, bucket_name, object_name=None):
    if object_name is None:
        object_name = file.filename

    try:
        s3_client.upload_fileobj(file.file, bucket_name, object_name)
    except NoCredentialsError:
        raise HTTPException(status_code=403, detail="Credentials not available")

@router.post("/upload_csv/")
async def upload_csv(file: UploadFile = File(...)):
    object_name = f"uploads/{file.filename}"
    
    # Sube el archivo a S3
    upload_to_s3(file, Config.S3_BUCKET_NAME, object_name)

    # Descarga el archivo desde S3 para procesarlo
    try:
        s3_client.download_file(Config.S3_BUCKET_NAME, object_name, f"temp/{file.filename}")
        df = pd.read_csv(f"temp/{file.filename}")
        department_model = Department(astra_client)
        job_model = Job(astra_client)
        hired_employee_model = HiredEmployee(astra_client)

        for _, row in df.iterrows():
            hired_employee_model.create(
                id=row['id'],
                name=row['name'],
                datetime=datetime.strptime(row['datetime'], '%Y-%m-%d %H:%M:%S'),
                department_id=row['department_id'],
                job_id=row['job_id']
            )
        return {"message": "File successfully processed and data uploaded"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
