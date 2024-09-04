"""ALL MODELS"""
from typing import List, Dict

class User():
    """the base class for every user"""
    __numberOfUsers = 0

    def __init__(self, name: str, email: str, **kwargs: dict):
        User.__numberOfUsers += 1
        self.name = name
        self.email = email


class Professional(User):
    """The service provider class"""

    def __init__(self, name=None, email=None, **kwargs):
        if name is not None:
            super().__init__(name, email, **kwargs)
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
            "name": self.name,
            "email": self.email,
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
        self.name = professionalDictionary.get("name")
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


