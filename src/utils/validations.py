import pandas as pd
from fastapi import APIRouter, UploadFile, File, HTTPException



class Validations:
    def drop_empty_rows(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Eliminar filas con columnas vacías.
        """
        df.dropna(inplace=True)
        return df

    def validate_required_columns(self, df: pd.DataFrame) -> None:
        """
        Asegurarse de que todas las columnas necesarias están presentes.
        """
        required_columns = ['id', 'name', 'datetime', 'department_id', 'job_id']
        if not all(column in df.columns for column in required_columns):
            raise ValueError("Missing required columns in the CSV file")

    def assign_column_names(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Asignar nombres de columnas manualmente.
        """
        
        column_names = ['id', 'name', 'datetime', 'department_id', 'job_id']
        if len(df.columns) != len(column_names):
            raise ValueError("The number of columns in the DataFrame does not match the number of column names provided")
        
        df.columns = column_names
        return df
    
    def is_csv(self, file: File) -> bool:
        validation_pass = None
        if not file.filename.endswith('.csv'):
            raise HTTPException(status_code=400, 
                                detail="El archivo debe tener la extensión .csv")
    
    def max_rows_count(rows: list, max_rows: int) -> None:
        if len(rows) > max_rows:
                    raise HTTPException(status_code=400, detail="El archivo contiene más de 1000 filas.")
        
        
    