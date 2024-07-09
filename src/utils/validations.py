import pandas as pd
from fastapi import APIRouter, UploadFile, File, HTTPException



class Validations:
    

    def validate_required_columns(self, df: pd.DataFrame) -> bool:
        """
        Asegurarse de que todas las columnas necesarias están presentes.
        """
        required_columns = ['id', 'name', 'datetime', 'department_id', 'job_id']
        if not all(column in df.columns for column in required_columns):
            raise ValueError("Missing required columns in the CSV file")


    def is_csv(self, file: File) -> bool:
        if not file.filename.endswith('.csv'):
            return False
        else:
            return True
            
            
            raise HTTPException(status_code=400, 
                                detail="El archivo debe tener la extensión .csv")
    
    def max_rows_count(rows: list, max_rows: int) -> bool:
        if len(rows) > max_rows:
                    raise HTTPException(status_code=400, detail="El archivo contiene más de 1000 filas.")
        
        
    