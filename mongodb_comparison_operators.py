from mongo_conn import mongo_uri


client = mongo_uri('atlas')
db = client.sample_supplies

print(dir(db))

for r in db.list_collection_names():
    print(r)


# find one
# print(db.sales.find_one())

# comparison operators
for r in db.sales.find({'items.price': {'$gt': 2550}}):
    print(r)
    x = input()

q = {'items': {
    '$elemMatch': {
        'name': 'laptop',
        'price': {'$gt': 800},
        'quantity': {'$gte': 1}
    }
}
}
for r in db.sales.find(q):
    print(r)

