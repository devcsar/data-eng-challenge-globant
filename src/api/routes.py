
from fastapi import APIRouter, UploadFile, File, HTTPException
# from .db import astra_db
from .db import session
from pipelines.api_pipelines import APIPipelines
from pipelines.stats_pipelines import StatsPipelines

router = APIRouter()

api_pipelines = APIPipelines()
stats_pipelines = StatsPipelines()


@router.post("/upload_csv/")
async def upload_csv(file: UploadFile = File(...)):
    
    try:
        pipeline_succeed, pipeline_message = \
            await api_pipelines.ingest_hired_employes_csv(session,file)
        if not pipeline_succeed:
            raise HTTPException(status_code=400, detail=pipeline_message)
        return pipeline_message
    except HTTPException as http_exp:
        raise http_exp
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

    # Sube el archivo a S3
    # rw_ops.upload_to_s3(file, object_name)
    # Descarga el archivo desde S3 para procesarlo
    
    
    # try:
    #     # rw_ops.s3_client.download_file(Config.S3_BUCKET_NAME, object_name, f"temp/{file.filename}")
    #     rw_ops.download_from_s3(object_name,object_temp_name)
        
    #     df = pd.read_csv(object_temp_name)
        
    #     # Validar datos
    #     df = validations.assign_column_names(df)        
    #     df = validations.drop_empty_rows(df)
    #     validations.validate_required_columns(df)

    #     hired_employee_model = HiredEmployees(session)

    #     for _, row in df.iterrows():
    #         hired_employee_model.create(
    #             id=int(row['id']),
    #             name=row['name'],
    #             datetime=parse_datetime(row['datetime']),
    #             department_id=int(row['department_id']),
    #             job_id=int((row['job_id']))
    #         )
    #     return {"message": "File successfully processed and data uploaded"}
    # except Exception as e:
    #     print(e)
    #     raise HTTPException(status_code=500, detail=str(e))
