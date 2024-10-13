from os import getenv

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

class Database():
    def __init__(self):
        self.client = MongoClient(getenv('MONGO_CLIENT_LOCAL'))
        self.db = self.client['dbms_course']
        self.user_collection = self.db['users']
        self.catalog_collection = self.db['catalog']

    def insert_one(self, data, collection_name):
        return collection_name.insert_one(data)
    
    def insert_many(self, data, collection_name):
        return collection_name.insert_many(data)
    
    def find():
        return 0
    
    def find_one_by_id():
        return 0
    
    def update_one():
        return 0
    
    def update_many():
        return 0
    
    def delete_one():
        return 0