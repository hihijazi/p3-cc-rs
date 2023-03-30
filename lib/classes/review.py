from classes.customer import Customer
from classes.restaurant import Restaurant

class Review:
    
    def __init__(self, customer, restaurant, rating):
        if not isinstance(rating, int):
            raise TypeError("Rating must be a number")
        if not 1 <= rating <= 5:
            raise Exception("rating must be between 1 and 5")
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

        customer.add_review(self)
        restaurant.add_review(self)

    def set_rating(self, rating):
        if not isinstance(rating, (int, float)):
            raise Exception("Rating must be a number.")
        if not (1 <= rating <= 5):
            raise Exception("Rating must be between 1 and 5.")
        self._rating = rating

    def get_rating(self):
        return self._rating

    rating = property(get_rating, set_rating)