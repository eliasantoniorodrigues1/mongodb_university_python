from dotenv import dotenv_values
from pymongo import MongoClient


def mongo_uri(type: str) -> MongoClient():
    if type.lower() == 'local':
        MONGODB_URI = 'mongodb://localhost:27017'    
        client = MongoClient(MONGODB_URI)
        return client
    elif type.lower() == 'atlas':
        user_auth = dotenv_values('.env')
        MONGODB_URI = f'mongodb+srv://{user_auth["USER"]}:{user_auth["PASSWORD"]}@cursemongodbasics.9w17tyv.mongodb.net/test'
        client = MongoClient(MONGODB_URI)
        return client
    else:
        print('Invalid type of connection. Send (local or Atlas)')

if __name__ == '__main__':
    print(mongo_uri('Atlas'))
