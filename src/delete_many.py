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

account_with_balance_lte_100 = {
    'balance' : {
        '$lte' : 200
    },
    'account_type': {
        '$ne' : 'fixed_deposit'
    }
}

result = accounts.delete_many(account_with_balance_lte_100)
for account in result:
    print(f'Account with balance less than or equal to 100: {account["_id"]}')
    pprint.pprint(account);

client.close()