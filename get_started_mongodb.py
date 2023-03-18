'''
MongoDB stores data in JSON-like documents, which makes the database very 
flexible and scalable.
To be able to experiment with the code examples in this tutorial, 
you will need access to a MongoDB database.
You can download a free MongoDB database at https://www.mongodb.com.
Or get started right away with a MongoDB cloud service at https://www.mongodb.com/cloud/atlas.

installation:
pip install pymongo

you will also need a mongodb drive to access the database.

i'm using mongodb Compass

'''
import pymongo


def create_database(db_name: str, connection: pymongo.MongoClient) -> str:
    # notice that: a database is not created until it gets content
    mydb = connection[db_name]
    print(connection.list_database_names())
    print(f'{db_name} was succesfully created!')
    return mydb


def create_collection(db_name, collection_name):
    mycol = db_name[collection_name]
    return mycol


def insert_data(data, collection):
    if type(data) == dict:
        x = collection.insert_one(data)
        print(f'Data {x.inserted_id} inserted succesfully!')       
    elif type(data) == list:
        x = collection.insert_many(data)
        print('Data inserted succesfully!')
        print(x.inserted_ids)        
    else:
        print('Invalid type. Please send a list or a dict to insert data.')


if __name__ == '__main__':
    # create mongodb connection
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    # instantiating a database and its collection
    mydb = myclient['test']
    mycol = mydb['test']

    # inserting one data
    # data = {'name': 'Quedma'}
    # insert_data(data, mycol)

    # to insert multiple data you need to pass a list of dicts
    # list_data = [{'name': 'Joseph'}, {'name': 'Marlos'}, {'name': 'Kim'}]
    # insert_data(list_data, mycol)

    # find one
    x = mycol.find_one()
    print(x)

    # find all - it retunrs an iterable
    x = mycol.find()
    for data in x:
        print(data)

    # filtering return
    for data in mycol.find(), {'name': 'Quedma'}:
        print(data)

    # quering data
    myquery = {'name': 'Quedma'}
    # returns a generator
    mydoc = mycol.find(myquery)

    for data in mydoc:
        print(data)

    # advanced query: using modifiers
    # $gt = greater than
    # $sort, $position, $slice, $push, $each, $addToSet
    myquery2 = {'name': {'$gt': 'Q'}}
    mydoc = mycol.find(myquery2)
    print('='* 60)
    for x in mydoc:
        print(x)

    # filtering with regular expressions
    myquery3 = {'name': {'$regex': '^[Kk]'}}
    mydoc = mycol.find(myquery3)
    print('*' * 60)
    for x in mydoc:
        print(x)
