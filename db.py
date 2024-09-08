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

'''
EXAMPLE OF THE USER DOCUMENT STRUCTURE IN DB
'''
Victory = {
        "name": "Victory Chibuike",
        "email": "victorychibuike121@gmail.com",
        "contact": 8104334025,
        "location": {
            "country": "Nigeria",
            "state": "Lagos",
            "LGA": "Oshodi-Isolo",
            "LANDMARK": "Community Road",
            "Street": "Fatai Lawal",
            "Domain": ["Ago Palace Way", "Okota", "Festac", "Yaba", "Ikoyi"]
        },
        "services": ["Electrician", "Electronics Repairer", "House Wiring", "Smart Device Installation"],
        "numOfStars": 257,
        "numOfReviews": 1000,
        "numberOfProfileView": 1311,
        "numberOfBookings": 1290,
        "reviews": ["He is a skilled, professional and fururistic worker", "He is very knowledgeable in his work"]
    }