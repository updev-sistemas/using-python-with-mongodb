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

pipeline = [
    {
        '$match': {
            'account_type': {
                '$in': ['credit', 'loan']
            },
            'balance': {
                '$gte': 500,
                '$lte': 600
            }
        }
    },
    {
        '$project': {
            '_id': 0,
            'account_id': 1,
            'account_holder': {
                '$toUpper': '$account_holder'
            },
            'account_type': {
                '$toUpper': '$account_type'
            },
            'balance': {
                '$concat': [
                    "R$ ",
                    {
                        '$toString': {
                            '$round': ["$balance", 2]
                        }
                    }
                ]
            },
            'created_at': {
                '$dateToString': {
                    'format': "%d/%m/%Y %H:%M",
                    'date': "$created_at"
                }
            },
            'last_updated': {
                '$dateToString': {
                    'format': "%d/%m/%Y %H:%M",
                    'date': "$last_updated"
                }
            }
        }
    },
    {
        '$sort': {
            'account_holder': 1
        }
    }
]

result = accounts.aggregate(pipeline)
for account in result:
    pprint.pprint(account);


client.close()