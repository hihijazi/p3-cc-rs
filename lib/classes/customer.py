class Customer:

    def __init__(self, first_name, last_name):
        pass

    def first_name(self):
        pass

    def last_name(self):
        pass

    def full_name(self):
        pass

    def get_num_reviews(self):
        pass

    def create_review(self, restaurant, rating):
        # This prevents a circular import!
        from classes.review import Review
        pass