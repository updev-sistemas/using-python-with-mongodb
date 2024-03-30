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

accounts_target = {
    'account_type': {
        '$eq' : 'fixed_deposit'
    },
    'balance' : {
        '$gte' : 200
    }
}

new_balance = {
    '$set': {
        'balance': 0.00,
        'last_updated': datetime.datetime.now()
    }
}

beforeUpdate = accounts.find(accounts_target)
for account in beforeUpdate:
    print(f'Account with balance greater than or equal to 5000: {account["_id"]}')

result = accounts.update_many(accounts_target, new_balance)
pprint.pprint(result)

afterUpdate = accounts.find(accounts_target)
for account in afterUpdate:
    print(f'Account with balance greater than or equal to 5000: {account["_id"]}')

client.close()
