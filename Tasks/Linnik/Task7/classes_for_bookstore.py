# Class 1: Book
# Create a class Book to represent information about a book. Each book should have the following attributes:
# (title, author, ISBN (International Standard Book Number), price)
# Implement the necessary methods to get and set these attributes. Ensure that the ISBN is a 13-digit number.

# Class 2: EBook
# Create a class EBook that inherits from the Book class. Add the following attributes:
#
# Format (e.g., PDF, ePub)
# File Size (in MB)
# Download Link
# Ensure that the download link starts with "https://".

# Class 3: PhysicalBook
# Create a class PhysicalBook that also inherits from the Book class. Add the following attributes:
#
# Weight (in grams)
# In Stock (boolean indicating availability)
# Include a method in the PhysicalBook class to update the availability status.

# Class 4: Customer
# Create a class Customer to represent a customer of the online bookstore.
# Each customer should have the following attributes:
#
# Name
# Email
# Address

# Class 5: ShoppingCart
# Create a class ShoppingCart that represents a customer's shopping cart. It should be able to:
#
# Add a book (either Book, EBook, or PhysicalBook) to the cart.
# Remove a book from the cart.
# Calculate the total price of the items in the cart.

# Class 6: PremiumCustomer
# Create a class PremiumCustomer that inherits from the Customer class.
# Add an attribute for membership status and a discount rate for premium customers.
# Implement a method to apply the discount to the total price in the shopping cart.

# Class 7: Order
# Create a class Order that represents a customer's order. It should include:
#
# The customer who placed the order.
# The list of items in the order (books or ebooks).
# The total price of the order.


# Task:
# Write a Python program that demonstrates the use of these classes. Create instances of books, ebooks, and customers.
# Add items to the shopping cart, apply discounts for premium customers, and generate an order.
#
# Ensure that your program adheres to good object-oriented design principles,
# such as encapsulation, inheritance, and proper use of attributes and methods.
