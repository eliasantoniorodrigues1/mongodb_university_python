# Simple repository to Study MongoDB Locally

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

## Basics Steps
        import pymongo

        # connection
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")


### Create database

*Notice that: A database is not created until it gets content*

      mydb = myclient['test']


### Create a collection

      # create a collection called "test_collection"
      mycol = mydb['test_collection']

### Insert data

  - Inserting a single data
  
        data = {'name': 'Joseph'}
        x = mycol.insert_one(data)

  - Inserting multiple records

        list_data = [{'name': 'Joseph'}, {'name': 'Marlos'}, {'name': 'Kim'}]
        x = mycol.insert_many(list_data)        

### Quering data

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


### Sorting data

        import pymongo

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["customers"]

        mydoc = mycol.find().sort("name")

        for x in mydoc:
          print(x)


### Deleting Documents

  - One

          import pymongo

          myclient = pymongo.MongoClient("mongodb://localhost:27017/")
          mydb = myclient["mydatabase"]
          mycol = mydb["customers"]

          myquery = { "address": "Mountain 21" }

          mycol.delete_one(myquery)

  - Many

        import pymongo

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["customers"]

        myquery = { "address": {"$regex": "^S"} }

        x = mycol.delete_many(myquery)

        print(x.deleted_count, " documents deleted.")


### Drop Collection

        import pymongo

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["customers"]

        mycol.drop()


### Update

        import pymongo

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["customers"]

        myquery = { "address": "Valley 345" }
        newvalues = { "$set": { "address": "Canyon 123" } }

        mycol.update_one(myquery, newvalues)

        #print "customers" after the update:
        for x in mycol.find():
          print(x)


### DB Limit Result

        import pymongo

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["customers"]

        myresult = mycol.find().limit(5)

        #print the result:
        for x in myresult:
          print(x)


### Sources: 

HowTO:
 - [W3School](https://www.w3schools.com/python/python_mongodb_getstarted.asp)

Installation:
 - [PrismaIO](https://www.prisma.io/dataguide/mongodb/setting-up-a-local-mongodb-database)