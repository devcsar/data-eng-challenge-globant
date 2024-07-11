
from config import Config
from utils.read_write_ops import ReadWriteOps
from utils.validations import Validations
from utils.transformations import Transformations
from cassandra.cluster import Session
from fastapi import File
from typing import List, Tuple, Dict, Union, Any
import boto3
class APIPipelines:
    
    def __init__(self):
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
        self.ENABLE_RAW_DATA = bool(Config.ENABLE_RAW_DATA)
        self.STREAM_FILE_CHUNKS_SIZE_KB = Config.STREAM_FILE_CHUNKS_SIZE_KB
        self.ROWS_LIMIT = Config.ROWS_LIMIT
        
    async def ingest_hired_employes_csv(self, session: Session, file: File) -> Tuple[bool, str]:
        '''
            Run sequential operations to process hired_employes csv
        '''
        validation = None
        
        # validate if selected file have .csv extension
        validation = self.validations.is_csv(file)
        if not validation:
            return (validation, 'The file must have .CSV extension')   
        
        # While upload streaming validate if file exceeds the row limit
        # define by ROWS_LIMIT env variable
        validation, csv_data =  await self.rw_ops. \
                            read_stream_chunks(file,
                                            self.ROWS_LIMIT, 
                                            self.STREAM_FILE_CHUNKS_SIZE_KB
                                            )
        if not validation:
            return (validation, 'The selected file exceeds the rows limit. (1000)')
        
        # validate if file have a header
        validation, column_names  = self.validations.have_header(csv_data)
        if not validation:
            return (validation, 'The selected file exceeds the rows limit. (1000)')
            
        
        
        # validate if header is valid with column names of 
        # -- hired_employees model: id, name, datetime, department_id, job_id
        validation = self.validations.header_is_valid(column_names)
        
        
        # pending -- if file have a header read ROWS_LIMIT +1 to take into account header
        
        # clean csv data (delete rows with empty columns)
        
        # validate rows with expected_types = [int, datetime, int, int]
        
        # create a file with rejected rows with extra column called_rejected-reason 
        # -- y guardarlo en S3_REJECTED_DATA_DESTINATION
        
        # if ENABLE_RAW_DATA is true then store a copy of the file clean in csv format in the
        # -- S3_RAW_DATA_DESTINATION
        
        # Process dataframe to store each row in Astra table, but taking into account the next validations: 
        # -- validate if id is unique (query table to find)
        # -- validate if department_id exist in departments table
        # -- validate if job_id exist in jobs table
        # -- once validated all above store row in astra table
        
        # return message to endpoint in routes

        
