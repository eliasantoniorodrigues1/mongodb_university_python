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

# to calculate the balance in GBP, divide the original balance by the conversion rate
conversion_rate_usd_to_gbp = 1.3

# select checking accounts with balances of more than $1.500
select_accounts = {'$match': {
    'account_type': 'checking', 'balance': {'$gt': 1500}}}

# organize documents in order from highest balance to lowest.
organize_by_original_balance = {'$sort': {'balance': -1}}

# return only the account type & balance fields, plus a new field containing
# balance in great british pounds (GPB).
return_specified_fields = {
    '$project': {
        'account_type': 1,
        'balance': 1,
        'gbp_balance': {'$divide': ['$balance', conversion_rate_usd_to_gbp]},
        '_id': 0
    }
    }

# create an aggregation pipeline containing the four stages created above
pipeline = [
    select_accounts,
    organize_by_original_balance,
    return_specified_fields
    ]

# perform an aggregation on 'pipeline'
results = accounts_collection.aggregate(pipeline)

print(
    'Account type, original balance and balance in GBP of checking accounts with original balance greater than $1.500'
    'in order from highest original balance to lowest: ', '\n'
    )

for item in results:
    pprint.pprint(item)

client.close()
