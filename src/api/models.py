from astrapy.database import Database
from astrapy.collection import Collection
from astrapy.ids import ObjectId, uuid8, UUID
from config import Config

# class Department:
#     def __init__(self, client: AstraClient):
#         self.collection = client.collections(
#                             namespace=Config.ASTRA_DB_KEYSPACE, 
#                             collection_name='departments'
#                             )

#     def create(self, id, department):
#         document = {
#             "id": id,
#             "department": department
#         }
#         self.collection.create(document)

# class Job:
#     def __init__(self, client: AstraClient):
#         self.collection = client.collections(
#                             namespace=Config.ASTRA_DB_KEYSPACE, 
#                             collection_name='jobs'
#                             )

#     def create(self, id, job):
#         document = {
#             "id": id,
#             "job": job
#         }
#         self.collection.create(document)

class HiredEmployees:
    def __init__(self, db_client: Database):
        self.collection = db_client.get_collection("hired_employees")
        

    def create(self, id, name, datetime, department_id, job_id):
        
        document = {
            "id": int(id),
            "name": name,
            "datetime": datetime.isoformat(),
            "department_id": int(department_id),
            "job_id": int(job_id)
        }
        print(document)

        self.collection.insert_one(document)
       
            
            
