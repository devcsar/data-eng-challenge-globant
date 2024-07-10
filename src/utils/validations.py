import pandas as pd
from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd



class Validations:
    def __init__(self):
        self.pd = pd
    

    def validate_required_columns(self, df: pd.DataFrame) -> bool:
        """
        Asegurarse de que todas las columnas necesarias están presentes.
        """
        required_columns = ['id', 'name', 'datetime', 'department_id', 'job_id']
        if not all(column in df.columns for column in required_columns):
            raise ValueError("Missing required columns in the CSV file")


    def is_csv(self, file: File) -> bool:
        return file.filename.endswith('.csv')
    
    def max_rows_count(rows: list, max_rows: int) -> bool:
        return len(rows) > max_rows 
        
                
    # def have_header(self,)
    
    # def header_is_valid(self,)
        
        
    