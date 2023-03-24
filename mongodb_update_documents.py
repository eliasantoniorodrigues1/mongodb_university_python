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

# filter
document_to_find = {'_id': ObjectId('641ba4c863d0d2e41555d5e3')}
result = accounts_collection.find_one(document_to_find)
print('Data before update:')
pprint.pprint(result)
print()

# update
add_balance = {'$inc': {'balance': 100}}
result = accounts_collection.update_one(document_to_find, add_balance)

print('Result after update:')
pprint.pprint(result.modified_count)
pprint.pprint(accounts_collection.find_one(document_to_find))

client.close()
