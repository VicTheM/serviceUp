#!/usr/bin/env python
"""This file models the database client"""
from pymongo import MongoClient
from config.secrets import MONGODB_USER
from config.secrets import MONGODB_USER_PASSWORD
from config.development import *

MONGODB_URI = f"mongodb+srv://{MONGODB_USER}:{MONGODB_USER_PASSWORD}@testcluster.njvzz.mongodb.net/?retryWrites=true&w=majority&appName=testCluster"
client = MongoClient(MONGODB_URI)


class DBClient:
    def __init__(self):
        self.client = client
        self.db = client[DATABASE]
        self.userCollection = self.db["users"]
        
        def insertUser(self, user):
            self.userCollection.insert_one(user)