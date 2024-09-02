"""ALL MODELS"""

class User():
    """the base class for every user"""
    __numberOfUsers = 0

    def __init__(self, name, email, **kwargs):
        User.numberOfUsers += 1
        self.name = name
        self.email = email


class Professional(User):
    """The service provider class"""

    def __init__(self, name, email, **kwargs):
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

    def to_dict(self):
        """This function represents the class as a dictionary
        for storing in database or jsonifying
        
        the following fields have non-string datatype
        contact: dict
        location: dict
        services: list
        reviewMessages: array
        """
        return {
            "name": self.name,
            "email": self.email,
            "contact": self.contact,
            "location": self.location,
            "services": self.services,
            "numOfStars": self.numOfStars,
            "reviews": self.reviewMessage
        }
    
    def from_dict(self, professionalDictionary):
        """This method populate a class instance from dictionary"""
    
    def add_star(self, star):
        """A user may rate a professional only once, with a max star of 5
        numOfStars is the total star the user has received"""

        self.numOfStars += star
        self.numOfReviews += 1

    def get_avg_star(self):
        """The average rating of a user"""

        return (self.numOfStars/self.numOfReviews)

    def add_review_message(self, review):
        """When a review message is added, the id in the database is added to the class instance
        while the message is sent to the database
        """
        self.reviewMessage.append(review)


