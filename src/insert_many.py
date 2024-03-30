import datetime
import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGO_DSN = os.environ['MONGO_DSN']

client = MongoClient(MONGO_DSN)

db = client.bank

accounts = db.accounts

list_new_accounts = [
    {
        "account_holder": "Mrs. Allison Zieme",
        "account_id": "102-4321-20003",
        "account_type": "digital_checking",
        "balance": 133.28,
        "created_at": datetime.datetime.now(),
        "last_updated": datetime.datetime.now()
    },
    {
        "account_holder": "Mr. Allan Kuhn",
        "account_id": "99-1000-10004",
        "account_type": "digital_checking",
        "balance": 123.48,
        "created_at": datetime.datetime.now(),
        "last_updated": datetime.datetime.now()
    }
]

results = accounts.insert_many(list_new_accounts)
print(f'Documents insert successfully with ids: {results.inserted_ids}')

client.close()