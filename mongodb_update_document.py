from mongo_conn import mongo_uri
from bson import ObjectId


'''
   - update_one
   - $set
   - $push
   - upsert 
'''
client = mongo_uri('local')
db = client.local
id = ObjectId('640e5ef3192ca4d19d9e29d5')

for r in db.countries.find({'_id': id}):
    print(r)

# updating all the documents to insert a new field called language
db.countries.update_one(
    filter={'_id': id},
    update={'$set': {'language': 'portuguese'}}
)

# looping through all documents to add language
for r in db.countries.find({}):
    id = ObjectId(r['_id'])
    db.countries.update_one(filter={'_id': id}, update={
                            '$set': {'language': 'portuguese'}})


# upsert true to insert document if a filter dosn't match anything
# print(dir(db.countries.update_one))
ivory_coast = {'name': 'Ivory Coast', 'code': 225, 'language': 'french'}
db.countries.update_one(filter={'name': 'Ivory Coast'},
                        update={'$set': {'code': '225'}},
                        upsert=True)

# push operator add elements in an array
db.countries.update_one(filter={'_id': ObjectId('640f848fbb0ce3fe3f0580c4')},
                        update={'$push': {'population': 23740424}})

# select all data
#for r in db.countries.find({}):
#    print(r)


#for func in dir(db.countries):
#    if not func.startswith('_') and 'and' in func:
#        print(func, func.__doc__)
#        x = input()

# print(db.countries.find_and_update)