
from io import TextIOWrapper, StringIO
import csv
import pandas as pd
from fastapi import APIRouter, UploadFile, File, HTTPException
from .models import HiredEmployees
# from .db import astra_db
from .db import session
from utils.read_write_ops import ReadWriteOps
from utils.validations import Validations
from config import Config
from dateutil.parser import parse as parse_datetime
router = APIRouter()

# Inicializa operaciones de escritura y lectura
rw_ops = ReadWriteOps(Config)
#Inicializa validaciones
validations = Validations()

@router.post("/upload_csv/")
async def upload_csv(file: UploadFile = File(...)):
    object_name = f"uploads/{file.filename}"
    object_temp_name = f"temp/{file.filename}"
    # Validar la extensión del archivo
    validations.is_csv(file)
    
    #Validar filas por chunks (streamIO)
    csv_file_data = ReadWriteOps.read_stream_chunks(file)
    
    

    # Sube el archivo a S3
    rw_ops.upload_to_s3(file, object_name)
    # Descarga el archivo desde S3 para procesarlo
    try:
        # rw_ops.s3_client.download_file(Config.S3_BUCKET_NAME, object_name, f"temp/{file.filename}")
        rw_ops.download_from_s3(object_name,object_temp_name)
        
        df = pd.read_csv(object_temp_name)
        
        # Validar datos
        df = validations.assign_column_names(df)        
        df = validations.drop_empty_rows(df)
        validations.validate_required_columns(df)

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
