import datetime
import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGO_DSN = os.environ['MONGO_DSN']

client = MongoClient(MONGO_DSN)

db = client.bank

accounts = db.accounts

new_account = {
    "account_holder": "Antonio Jose",
    "account_id": "99-1000-10001",
    "account_type": "digital_checking",
    "balance": 13.88,
    "created_at": datetime.datetime.now(),
    "last_updated": datetime.datetime.now()
};


result = accounts.insert_one(new_account)
print(f'Document insert successfully with id: {result.inserted_id}')

client.close()