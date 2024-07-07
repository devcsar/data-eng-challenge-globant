
import boto3
import pandas as pd
from botocore.exceptions import NoCredentialsError
from fastapi import APIRouter, UploadFile, File, HTTPException
import csv
from io import StringIO


class ReadWriteOps:
    def __init__(self, config):
        self.config = config
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
            region_name=config.AWS_REGION,
        )

    def upload_to_s3(self, file, object_name=None):
        if object_name is None:
            object_name = file.filename

        try:
            self.s3_client.upload_fileobj(file.file, self.config.S3_BUCKET_NAME, object_name)
        except NoCredentialsError:
            raise HTTPException(status_code=403, detail="Credentials not available")
        
    def download_from_s3(self, object_name: str, file):
        try:
            self.s3_client.download_file(self.config.S3_BUCKET_NAME, object_name, file)
            df = pd.read_csv(file)
            return df
        except NoCredentialsError:
            raise HTTPException(status_code=403, detail="Credentials not available")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    async def read_stream_chunks(self, file: File) -> pd.DataFrame:
        
        # Limitar el tamaño máximo de las primeras 100 filas
        max_rows = int(self.config.ROWS_LIMIT)
        rows = []
        reader = None

        # Definir el tamaño del chunk (por ejemplo, 1024 bytes)
        chunk_size = self.config.ROWS_LIMITSTREAM_FILE_CHUNKS_SIZE_KB
        
        # Procesar el archivo en partes mientras se sube
        while True:
            chunk = await file.read(chunk_size)
            if not chunk:
                break

            if reader is None:
                # Inicializar el lector CSV en el primer chunk
                reader = csv.reader(StringIO(chunk.decode('utf-8')))
            else:
                # Continuar leyendo del archivo
                reader = csv.reader(StringIO(chunk.decode('utf-8')), reader.dialect)
            
            for row in reader:
                rows.append(row)
                if len(rows) > max_rows:
                    raise HTTPException(status_code=400, detail="El archivo contiene más de 1000 filas.")

            if len(rows) >= max_rows:
                break

        # Convertir las filas a un DataFrame de pandas
        df = pd.DataFrame(rows[:max_rows])
        
        return df
        
