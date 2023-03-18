from mongo_conn import mongo_uri


client = mongo_uri('atlas')
db = client.sample_training

# logical operators $and e $or
'''
q = {
    '$and': [
        {'dst_airport': 'SEA'},
        {'src_airport': 'SEA'}
    ]
}

for r in db.routes.find(q):
    print(r)
'''

q2 = {
    '$and': [
        {'$or': [
            {'dst_airport': 'SEA'},
            {'src_airport': 'SEA'}
        ]},
        {'$or': [
            {'airplane': 'American Airlines'},
            {'airplane': 320},
        ]},
    ]
}

for r in db.routes.find(q2):
    print(r)