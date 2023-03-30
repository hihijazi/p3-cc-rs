from .restaurant import Restaurant

class Customer:

    def __init__(self, first_name, last_name):
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise TypeError("Names must be strings.")
        if not (1 <= len(first_name) <= 25) or not (1 <= len(last_name) <= 25):
            raise ValueError("Names must be between 1 and 25 characters long.")
        self._first_name = first_name
        self._last_name = last_name
        self._reviews = []

    def set_first_name(self, first_name):
        if not (1 <= len(first_name) <= 25):
            raise ValueError("Names must be between 1 and 25 characters long.")
        self._first_name = first_name

    def get_first_name(self):
        return self._first_name

    first_name = property(get_first_name, set_first_name)
    
    def set_last_name(self, last_name):
        if not (1 <= len(last_name) <= 25):
            raise ValueError("Names must be between 1 and 25 characters long.")
        self._last_name = last_name

    def get_last_name(self):
        return self._last_name

    last_name = property(get_last_name, set_last_name)

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"
    
    def add_review(self, review):
        self._reviews.append(review)

    def getrestaurants(self):
        return list(map(lambda review: review.restaurant, self._reviews))
    
    restaurants = property(getrestaurants)

    def getreviews(self):
        return self._reviews
    
    reviews = property(getreviews)

    def get_num_reviews(self):
        return len(self._reviews)

    def create_review(self, restaurant, rating):
        from .review import Review
        if not isinstance(restaurant, Restaurant):
            raise TypeError("Restaurant must be an instance of Restaurant.")
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5, inclusive.")
        review = Review(self, restaurant, rating)