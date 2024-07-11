# from astrapy.database import Database
# from astrapy.collection import Collection
# from astrapy.ids import ObjectId, uuid8, UUID
from cassandra.cluster import Session
from cassandra.query import SimpleStatement
from config import Config

class Department:
    def __init__(self, session: Session):
        self.session = session

    def create(self, id, department):
        query = SimpleStatement(f"""
                                INSERT INTO {Config.ASTRA_DB_KEYSPACE}.departments 
                                (id, department)
                                VALUES (%s, %s)
                                """)
        self.session.execute(query, (id, department))

class Job:
    def __init__(self, session: Session):
        self.session = session

    def create(self, id, job):
        query = SimpleStatement(f"""
                                INSERT INTO {Config.ASTRA_DB_KEYSPACE}.jobs (id, job)
                                VALUES (%s, %s)
                                """)
        self.session.execute(query, (id, job))

class HiredEmployees:
    
    column_names = ['id', 'nombre', 'fecha_registro']
    column_types = ['int', 'str', 'datetime']
    schema = zip(column_names, column_types)
    
    def __init__(self, session: Session):
        self.session = session

    def create(self, id, name, datetime, department_id, job_id):
        query = SimpleStatement(f"""
                                INSERT INTO {Config.ASTRA_DB_KEYSPACE}.hired_employees 
                                    (id, name, datetime, department_id, job_id)
                                VALUES 
                                    (%s, %s, %s, %s, %s);
                                """)
        self.session.execute(query, (id, name, datetime, department_id, job_id))       
            
            
