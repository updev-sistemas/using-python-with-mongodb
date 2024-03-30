import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGO_DSN = os.environ['MONGO_DSN']

client = MongoClient(MONGO_DSN)

# List all databases in the cluster.
for db_name in client.list_database_names():
    print(db_name)

client.close()