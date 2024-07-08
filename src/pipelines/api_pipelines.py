
from config import Config
from utils.read_write_ops import ReadWriteOps
from utils.validations import Validations
from utils.transformations import Transformations
from api.models import HiredEmployees
from api.db import session
from fastapi import File, HTTPException
import boto3



class APIPipelines:
    
    def __init__(self, file: File, http_exception: HTTPException):
        
        self.file = file
        self.http_exception = http_exception
        self.validations = Validations()
        self.rw_ops = ReadWriteOps()
        self.session = session
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id = Config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key = Config.AWS_SECRET_ACCESS_KEY,
            region_name = Config.AWS_REGION,
        )
        self.S3_BUCKET_NAME = Config.S3_BUCKET_NAME
        self.S3_RAW_DATA_DESTINATION = Config.S3_RAW_DATA_DESTINATION
        self.S3_REJECTED_DATA_DESTINATION = Config.S3_REJECTED_DATA_DESTINATION
        self.ENABLE_RAW_DATA = Config.ENABLE_RAW_DATA
        self.STREAM_FILE_CHUNKS_SIZE_KB = Config.STREAM_FILE_CHUNKS_SIZE_KB

        
        
    def upload_hired_employes() -> tuple [bool,dict]:
        
        
        
        
        
        return 1