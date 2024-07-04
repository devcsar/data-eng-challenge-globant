from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    job_id: str
    department_id: str
