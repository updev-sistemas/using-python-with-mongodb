import datetime
import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGO_DSN = os.environ['MONGO_DSN']

client = MongoClient(MONGO_DSN)

db = client.bank

accounts = db.accounts

my_account = {
    'account_id': {
        '$eq' : '99-1000-10001'
    }
}

result = accounts.delete_one(my_account)
pprint.pprint(result);

client.close()