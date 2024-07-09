
from config import Config
from utils.read_write_ops import ReadWriteOps
from utils.validations import Validations
from utils.transformations import Transformations
from api.models import HiredEmployees
from api.db import session
from fastapi import File, HTTPException
from typing import List, Tuple, Dict, Union, Any
import boto3
class APIPipelines:
    
    def __init__(self):
        
        self.http_exception = HTTPException
        self.validations = Validations()
        
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id = Config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key = Config.AWS_SECRET_ACCESS_KEY,
            region_name = Config.AWS_REGION,
        )
        self.S3_BUCKET_NAME = Config.S3_BUCKET_NAME
        self.S3_RAW_DATA_DESTINATION = Config.S3_RAW_DATA_DESTINATION
        self.S3_REJECTED_DATA_DESTINATION = Config.S3_REJECTED_DATA_DESTINATION
        self.rw_ops = ReadWriteOps(Config,self.s3_client)
        self.session = session
        self.ENABLE_RAW_DATA = Config.ENABLE_RAW_DATA
        self.STREAM_FILE_CHUNKS_SIZE_KB = Config.STREAM_FILE_CHUNKS_SIZE_KB

        
        
    async def ingest_hired_employes_csv(self, file: File) -> Tuple[bool, str]:
                
        self.validations.is_csv(file)
        
        csv_file_data =  await self.rw_ops.read_stream_chunks(file)
