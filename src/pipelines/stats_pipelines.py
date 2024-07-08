
from config import Config
from ..utils.read_write_ops import ReadWriteOps
from ..utils.validations import Validations
from ..utils.transformations import Transformations
from fastapi import APIRouter, UploadFile, File, HTTPException

class StatsPipelines:
    def __init__(self, ):
        self.config = Config