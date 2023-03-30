# Object Relations Code Challenge - Restaurants

For this assignment, we'll be working with a Yelp-style domain.

We have three models: `Restaurant`, `Customer`, and `Review`.

For our purposes, a `Restaurant` has many `Reviews`, a `Customer` has many
`Review`s, and a `Review` belongs to a `Customer` and to a `Restaurant`.

`Restaurant` - `Customer` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge has tests to help you check your work. You
can run `pytest` to make sure your code is functional before submitting.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers, Readers, and Writers

For any invalid inputs raise an `Exception`. In your future work, you should
raise specific types of exceptions for specific error cases. You can do that
here and the tests will pass, but you don't have to this time around!

#### Customer

- `Customer __init__(self, first_name, last_name)`
  - Customer should be initialized with a given name and family name, (i.e.,
    first and last name,
    like George Washington)"
- `Customer property first_name()` and `Customer property last_name()`
  - Return first and last name, respectively
  - Names must be of type `str`
  - Names must be between 1 and 25 characters, inclusive

#### Restaurant

- `Restaurant __init__(self, name)`
  - Restaurants should be initialized with a name, as a string
- `Restaurant property name()`
  - Returns the restaurant's name
  - Should not be able to change after the restaurant is created

#### Review

- `Review __init__(self, customer, restaurant, rating)`
  - Reviews should be initialized with a customer, restaurant, and a rating (a number)
- `Review property rating()`
  - Returns the rating for a restaurant
  - Rating must be a number between 1 and 5, inclusive

### Object Relationships

#### Review

- `Review customer`
  - Returns the customer object for that review
  - Must be of type `Customer`
- `Review restaurant`
  - Returns the restaurant object for that given review
  - Must be of type `Restaurant`

#### Restaurant

- `Restaurant reviews`
  - Returns a list of all reviews for that restaurant
  - Reviews must be of type `Review`
- `Restaurant customers()`
  - Returns a **unique** list of all customers who have reviewed a particular restaurant.
  - Customers must be of type `Customer`

#### Customer

- `Customer restaurants`
  - Returns a **unique** list of all restaurants a customer has reviewed
- `Customer reviews`
  - Returns a list of all reviews a customer has written

### Aggregate and Association Methods

#### Customer

- `Customer num_reviews()`
  - Returns the total number of reviews that a customer has authored
- `Customer add_review(restaurant, rating)`
  - given a **restaurant object** and a star rating (as an integer), creates a
    new review and associates it with that customer and restaurant.

#### Restaurant

- `Restaurant average_star_rating()`
  - Returns the average star rating for a restaurant based on its reviews
  - Reminder: you can calculate the average by adding up all the ratings and
    dividing by the number of ratings

- `Restaurant get_all_restaurants() classmethod`
  - Returns a list of all restaurants
