from astrapy.client import AstraClient
from config import Config

class Department:
    def __init__(self, client: AstraClient):
        self.collection = client.collections(
                            namespace=Config.ASTRA_DB_KEYSPACE, 
                            collection_name='departments'
                            )

    def create(self, id, department):
        document = {
            "id": id,
            "department": department
        }
        self.collection.create(document)

class Job:
    def __init__(self, client: AstraClient):
        self.collection = client.collections(
                            namespace=Config.ASTRA_DB_KEYSPACE, 
                            collection_name='jobs'
                            )

    def create(self, id, job):
        document = {
            "id": id,
            "job": job
        }
        self.collection.create(document)

class HiredEmployee:
    def __init__(self, client: AstraClient):
        self.collection = client.collections(
                            namespace=Config.ASTRA_DB_KEYSPACE, 
                            collection_name='hired_employees'
                            )

    def create(self, id, name, datetime, department_id, job_id):
        document = {
            "id": id,
            "name": name,
            "datetime": datetime.isoformat(),
            "department_id": department_id,
            "job_id": job_id
        }
        self.collection.create(document)
