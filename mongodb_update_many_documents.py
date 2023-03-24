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

# update filter - this filter needs to return more than one value
select_accounts = {'account_type': 'checking'}
set_field = {'$set': {'minimum_balance': 100}}

# update many
result = accounts_collection.update_many(select_accounts, set_field)
print(f'Documents matched: {result.matched_count}')
print(f'Documents matched: {result.modified_count}')
pprint.pprint(accounts_collection.find_one(select_accounts))

client.close()
