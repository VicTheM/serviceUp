"""ALL MODELS"""
from typing import List, Dict

class User():
    """the base class for every user"""
    __numberOfUsers = 0

    def __init__(self, firstname: str, lastname: str, email: str, username: str, password: str, **kwargs: dict):
        User.__numberOfUsers += 1
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username
        self.password = password

    def to_dict(self):
        """This function represents the class as a dictionary
        for storing in database or jsonifying"""
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "username": self.username,
            "password": self.password
        }
    
    def from_dict(self, userDictionary: dict):
        """This method populate a class instance from dictionary"""
        self.firstname = userDictionary.get("firstname")
        self.lastname = userDictionary.get("lastname")
        self.username = userDictionary.get("username")
        self.password = userDictionary.get("password")


class Professional(User):
    """The service provider class"""

    def __init__(self, firstname=None, lastname=None, email=None, username=None, password=None, **kwargs):
        if firstname is not None:
            super().__init__(firstname, lastname, email, username, password, **kwargs)
            self.numOfStars = 0
            self.numOfReviews = 0
            self.numberOfProfileView = 0
            self.numberOfBookings = 0

            if "contact" in kwargs:
                self.contact = kwargs["contact"]
            else:
                self.contact = None
            if "location" in kwargs:
                self.location = kwargs["location"]
            else:
                self.location = None
            if "services" in kwargs:
                self.services = kwargs["services"]
            else:
                self.services = []
            if "reviewMessage" in kwargs:
                self.reviewMessage = kwargs["reviewMessage"]
            else:
                self.reviewMessage = []
        # if name is None, then the class instance is being populated from the database
        # use the syntax variable = Professional().from_dict(professionalDictionary)

    def to_dict(self):
        """This function represents the class as a dictionary
        for storing in database or jsonifying
        
        the following fields have non-string datatype
        contact: dict
        location: dict
        services: list
        reviewMessages: list
        """
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "contact": self.contact,
            "location": self.location,
            "services": self.services,
            "numOfStars": self.numOfStars,
            "numOfReviews": self.numOfReviews,
            "numberOfProfileView": self.numberOfProfileView,
            "numberOfBookings": self.numberOfBookings,
            "reviews": self.reviewMessage
        }
    
    def from_dict(self, professionalDictionary: dict):
        """This method populate a class instance from dictionary"""
        self.firstname = professionalDictionary.get("firstname")
        self.lastname = professionalDictionary.get("lastname")
        self.username = professionalDictionary.get("username")
        self.password = professionalDictionary.get("password")
        self.email = professionalDictionary.get("email")
        self.contact = professionalDictionary.get("contact")
        self.location = professionalDictionary.get("location")
        self.services = professionalDictionary.get("services")
        self.numOfStars = professionalDictionary.get("numOfStars", 0)
        self.numOfReviews = professionalDictionary.get("numOfReviews", 0)
        self.numberOfProfileView = professionalDictionary.get("numberOfProfileView", 0)
        self.numberOfBookings = professionalDictionary.get("numberOfBookings", 0)
        self.reviewMessage = professionalDictionary.get("reviews", [])
    
    def add_star(self, star: int):
        """A user may rate a professional only once, with a max star of 5
        numOfStars is the total star the user has received"""

        self.numOfStars += star
        self.numOfReviews += 1

    def get_avg_star(self):
        """The average rating of a user"""

        return (self.numOfStars/self.numOfReviews)

    def add_review_message(self, review: str):
        """When a review message is added, the id in the database is added to the class instance
        while the message is sent to the database
        """
        self.reviewMessage.append(review)