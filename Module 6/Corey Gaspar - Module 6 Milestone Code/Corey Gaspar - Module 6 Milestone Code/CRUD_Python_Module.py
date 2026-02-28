# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient(f"mongodb://{username}:{password}@{HOST}:{PORT}")
        self.database = self.client[DB]
        self.collection = self.database[COL] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is None:
            return False

        try:
            self.collection.insert_one(data)
            return True
        except Exception as e:
            print(f"Insert error: {e}")
            return False

    # Create method to implement the R in CRUD.
    def read(self, query):
        results = []

        try:
            cursor = self.collection.find(query)
            for document in cursor:
                results.append(document)
            return results
        except Exception as e:
            print(f"Read error: {e}")
            return []
    
    # Create method to implement the U in CRUD.
    def update(self, query, new_values):
        if query is None or new_values is None:
            return 0

        try:
            result = self.collection.update_many(query, new_values)
            return result.modified_count
        except Exception as e:
            print(f"Update error: {e}")
            return 0
        
    # Create method to implement the D in CRUD.
    def delete(self, query):
        if query is None:
            return 0

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Delete error: {e}")
            return 0

