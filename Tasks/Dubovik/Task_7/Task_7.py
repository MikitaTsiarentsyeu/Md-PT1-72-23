
class Book:
    def __init__(self, Title, Author, ISBN, Price):
        self.Title = Title
        self.Author = Author
        self.ISBN = ISBN
        self.Price = Price

    def __set_title(self, Title):
        self.Title = Title

    def get_title(self):
        return self.Title

    def __set_author(self, Author):
        self.Author = Author

    def get_author(self):
        return self.Author

    def __set_ISBN(self, ISBN):
        if len(str(ISBN)) != 13:
            print('Incorrect ISBN')
        self.ISBN = ISBN

    def get_isbn(self):
        return self.ISBN

    title = property(get_title, __set_title)
    author = property(get_author, __set_author)
    isbn = property(get_isbn, __set_ISBN)


class EBook(Book):
    FORMAT = ["FB2", "EPUB", "PDF", "djvu"]

    def __init__(self, Title, Author, ISBN, Price, format, file_size, download_link):
        super().__init__(Title, Author, ISBN, Price)
        self.format = format
        self.file_size = f"{file_size} mb"
        self.set_download_link = download_link

    def set_download_link(self, download_link):
        if 'https://' not in download_link:
            link = f'https://{download_link}'
        else:
            print("Incorrect download link")

    def get_download_link(self):
        return self.download_link

    download_link = property(get_download_link, set_download_link)


class PhysicalBook(Book):

    def __init__(self, Title, Author, ISBN, Price, Weight, In_stock=True):
        super().__init__(Title, Author, ISBN, Price)
        self.Weight = f"{Weight} grams"
        self.In_stock = In_stock

    def update_availability_status(self, In_stock):
        self.In_stock = In_stock


class Customer:

    def __init__(self, Name, Email, Address):
        self.Name = Name
        self.Email = Email
        self.Address = Address


class ShoppingCart:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        # print('Book added')

    def remove_book(self, book):
        self.books.remove(book)

    def cart_subtotal(self):
        rate = sum(book.Price for book in self.books)
        return rate


class PremiumCustomer(Customer):

    def __init__(self, Name, Email, Address, membership_status, discount_rate):
        super().__init__(Name, Email, Address)
        self.membership_status = membership_status
        self.discount_rate = discount_rate

    def apply_discount(self, rate):
        return rate * (1 - self.discount_rate)


class Order:

    def __init__(self, customer, books):
        self.customer = customer
        self.books = books
        self.rate = sum(book.Price for book in books)


# Customer setup
customer = Customer("Alex Dubovik", "test@test.com", "122 Dart Hill Rd")
customer2 = Customer("Alex Dubovik2", "test@test.com", "122 Dart Hill Rd")
customer3 = Customer("Alex Dubovik3", "test@test.com", "122 Dart Hill Rd")

# Premium setup

premium_customer = PremiumCustomer("Alex DubovikPremium", "test@test.com", "122 Dart Hill Rd", "Premium", 0.3)
premium_customer2 = PremiumCustomer("Alex DubovikPremium2", "test@test.com", "122 Dart Hill Rd", "Premium2", 0.5)


# Books setup
b1 = EBook("Искусство программирования.Том 1.", "Дональд Эрвин Кнут", "9999999999999", 190.56, "epub", 5670,
               "https://flibusta.is/b/329114")


b2 = EBook("Воспоминание о развитии моего ума и характера", "Чарльз Роберт Дарвин", "7777777777777", 500.17, "djvu",
               1220, "https://flibusta.is/b/185017")

b3 = PhysicalBook("Таинственный остров", "Жюль Верн", "8888888888888", 200.22, 560, True)
b4 = PhysicalBook("Графиня де Монсоро", "Александр Дюма", "9999999999999", 300.15, 3990, True)




# Cart setup
cart = ShoppingCart()
cart.add_book(b1)
cart.add_book(b2)
cart.add_book(b3)
cart.add_book(b4)

cart2 = ShoppingCart()
cart2.add_book(b3)
cart2.add_book(b3)


cart3 = ShoppingCart()
cart3.add_book(b2)
cart3.add_book(b2)
cart3.add_book(b4)
cart3.add_book(b4)

cart4 = ShoppingCart()
cart4.add_book(b1)
cart4.add_book(b1)
cart4.add_book(b1)
cart4.add_book(b1)




# Rare setup
rate = cart.cart_subtotal()


# Discount rate setup
discount_rate = premium_customer.apply_discount(rate)
discount_rate2 = premium_customer2.apply_discount(rate)


# Order setup

order = Order(premium_customer, cart.books)
order2 = Order(customer, cart2.books)
order3 = Order(customer2, cart3.books)
order4 = Order(premium_customer2,cart4.books)



print(f"Customer -  {order.customer.Name}:\n")
print("Book List:\n")
for book in order.books:
    print(f"{book.title} - {book.author} -  ${book.Price}")
print("\n")
print(f"Total price is: ${round(order.rate, 2)}")
print(f"With discount applied price is: ${round(discount_rate, 2)}\n")


print(f"Customer -  {order2.customer.Name}:\n")
print("Book List:\n")
for book in order2.books:
    print(f"{book.title} - {book.author} -  ${book.Price}")
print("\n")
print(f"Total price is: ${round(order2.rate, 2)}")


print(f"Customer -  {order3.customer.Name}:\n")
print("Book List:\n")
for book in order3.books:
    print(f"{book.title} - {book.author} -  ${book.Price}")
print("\n")
print(f"Total price is: ${round(order3.rate, 2)}")



print(f"Customer -  {order4.customer.Name}:\n")
print("Book List:\n")
for book in order4.books:
    print(f"{book.title} - {book.author} -  ${book.Price}")
print("\n")
print(f"Total price is: ${round(order4.rate, 2)}")
print(f"With discount applied price is: ${round(discount_rate2, 2)}\n")
