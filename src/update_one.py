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

new_balance = {
    '$set': {
        'balance': 100.00,
        'last_updated': datetime.datetime.now()
    }
}

beforeUpdate = accounts.find_one(my_account)
pprint.pprint(beforeUpdate)

result = accounts.update_one(my_account, new_balance)
pprint.pprint(result)

afterUpdate = accounts.find_one(my_account)
pprint.pprint(afterUpdate)


add_new_attr = {
    '$set': {
        'minimum_balance': 500.00
    }
}

resultWithNewAttr = accounts.update_one(my_account, add_new_attr)
pprint.pprint(resultWithNewAttr)

afterUpdateWithNewAttr = accounts.find_one(my_account)
pprint.pprint(afterUpdateWithNewAttr)


rm_attr_past = {
    '$unset': {
        'minimum_balance': ""
    }
}

resultWithRmvAttr = accounts.update_one(my_account, rm_attr_past)
pprint.pprint(resultWithRmvAttr)

afterUpdateWithRmvAttr = accounts.find_one(my_account)
pprint.pprint(afterUpdateWithRmvAttr)

client.close()