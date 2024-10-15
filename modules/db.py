from contextlib import contextmanager
from os import getenv

from pymongo import MongoClient
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Database():
    def __init__(self):
        self.client = MongoClient(getenv('MONGO_CLIENT_LOCAL'))
        self.db = self.client['dbms_course']
        self.user_collection = self.db['users']
        self.catalog_collection = self.db['catalog']

    def insert_one(self, data: BaseModel, collection_name):
        try:
            data = data.dict()
            return collection_name.insert_one(data)
        except:
            print('insertion error')

    def insert_many(self, data, collection_name):
        return collection_name.insert_many(data)
    
    def find_all(self, collection_name):
        return collection_name.find()
    
    def find_by_filter(self, filter, collection_name):
        return collection_name.find(filter)
    
    def find_one_by_id(self, id, collection_name):
        return collection_name.find(id)
    
    def update_one(self, filter, updated_data, collection_name):
        return collection_name.update_one(filter, {'$set' : updated_data})
    
    def update_many(self, filter, updated_data, collection_name):
        return collection_name.update_many(filter, {'$set' : updated_data})
    
    def delete_one(self, filter, collection_name):
        return collection_name.delete_one(filter)
    
    def delete_many(self, filter, collection_name):
        return collection_name.delete_many(filter)
    
@contextmanager
def get_db():
    db = Database()
    try:
        yield db
    finally:
        print("Closing DB")