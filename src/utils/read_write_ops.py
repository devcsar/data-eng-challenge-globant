
import boto3
import pandas as pd
from botocore.exceptions import NoCredentialsError
from fastapi import HTTPException

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
        
    def download_from_s3(self, object_name, file):
        try:
            self.s3_client.download_file(self.config.S3_BUCKET_NAME, object_name, file)
            df = pd.read_csv(file)
            return df
        except NoCredentialsError:
            raise HTTPException(status_code=403, detail="Credentials not available")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))