
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import dotenv
import os

dotenv.load_dotenv()

uri = os.getenv("mongo_uri")

def init_mongo_connection(uri):
    print('creating connection')
    client = MongoClient(uri, server_api=ServerApi('1'))
    return client

connection=init_mongo_connection(uri)

