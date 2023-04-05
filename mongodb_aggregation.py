import datetime
import os

from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

# load config from .env file
load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI_LOCAL']

# connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# get reference to 'bank' database
db = client.bank

# get reference to accounts collection
accounts_collection = db.bank

# inserting data
'''
data = [
    {
        'account_holder': 'Cravinho Love',
        'account_id': 'MDBB23423423',
        'account_type': 'savings',
        'balance': 950.12,
        'last_updated': datetime.datetime(2023, 3, 23, 1, 0, 56, 322000)
    },
    {
        'account_holder': 'Melina Mel',
        'account_id': 'ABDEC3423423',
        'account_type': 'savings',
        'balance': 150.12,
        'last_updated': datetime.datetime(2023, 3, 23, 1, 0, 56, 322000)
    },
    {
        'account_holder': 'Falcony José',
        'account_id': 'KXYZ3423423',
        'account_type': 'checking',
        'balance': 450.12,
        'last_updated': datetime.datetime(2023, 3, 23, 1, 0, 56, 322000)
    },        
]

result = accounts_collection.insert_many(data)
print(result)

'''

# the filters needs to be in order, this is why we filter the accounts with
# less than $1000
# select accounts with balances of less than $1000
select_by_balance = {'$match': {'balance': {'$lt': 1000}}}

# separate documents by account type and calculate the average balance of each account type.
separate_by_account__calculate_avg_balance = {
    '$group': {'_id': '$account_type', 'avg_balance': {'$avg': '$balance'}}
}

# pipeline
pipeline = [
    {
        '$match': {'balance': {'$lt': 1000}}
    },
    {
        '$group': {
            '_id': '$account_type',
            'average': {'$avg': '$balance'}
        }
    },
]

# aggregation
results = accounts_collection.aggregate(pipeline)
for item in results:
    pprint.pprint(item)

client.close()
