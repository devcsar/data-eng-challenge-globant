import os
import boto3
import pandas as pd
from datetime import datetime
from fastapi import APIRouter, UploadFile, File, HTTPException
from botocore.exceptions import NoCredentialsError
from .models import HiredEmployees
# from .db import astra_db
from .db import session
from config import Config
from dateutil.parser import parse as parse_datetime
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

def validate_and_clean_data(df):
    # Eliminar filas con columnas vacías
    df.dropna(inplace=True)
    
    # Asegurarse de que todas las columnas necesarias están presentes
    required_columns = ['id', 'name', 'datetime', 'department_id', 'job_id']
    if not all(column in df.columns for column in required_columns):
        raise ValueError("Missing required columns in the CSV file")
    
    return df
@router.post("/upload_csv/")
async def upload_csv(file: UploadFile = File(...)):
    object_name = f"uploads/{file.filename}"
    
    # Sube el archivo a S3
    upload_to_s3(file, Config.S3_BUCKET_NAME, object_name)

    # Descarga el archivo desde S3 para procesarlo
    try:
        s3_client.download_file(Config.S3_BUCKET_NAME, object_name, f"temp/{file.filename}")
        df = pd.read_csv(f"temp/{file.filename}")
        
        # Asignar nombres de columnas manualmente
        df.columns = ['id', 'name', 'datetime', 'department_id', 'job_id']
        
        # Validar y limpiar los datos
        df = validate_and_clean_data(df)

        hired_employee_model = HiredEmployees(session)

        for _, row in df.iterrows():
            hired_employee_model.create(
                id=int(row['id']),
                name=row['name'],
                datetime=parse_datetime(row['datetime']),
                department_id=int(row['department_id']),
                job_id=int((row['job_id']))
            )
        return {"message": "File successfully processed and data uploaded"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
