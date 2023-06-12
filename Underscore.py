class Underscore:
    def map(self, iterable, callback):
        # your code here
        return [callback(item) for item in iterable]

    def find(self, iterable, callback):
        # your code here
        return [item for item in iterable if callback(item)]

    def filter(self, iterable, callback):
        # your code
        return [item for item in iterable if callback(item)]

    def reject(self, iterable, callback):
        # your code
        return [item for item in iterable if not callback(item)]


# you just created a library with 4 methods!
# let's create an instance of our class
score = Underscore()  # yes we are setting our instance to a variable that is an underscore
evens = score.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above


# Complete the map method

# Complete the find method

# Complete the filter method

# Complete the reject method
