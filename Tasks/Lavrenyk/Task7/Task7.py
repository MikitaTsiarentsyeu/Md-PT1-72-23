from random import randint


class Book:
    def __init__(self, title, author, isbn, price):
        Book.__setTitle(self, title)
        Book.__setAuthor(self, author)
        Book.__setIsbn(self, isbn)
        self.__Price = price

    def __setTitle(self, title):
        self.__Title = title

    def getTitle(self):
        return self.__Title

    def __setAuthor(self, author):
        self.__Author = author

    def getAuthor(self):
        return self.__Author

    def __setIsbn(self, isbn):
        if len(isbn) != 13:
            isbn = "0000000000000"
        self.__Isbn = isbn

    def getIsbn(self):
        return self.__Isbn

    def __setPrice(self, price):
        self.__Price = price

    def getPrice(self):
        return self.__Price

    title = property(getTitle)
    author = property(getAuthor)
    isbn = property(getIsbn)
    price = property(getPrice, __setPrice)


class Ebook(Book):
    __AVAILABLE_FORMATS = ['FB2', 'EPUB', 'MOBI',
                           'TXT', 'PDF', 'LRF',
                           'DjVu', 'RTF', 'DOC']

    def __init__(self, form, download_link, title, author, isbn, price):
        super().__init__(title, author, isbn, price)
        Ebook.__setFormat(self, form)
        Ebook.__setFileSize(self, randint(2, 3000))
        Ebook.__setDownloadLink(self, download_link)

    def __setFileSize(self, kb_size):
        self.__File_size = f'{kb_size} MB'

    def getFileSize(self):
        return self.__File_size

    def __setFormat(self, form):
        if form in self.__AVAILABLE_FORMATS:
            self.__Format = form
        else:
            self.__Format = 'EPUB'

    def getFormat(self):
        return self.__Format

    def __setDownloadLink(self, link):
        if 'https://' not in link:
            link = f'https://{link}'
        self.__download_link = link

    def getDownloadLink(self):
        return self.__download_link

    form = property(getFormat, __setFormat)
    f_size = property(getFileSize)
    d_link = property(getDownloadLink)


class PhysicalBook(Book):
    def __init__(self, in_stock, title, author, isbn, price, weight=randint(100, 1500)):
        super().__init__(title, author, isbn, price)
        self.__In_stock = in_stock
        PhysicalBook.__setWeight(self, weight)

    def getInStock(self):
        return self.__In_stock

    def UpdateStock(self):
        if self.__In_stock:
            self.__In_stock = False
        else:
            self.__In_stock = True

    def __setWeight(self, weight):
        self.__weight = f'{weight} g.'

    def getWeight(self):
        return self.__weight

    Avail = property(getInStock)
    Weight = property(getWeight)


class Customer:
    def __init__(self, customer_name, customer_email, customer_address):
        self.__customer_name = customer_name
        self.__customer_email = customer_email
        self.__customer_address = customer_address

    def getName(self):
        return self.__customer_name

    name = property(getName)

    def __setEmail(self, email):
        self.__customer_email = email

    def getEmail(self):
        return self.__customer_email

    email = property(getEmail, __setEmail)

    def __setAddress(self, address):
        self.__customer_address = address

    def getAddress(self):
        return self.__customer_address

    address = property(getAddress, __setAddress)


class ShoppingCart:
    def __init__(self):
        self.__BOOKS_IN_CART = {}
        self.__TotalPrice = 0

    def AddBook(self, bookObj):
        if bookObj.title in self.__BOOKS_IN_CART:
            self.__BOOKS_IN_CART[bookObj.title][1] += 1
        else:
            self.__BOOKS_IN_CART[bookObj.title] = [bookObj.price, 1]

    def RemoveBook(self, bookObj):
        if self.__BOOKS_IN_CART[bookObj.title][1] == 1:
            self.__BOOKS_IN_CART.pop(bookObj.title)
        else:
            self.__BOOKS_IN_CART[bookObj.title][1] -= 1

    def CalcTotalPrice(self):
        self.__TotalPrice = 0
        for v in self.__BOOKS_IN_CART.values():
            self.__TotalPrice += v[0] * v[1]

        return self.__TotalPrice

    def getBooksInCart(self):
        return self.__BOOKS_IN_CART

    books_in_cart = property(getBooksInCart)
    total_price = property(CalcTotalPrice)


class PremiumCustomer(Customer):
    __DISCOUNT_RATE = {"Pro": 10,
                       "Premium": 25,
                       "UltraPremium": 50}

    def __init__(self, customer_name, customer_email, customer_address, membership_status):
        super().__init__(customer_name, customer_email, customer_address)
        if membership_status not in self.__DISCOUNT_RATE:
            self.__membership_status = "Pro"
        else:
            self.__membership_status = membership_status
        self.__discount = self.getDiscount()

    def getDiscount(self):
        return self.__DISCOUNT_RATE[self.__membership_status]

    def ApplyDiscount(self, cartObj):
        return cartObj.total_price - cartObj.total_price * self.__discount / 100

    discount = property(getDiscount)


class Order:
    def __init__(self, customer, shopping_cart):
        if type(customer) == PremiumCustomer:
            self.__discount = True
            self.__premium_customer = customer
        else:
            self.__discount = False
        Order.__setCustomerName(self, customer)
        self.__list_of_books = shopping_cart.books_in_cart
        Order.__setPrice(self, shopping_cart)

    def __setCustomerName(self, customer):
        self.__customer_name = customer.name

    def getCustomerName(self):
        return self.__customer_name

    def getBooks(self):
        return self.__list_of_books

    def __setPrice(self, total_price):
        if self.__discount:
            self.__total_price = self.__premium_customer.ApplyDiscount(total_price)
        else:
            self.__total_price = total_price.total_price

    def getPrice(self):
        return self.__total_price
