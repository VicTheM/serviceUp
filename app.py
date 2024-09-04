"""The main entry point to the flask application"""
from flask import Flask, jsonify, redirect, request, session
from pymongo import MongoClient
from config.secrets import MONGODB_USER
from config.secrets import MONGODB_USER_PASSWORD
from config.development import *

app = Flask(__name__)

MONGODB_URI = f"mongodb+srv://{MONGODB_USER}:{MONGODB_USER_PASSWORD}@testcluster.njvzz.mongodb.net/?retryWrites=true&w=majority&appName=testCluster"
client = MongoClient(MONGODB_URI)
db = client[DATABASE]
handworkMenCollection = db["handworkMen"]
userCollection = db["users"]



# GENERAL ROUTES
@app.route("/", methods=['GET'])
def landing_page():
    """Index page contains search bar, link to register and login
    and other adverts or news"""
    # return the html of our main site (not jinja template)
    return "index page"

@app.route('/register', methods=['POST'])
def register():
    """Register page contains form to register a new user
    One could either register as a user of as a Professional"""
    # Frontend will show registration successful pop up
    # then spit out a copy of the landig page with a different view
    return "register page"

@app.route('/login', methods=['POST'])
def login():
    """This page will do the session and cookie management
    then redirect to the profile page for professionals and index page for users"""
    username = request.form.get('username')
    password = request.form.get('password')
    # hash it and compare it to the one in db 
    session['username'] = username

    # spit out the special landing page for logged in users
    return "login page"

@app.route('/logout', methods=['POST'])
def logout():
    #  clear session and pop username off it
    # spit out the main landig page for non-logged in users
    return "logout page"

@app.route('/profile', methods=['GET'])
def profile():
    # Retrieve all the usernames from query string and return their
    # profile as json.
    # If no username in query string then return the
    # current user profile in a Jinja template
    return "profile page"

@app.route('/profile/edit', methods=['POST', 'PUT', 'DELETE'])
def edit_profile():
    # Frontend will provide the feedback, we won't return anything
    # Change the user object using the parameters changed fed in from the query string
    # and update the record in db
    return "edit profile page"


# PROFESSIONAL ROUTES
@app.route('/action/search', methods=['GET'])
def search():
    # The current supported search field is the services field
    # return all professional profiles that offer that service
    # as json 
    return "search results"

@app.route('/action/hire', methods=['POST'])
def hire():
    # Frontend will give the feedback
    # just update the professional hire records in
    # the database 
    return "hire page"

@app.route('/action/review', methods=['POST'])
def review():
    # Frontend will give the feedback
    # update the review record
    return "review page"

@app.route('/action/rate', methods=['POST'])
def rate():
    # Frontend will give the feedback
    # update the rating record
    return "rate page"



if __name__ == '__main__':
    app.run(debug=True, port=5000)