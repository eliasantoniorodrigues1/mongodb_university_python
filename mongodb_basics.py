from mongo_conn import mongo_uri
from bson import ObjectId

client = mongo_uri('atlas')
db = client.sample_training

# finding documents
# for r in db.zips.find({'state': 'AZ'}):
#    print(r)

# $in operator
q = {'city': {'$in': ['PHOENIX', 'CHICAGO']}}
# for r in db.zips.find(q):
#    print(r)

# $eq
id = ObjectId('5c8eccc1caa187d17ca7080a')
q = {'_id': id}
for r in db.zips.find(q):
    print(r)
