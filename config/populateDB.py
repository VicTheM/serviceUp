"""
Considering this is a capstone project, the production database will have to
be populated with users so testers can see the full functionality of the program
"""
from pymongo import MongoClient
from development import *

client = MongoClient(MONGODB_URI)
db = client[DATABASE]
handworkMenCollection = db["handworkMen"]
userCollection = db["users"]

availableServices = ["electrician", "bricklayer", "plumber"]
firstNames = ["Ada", "Chyintia", "Stephen"]
lastNames = ["Moses", "Daniel", "Joseph"]

def createProfessional(service, firstName, lastName, x):
    phone = 7062453170
    email = firstName + "@gmail.com"
    username = "user | " + firstName
    location = {
        "state": "Lagos", "city": "Yaba", "lga": "Surulere", "street": "Unilag Main Road"
    }

    professional = {
        "firstname": firstName, "lastname": lastName, "email": email, "username": username,
        "password": "1234", "location": location, "services": [service],
        "numOfStars": x, "numOfReview": x // 4, "numOfProfileView": 0, "numOfBookings": x // 4,
        "reviews": [
            'Trust me, you will not be disappointed if you hire him',
            'wow, he arrived at the speed of light!'
                    ] 
    }

    handworkMenCollection.insert_one(professional)

for x in range(0, len(firstNames) - 1):
    createProfessional(availableServices[x], firstNames[x], lastNames[x], x)
    print(f"[{x+1}] inserting...                      Done.")

