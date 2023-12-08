class Book:
    
    def __init__(self, title, author, isbn, price):
        self.__set_title(title)
        self.__set_author(author)
        self.__set_isbn(isbn)
        self.price = price

    def __set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title
    
    def __set_author(self, author):
        self.__author = author

    def get_author(self):
        return self.__author

    def __set_isbn(self, isbn):
        if len(isbn) == 13 and isbn.isdigit():
            self.__isbn = isbn

    def get_isbn(self):
        return self.__isbn
    
    title = property(get_title, __set_title)
    author = property(get_author, __set_author)
    isbn = property(get_isbn, __set_isbn)


class EBook(Book):
    
    def __init__(self, title, author, isbn, price, format, file_size, download_link):
        super().__init__(title, author, isbn, price)
        self.format = format
        self.file_size = file_size
        self.__set_download_link(download_link)

    def __set_download_link(self, link):
        if link[0:8] == 'https://':
            self.__download_link = link
        else:
            print("Incorrect download link")
    
    def get_download_link(self):
        return self.__download_link
    
    download_link = property(get_download_link, __set_download_link)


class PhysicalBook(Book):
    
    def __init__(self, title, author, isbn, price, weight, in_stock=True):
        super().__init__(title, author, isbn, price)
        self.weight = weight
        self.in_stock = in_stock

    def update_availability(self, in_stock):
        self.in_stock = in_stock


class Customer:
    
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address


class ShoppingCart:
    
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total_price(self):
        total_price = sum(item.price for item in self.items)
        return total_price


class PremiumCustomer(Customer):
    
    def __init__(self, name, email, address, membership_status, discount_rate):
        super().__init__(name, email, address)
        self.membership_status = membership_status
        self.discount_rate = discount_rate

    def apply_discount(self, total_price):
        return total_price * (1 - self.discount_rate)


class Order:
    
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self.total_price = sum(item.price for item in items)


book1 = Book("The Lord Of The Rings", "J.R.R. Tolkien ", "9780544003415", 35)
ebook1 = EBook("Brave new world", "Aldous Huxley", "9781841593593", 12.86, "pdf", 2916, "https://www.example.com/Brave-New-World-Aldous-Huxley")
pbook1 = PhysicalBook("Dune", "Frank Herbert", "9780143111580", 19.05, 567, True)
pbook2 = PhysicalBook("Foundation", "Isaac Asimov", "9780808520788", 13.87, 198, True)

customer1 = Customer("Chandler", "chandler@example.com", "90 Bedford St")
premium_customer1 = PremiumCustomer("Monica", "monica@example.com", "90 Bedford St", "Gold", 0.2)

# Add books in Shooping cart
cart = ShoppingCart()
cart.add_item(book1)
cart.add_item(ebook1)
cart.add_item(pbook1)
cart.add_item(pbook2)

# Price calculation
total_price = cart.calculate_total_price()
discounted_price = premium_customer1.apply_discount(total_price)

# Create an order
order = Order(premium_customer1, cart.items)

# Checking order list:
# for item in cart.items:
#     print(f"{item.title} by {item.author}")
# [print(f"{item.title} by {item.author}") for item in cart.items]

# Output

# The Lord Of The Rings by J.R.R. Tolkien 
# Brave new world by Aldous Huxley
# Dune by Frank Herbert
# Foundation by Isaac Asimov

print(f"Order placed by {order.customer.name}:\n")
for item in order.items:
    print(f"    {item.title} by {item.author}: ${item.price}")
print(f"\nTotal price: ${order.total_price} (Discounted: ${round(discounted_price, 2)})")

# output:

# Order placed by Monica:

#     The Lord Of The Rings by J.R.R. Tolkien : $35
#     Brave new world by Aldous Huxley: $12.86
#     Dune by Frank Herbert: $19.05
#     Foundation by Isaac Asimov: $13.87

# Total price: $80.78 (Discounted: $64.62)