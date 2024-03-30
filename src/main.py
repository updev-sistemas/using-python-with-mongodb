from pymongo import MongoClient

# Set the value of MONGODB_URI to your Atlas connection string.
MONGODB_URI = 'mongodb://localhost:27017/?readPreference=primary&directConnection=true&ssl=false'

# Connect to your MongoDB cluster.
client = MongoClient(MONGODB_URI)

# List all databases in the cluster.
for db_name in client.list_database_names():
    print(db_name)
