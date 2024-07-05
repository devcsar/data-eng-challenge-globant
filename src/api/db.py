# from astrapy.client import DataAPIClient
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from config import Config


# astra_db = DataAPIClient(
#                 Config.ASTRA_DB_APPLICATION_TOKEN
#                 ).get_database(
#                     Config.ASTRA_DB_ENDPOINT,
#                     namespace=Config.ASTRA_DB_KEYSPACE,
#                     )

def get_cluster():
    cloud_config = {
        'secure_connect_bundle': Config.ASTRA_DB_SECURE_CONNECT_BUNDLE
    }
    auth_provider = PlainTextAuthProvider(Config.ASTRA_DB_CLIENT_ID, Config.ASTRA_DB_SECRET)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    return cluster

def get_session():
    cluster = get_cluster()
    session = cluster.connect(Config.ASTRA_DB_KEYSPACE)
    return session

session = get_session()