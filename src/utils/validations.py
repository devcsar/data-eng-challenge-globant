import pandas as pd
from fastapi import File



class Validations:
    def __init__(self):
        self.pd = pd
    

    def validate_required_columns(self, df: pd.DataFrame) -> bool:
        """
        Asegurarse de que todas las columnas necesarias están presentes.
        """
        required_columns = ["id", "name", "datetime", "department_id", "job_id"]
        if not all(column in df.columns for column in required_columns):
            raise ValueError("Missing required columns in the CSV file")


    def is_csv(self, file: File) -> bool:
        return file.filename.endswith(".csv")
    
    def max_rows_count(rows: list, max_rows: int) -> bool:
        return len(rows) > max_rows 
        
                
    def have_header(self,csv_data: pd.DataFrame) -> tuple[bool, list]:
        validation= True
        columns = []
        return (validation, columns)
    
    def header_is_valid(self,column_names: list) -> bool:
        validation = None
        return validation
        
        
    