# Assignment: Store & Products
# Objectives:
# Practice creating classes
# Practice associations between classes
# Practice modularizing code
# Start by creating a Store class that has 2 attributes: a name and a list of products. The name must be provided upon creation, but the products list should be empty.

# Next, create a Product class that has 3 attributes: a name, a price, and a category. All of these should be provided upon creation.

# Let's give some methods to our Product class:

# update_price(self, percent_change, is_increased) - updates the product's price. If is_increased is True, the price should increase by the percent_change provided. If False, the price should decrease by the percent_change provided.
# print_info(self) - print the name of the product, its category, and its price.
# Let's also give some methods to our Store class:

# add_product(self, new_product) - takes a product and adds it to the store
# sell_product(self, id) - remove the product from the store's list of products given the id (assume id is the index of the product in the list) and print its info.
# inflation(self, percent_increase) - increases the price of each product by the percent_increase given (use the method you wrote in the Product class!)
# set_clearance(self, category, percent_discount) - updates all the products matching the given category by reducing the price by the percent_discount given (use the method you wrote in the Product class!)


# Create a Store class with 2 attributes
class store:
    def __init__(self, name, products):
        self.name = name
        self.products = products

# Create a Product class with 3 attributes


class products:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.id = id

# Add the print_info method to the Product class


def print_info(self):
    print(f"{self.name} is a {self.category} and costs {self.price}")

# Add the update_price method to the Product class


def update_price(self, percentage, increase):
    if increase:
        self.price = self.price + (self.price * percentage)
        print(f"{self.name} is now {self.price}")
        return self.price
    else:
        self.price = self.price - (self.price * percentage)

# Add the add_product method to the Store class


def add_product(self, new_product):
    self.products.append(new_product)

# Add the sell_product method to the Store class


def sell_product(self, id):
    self.products.pop(id)


# Test out your classes by creating an instance of the Store and a few instances of the Product class, add those instances to the store instance, and then test out the methods.
store1 = store("walmart", [])
product1 = products("apple", 2, "fruit")
product2 = products("banana", 3, "fruit")
product3 = products("orange", 4, "fruit")

store1.add_product(product1)
store1.add_product(product2)
store1.add_product(product3)

product1.update_price(0.25, True)
product2.print_info()
store1.sell_product(0)


# NINJA BONUS: Add the inflation method to the Store class
def inflation(self, percentage):
    for product in self.product:
        product.update_percentage(percentage)
        print(f"{product.name} is now {product.price}")

# NINJA BONUS: Add the set_clearance method to the Store class


def et_clearance(self, catergory, percentage):
    for product in self.products:
        if product.catergory == catergory:
            product.update_percentage(percentage)
            print(f"{product.name} is now {product.price}")

# NINJA BONUS: Modularize your code into 3 separate files
# Store.py
# Product.py
# main.py


# SENSEI BONUS: Update the product class to give each product a unique id. Update the sell_product method to accept the unique id.
