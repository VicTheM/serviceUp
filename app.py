"""The main entry point to the flask application"""
from flask import Flask, jsonify, redirect, url_for, render_template, request, session
from pymongo import MongoClient
from typing import List, Dict, Any
from .models.user import User
from .models.user import Professional
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util


MONGODB_USER = "testUser"
MONGODB_USER_PASSWORD = "1234"
DATABASE = "development"

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

MONGODB_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGODB_URI)
db = client[DATABASE]
handworkMenCollection = db["handworkMen"]
userCollection = db["users"]



# GENERAL ROUTES
@app.route("/", methods=['GET'])
def landing_page():
    """Loggedin page has premium css style while logged out page has a basic style"""

    if "email" in session:
        return render_template('landing_logged_in.html')
    else:
        return render_template('landing.html')

@app.route('/register', methods=['POST'])
def register():
    """Receives registration details as a POST parameter.
    Frontend will handle the data validation before making the request, otherwise abort it"""
    
    data: Dict[str, Any] = request.get_json()
    registration_type = data.get('registration-type')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Hash the password
    hashed_password = generate_password_hash(password)

    if registration_type == 'professional':
    #     # Check if email already exists in userCollection or handworkMenCollection
        if handworkMenCollection.find_one({"email": email}):
            print("Email found")
            return jsonify({"error": "Email already exist"}), 400
        
        # Extract additional professional data
        contact = data.get('contact')
        state = data.get('state')
        area_or_city = data.get('city')
        lga = data.get('lga')
        street = data.get('street')
        service = data.get('service')

        # Create Professional object and save to the collection
        new_professional = Professional(
            firstname, lastname, email, username, hashed_password, contact=contact,
            location={"state": state, "area_or_city": area_or_city, "lga": lga, "street": street},
            services=[service]
        )
        handworkMenCollection.insert_one(new_professional.to_dict())
    else:
        if userCollection.find_one({"email": email}):
            return jsonify({"error": "Email already exists"}), 400
        # Create User object and save to the collection
        new_user = User(firstname, lastname, email, username, password=hashed_password)
        userCollection.insert_one(new_user.to_dict())

    # Store username in session
    session['email'] = email

    # Redirect to the login page
    return render_template('landing_logged_in.html')

@app.route('/login', methods=['POST'])
def login():
    """This page will do the session and cookie management
    then redirect to the profile page for professionals and index page for users"""
    # hash it and compare it to the one in db if it matches
    # spit out the special landing page for logged in users

    email = request.form.get('email')
    exists: Dict[str, Any] = userCollection.find_one({"email": email}) or handworkMenCollection.find_one({"email": email})
    if not exists:
        return jsonify({"error": "User not found"}), 404
    if not check_password_hash(exists.get("password"), request.form.get('password')):
        return jsonify({"error": "Incorrect password"}), 400
    session['email'] = exists.get("email")
    return redirect(url_for('landing_page'))

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    # to be handled by the frontend
    return jsonify({"message": "Logged out successfully"})

@app.route('/profile', methods=['GET'])
def profile():
    # Retrieve all the usernames from query string and return their
    # profile as json.
    # If no username in query string then return the
    # current user profile in a Jinja template

    # get parameter from query string
    if "email" in request.args:
        email = request.args.get('email')
        professional = handworkMenCollection.find_one({"email": email})
        return jsonify(json_util._json_convert(professional))
    else:
        if "email" in session:
            currentUser = session['email']
            user = handworkMenCollection.find_one({"email": currentUser}) or userCollection.find_one({"email": currentUser})
            return render_template('profile.html', user=user)
        else:
            return redirect(url_for('landing_page'))

@app.route('/profile/edit', methods=['POST', 'PUT', 'DELETE'])
def edit_profile():
    """   TESTED WITH POSTMAN   """
    # Frontend will provide the feedback, we won't return anything
    # Change the user object using the parameters changed fed in from the query string
    # and update the record in db

    if "email" not in session:
        return jsonify({"error": "Not logged in"}), 401
    email = session['email']
    user = handworkMenCollection.find_one({"email": email}) or userCollection.find_one({"email": email})
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    # any other parameter to change will be in the query string
    if "firstname" in request.args:
        user["firstname"] = request.args.get('firstname')
    if "lastname" in request.args:
        user["lastname"] = request.args.get('lastname')
    if "contact" in request.args:
        user["contact"] = request.args.get('contact')
    if "state" in request.args:
        user["location"]["state"] = request.args.get('state')
    if "city" in request.args:
        user["location"]["city"] = request.args.get('city')
    if "lga" in request.args:
        user["location"]["lga"] = request.args.get('lga')
    if "street" in request.args:
        user["location"]["street"] = request.args.get('street')
    if "service" in request.args:
        if request.method == 'DELETE':
            user["services"].remove(request.args.get('service'))
        else:
            user["services"].append(request.args.get('service'))
    
    handworkMenCollection.update_one({"email": email}, {"$set": user})
    return jsonify({"message": "Profile updated successfully"})


# PROFESSIONAL ROUTES
@app.route('/action/search', methods=['GET'])
def search():
    # The current supported search field is the services field
    # return all professional profiles that offer that service
    # as json

    service = request.args.get('service')
    professionals = handworkMenCollection.find({"services": service})
    if not professionals:
        return jsonify({"error": "No professional found"}), 404

    professionals = list(professionals)
    for professional in professionals:
        print(professional)
    return jsonify(json_util._json_convert(professionals))

@app.route('/action/hire', methods=['POST'])
def hire():
    # Frontend will give the feedback
    # just update the professional hire records in
    # the database

    hired_professional = request.args.get('email')
    professional = handworkMenCollection.find_one({"email": hired_professional})
    if not professional:
        return jsonify({"error": "Professional not found"}), 404
    print (f"number of booking before update: {professional["numOfBookings"]}")
    if not "numOfBookings" in professional or professional["numOfBookings"] is None:
        professional["numOfBookings"] = 0
    professional["numOfBookings"] += 1
    print (f"number of booking before saving: {professional["numOfBookings"]}")
    handworkMenCollection.update_one({"email": hired_professional}, {"$set": {"numOfBookings": professional.get("numOfBookings")}}) # inefficient, rather use a mongo update operator
    print (f"number of booking after saving: {professional["numOfBookings"]}")
    return jsonify({"message": "Professional hired successfully"})

@app.route('/action/review', methods=['POST'])
def review():
    # Frontend will give the feedback
    # update the review record
    review = request.form.get('review')
    reviewed_professional = request.args.get('email')
    professional = handworkMenCollection.find_one({"email": reviewed_professional})
    if not professional:
        return jsonify({"error": "Professional not found"}), 404
    professional["reviews"].append(review)
    handworkMenCollection.update_one({"email": reviewed_professional}, {"$set": {"reviews": professional.get("reviews")}})
    return jsonify({"message": "Review added successfully"})

@app.route('/action/rate', methods=['POST'])
def rate():
    # Frontend will give the feedback
    # update the rating record
    star = request.args.get('star')
    if not isinstance(star, int):
        star = int(star)
    if star > 5:
        star = 5
    elif star < 1:
        star = 1
    rated_professional = request.args.get('email')
    professional = handworkMenCollection.find_one({"email": rated_professional})
    if not professional:
        return jsonify({"error": "Professional not found"}), 404
    professional["numOfStars"] += star
    professional["numOfReviews"] += 1
    handworkMenCollection.update_one({"email": rated_professional}, {"$set": {"numOfStars": professional.get("numOfStars"), "numOfReviews": professional.get("numOfReviews")}})

    return jsonify({"message": "Rating added successfully"})

@app.route('/action/profile/updatepassword', methods=['POST'])
def update_password():
    # Frontend will give the feedback
    # update the password record
    if "email" not in session:
        return jsonify({"error": "Not logged in"}), 401
    new_password = request.args.get('new-password')
    professional = handworkMenCollection.find_one({"email": session['email']})
    professional["password"] = generate_password_hash(new_password)
    handworkMenCollection.update_one({"email": session['email']}, {"$set": {"password": professional.get("password")}})

@app.errorhandler(404)
def page_not_found_error(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)