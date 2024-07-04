from astrapy.client import DataAPIClient
from config import Config

astra_client = DataAPIClient(Config.ASTRA_DB_APPLICATION_TOKEN)
db = astra_client.get_database_by_api_endpoint(
                    Config.ASTRA_DB_ENDPOINT,
                    namespace=Config.ASTRA_DB_KEYSPACE,
                    )


# astra_client = DataAPIClient(
#     astra_database_id=Config.ASTRA_DB_ID,
#     astra_database_region=Config.ASTRA_DB_REGION,
#     astra_application_token=Config.ASTRA_DB_APPLICATION_TOKEN
# )
