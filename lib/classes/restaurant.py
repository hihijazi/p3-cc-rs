class Restaurant:

    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        self._name = name
        self._reviews = []

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        name

    name = property(get_name, set_name)

    def add_review(self, review):
        self._reviews.append(review)

    def getcustomers(self):
        return list(map(lambda review: review.customer, self._reviews))
    
    customers = property(getcustomers)

    def getreviews(self):
        return self._reviews
    
    reviews = property(getreviews)

    def average_star_rating(self):
        return sum(list(map(lambda review: review.rating, self._reviews)))/len(self._reviews)

    @classmethod
    def get_all_restaurants(cls):
        return cls.all