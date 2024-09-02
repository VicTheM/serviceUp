"""The main entry point to the flask application"""
import os
from flask import Flask, jsonify

app = Flask(__name__)



# GENERAL ROUTES
@app.route("/", methods=['GET'])
def index_page():
    """Index page contains search bar, link to register and login
    and other adverts or news"""

    return "index page"

@app.route('/register', methods=['POST'])
def register():
    """Register page contains form to register a new user
    One could either register as a user of as a Professional"""

    return "register page"

@app.route('/login', methods=['POST'])
def login():
    """This page will do the session and cookie management
    then redirect to the profile page for professionals and index page for users"""

    return "login page"

@app.route('/logout', methods=['POST'])
def logout():
    return "logout page"

@app.route('/profile', methods=['GET'])
def profile():
    return "profile page"

@app.route('/profile/edit', methods=['PUT', 'DELETE'])
def edit_profile():
    return "edit profile page"


# PROFESSIONAL ROUTES
@app.route('/action/search', methods=['GET'])
def search():
    return "search results"

@app.route('/action/hire', methods=['POST'])
def hire():
    return "hire page"

@app.route('/action/review', methods=['POST'])
def review():
    return "review page"

@app.route('/action/rate', methods=['POST'])
def rate():
    return "rate page"



if __name__ == '__main__':
    app.run(debug=True, port=5000)