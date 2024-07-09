
import os
import pandas as pd

class Transformations:
    def __init__(self):
        self.pd = pd
        
    def drop_empty_rows(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Eliminar filas con columnas vacías.
        """
        df.dropna(inplace=True)
        return df
    
    def assign_column_names(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Asignar nombres de columnas manualmente.
        """
        
        column_names = ['id', 'name', 'datetime', 'department_id', 'job_id']
        if len(df.columns) != len(column_names):
            raise ValueError("The number of columns in the DataFrame does not match the number of column names provided")
        
        df.columns = column_names
        return df
    