from classes.restaurant import Restaurant
from classes.customer import Customer
from classes.review import Review
import pytest
class TestCustomer:
    '''Customer in customer.py'''

    def test_has_name(self):
        '''has the first name and last name passed into __init__'''
        customer = Customer('Steve', 'Wayne')
        assert(customer.first_name == "Steve")
        assert(customer.last_name == "Wayne")
        assert(customer.get_full_name() == 'Steve Wayne')
        with pytest.raises(Exception):
            customer.first_name = True
        with pytest.raises(Exception):
            customer.first_name = "a"*26
        with pytest.raises(Exception):
            customer.first_name = ""


    def test_has_many_reviews(self):
        '''customer has many reviews'''
        restaurant = Restaurant("Mels")
        customer = Customer('Steve', 'Wayne')
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)

        assert( len(restaurant.reviews) == 2)
        assert(review_1 in customer.reviews)
        assert(review_2 in customer.reviews)

    def test_has_many_restaurants(self):
        '''customer has many restaurants.'''
        restaurant = Restaurant("Mels")
        restaurant_2 = Restaurant("Chipotle")

        customer = Customer('Steve', 'Wayne')
        customer_2 = Customer('Dima', 'Bay')
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant_2, 5)

        assert(restaurant in customer.restaurants)
        assert(restaurant_2 in customer.restaurants)


    def test_get_number_of_reviews(self):
        '''test get_number_of_reviews()'''
        restaurant = Restaurant("Mels")
        customer = Customer('Steve', 'Wayne')
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)

        assert(  customer.get_num_reviews() == 2)

    def test_add_review(self):
        '''test add_review()'''
        restaurant = Restaurant("Mels")
        customer = Customer('Steve', 'Wayne')
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)
        
        assert(customer.get_num_reviews() == 2)
        customer.add_review(restaurant, 1)
        assert(len(customer.reviews) == 3)
        assert(customer.reviews[2].rating == 1)
        assert(customer.reviews[2].restaurant == restaurant)