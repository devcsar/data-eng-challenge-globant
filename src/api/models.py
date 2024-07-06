# from astrapy.database import Database
# from astrapy.collection import Collection
# from astrapy.ids import ObjectId, uuid8, UUID
from cassandra.cluster import Session
from cassandra.query import SimpleStatement
from config import Config

# class HiredEmployees:
#     def __init__(self, db_client: Database):
#         self.collection = db_client.get_collection("hired_employees")
        

#     def create(self, id, name, datetime, department_id, job_id):
        
#         document = {
#             "id": int(id),
#             "name": name,
#             "datetime": datetime.isoformat(),
#             "department_id": int(department_id),
#             "job_id": int(job_id)
#         }
#         print(document)

#         self.collection.insert_one(document)

class HiredEmployees:
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
            
            
