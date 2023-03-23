import datetime
import os

from dotenv import load_dotenv
from pymongo import MongoClient
import pprint
from bson.objectid import ObjectId

# load config from .env file
load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI_LOCAL']

# connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# get reference to 'bank' database
db = client.bank

# get reference to accounts collection
accounts_collection = db.bank

# ========== RESULT ==============================================
# find one
# document_to_find = {"_id": ObjectId("641b9b7e50bf6c85705a96ab")}
# result = accounts_collection.find_one(document_to_find)
# pprint.pprint(result['account_holder'])

# ========== CURSOR ==============================================
# find many
document_to_find = {"balance": {"$gt": 4700}}
# cursor needs to be iterate
cursor = accounts_collection.find(document_to_find)
num_docs = 0
for document in cursor:
    num_docs += 1
    pprint.pprint(document)
    print()

client.close()
