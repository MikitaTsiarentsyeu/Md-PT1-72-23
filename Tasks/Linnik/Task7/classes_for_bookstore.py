import re


class Book:

    def __init__(self, title, author, isbn, price):
        self.__title = title
        self.__author = author
        self.__set_isbn(isbn)
        self.price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def __set_isbn(self, isbn):
        while True:
            if len(str(isbn)) != 13 or not isinstance(isbn, int):
                print('it must have 13 digits! \ntry again!')
                try:
                    isbn = int(input())
                except ValueError:
                    print('it must be an integer and', end=' ')
            else:
                self.__isbn = isbn
                break

    title = property(get_title)
    author = property(get_author)
    isbn = property(get_isbn)


class EBook(Book):

    def __init__(self, title, author, isbn, price, format_, file_size, download_link):
        super().__init__(title, author, isbn, price)
        self.format_and_file_size = (format_, file_size)
        self.set_download_link(download_link)

    def get_download_link(self):
        return self.__download_link

    def set_download_link(self, download_link):
        while True:
            if re.search("^https://", download_link):
                self.__download_link = download_link
                break
            else:
                download_link = input("Give another link that starts with 'https://'. \n")

    download_link = property(get_download_link, set_download_link)


class PhysicalBook(Book):

    def __init__(self, title, author, isbn, price, weight, in_stock=True):
        super().__init__(title, author, isbn, price)
        self.__weight = weight
        self.__in_stock = in_stock

    def get_status(self):
        return self.__in_stock

    def update_status(self, in_stock):
        self.__in_stock = in_stock

    def get_weight(self):
        return self.__weight

    in_stock = property(get_status, update_status)
    weight = property(get_weight)


class Customer:

    class ShoppingCart:
        pass

    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address


e_paws = EBook('My Life In His Paws', 'Wendy Hillings', 1234567891634, 25, \
               'PDF', 10, "https://www.goodreads.com/book/show/29244831-my-life-in-his-paws")
#
ph_paws1 = PhysicalBook('My Life In His Paws', 'Wendy Hillings', 1234567891234, 25, \
                       150)
ph_paws1.in_stock = False
#
ph_paws2 = PhysicalBook('My Life In His Paws', 'Wendy Hillings', 1234567893454, 45, \
                       200)
ennead = EBook('Ennead', 'Mojito', 1234567891267, 30, \
               'ePub', 30, "https://www.tappytoon.com/en/book/ennead")

print('e_paws:', e_paws.title, e_paws.author, e_paws.isbn, e_paws.price, \
      e_paws.format_and_file_size, e_paws.download_link, sep='; ')
print('ph_paws1:', ph_paws1.title, ph_paws1.author, ph_paws1.isbn, ph_paws1.price, \
      ph_paws1.weight, ph_paws1.in_stock, sep='; ')
print('ph_paws2:', ph_paws2.title, ph_paws2.author, ph_paws2.isbn, ph_paws2.price, \
      ph_paws2.weight, ph_paws2.in_stock, sep='; ')
print('ennead:', ennead.title, ennead.author, ennead.isbn, ennead.price, \
      ennead.format_and_file_size, ennead.download_link, sep='; ')


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
