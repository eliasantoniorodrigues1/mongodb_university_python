from mongo_conn import mongo_uri
from bson import ObjectId


client = mongo_uri('local')
db = client.local
id = ObjectId('640e5ef3192ca4d19d9e29d5')

# verifying data
for r in db.countries.find({'_id': id}):
    print(r)

# replace document
country = {'name': 'Namibia', 'code': 264}
r = db.countries.replace_one(filter={'_id': id}, replacement=country)
print(f'Raw Result: {r.raw_result}')
print(f'Acknowledged: {r.acknowledged}')

# select all data from table
for r in db.countries.find({}):
    print(r)
