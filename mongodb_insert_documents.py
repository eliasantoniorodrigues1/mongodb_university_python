import datetime
import os

from dotenv import load_dotenv
from pymongo import MongoClient

# load config from .env file
load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI_LOCAL']

# connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# get reference to 'bank' database
db = client.bank

# get reference to accounts collection
accounts_collection = db.accounts

new_account = {
    "account_holder": "Linus Torvalds",
    "account_id": "MDBB29001337",
    "account_type": "checking",
    "balance": 50352434,
    "last_updated": datetime.datetime.utcnow(),
}

# write an expressiong that inserts the 'new_account' document into the
# 'accounts' collection.

# result = accounts_collection.insert_one(new_account)
# document_id = result.inserted_id
# print(f'_id of inserted document: {document_id}')

# insert many
documents = [
    {
        "account_holder": "Kratos of Spartan",
        "account_id": "MDBB29993337",
        "account_type": "checked",
        "balance": 150352434,
        "last_updated": datetime.datetime.utcnow(),
    },
    {
        "account_holder": "Michael Keaton",
        "account_id": "MDBB29001444",
        "account_type": "checking",
        "balance": 352434,
        "last_updated": datetime.datetime.utcnow(),
    }


]

result2 = db.bank.insert_many(documents)
document_ids = result2.inserted_ids
print("# of documents inserted: " + str(len(document_ids)))
print(f"_ids of inserted documents: {document_ids}")


client.close()
