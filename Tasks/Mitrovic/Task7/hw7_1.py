cart_list = []


class Book:
    __titles = ['Tom Soyer', 'Around the world in 80 days', 'Black Holes', 'Treasure Island', 'Jungle Book',
                'Another category']
    __default_title_number = -1

    def __init__(self, title, author, ISBN, price):
        self.__title_of_book = title
        self.author = author
        self.price = price
        self.set_ISBN(ISBN)

    def __str__(self):
        return self.__title

    def __set_title(self, title):
        if title in Book.__titles:
            self.__title = title
        else:
            self.__title = Book.__titles[Book.__default_title_number]

    def get_title(self):
        return self.__title

    __title_of_book = property(get_title, __set_title)
    title = property(get_title)

    def set_price(self, price):
        self._price = price

    def get_price(self):
        return f'{self._price} dollars'

    price = property(get_price, set_price)

    def get_ISBN(self):
        return self._ISBN

    def set_ISBN(self, ISBN):
        if len(ISBN) == 13:
            self.ISBN = ISBN
        else:
            print('Enter a correct ISBN')


class Ebook(Book):
    def __init__(self, title, author, ISBN, price, format, filesize, downloadlink):
        self.format = format
        self._filesize = filesize
        self._downloadlink = downloadlink

        super().__init__(title, author, ISBN, price)

    def _set__filesize(self, filesize):
        self._filesize = filesize

    def get_filesize(self):
        return f"{self._filesize} Mb"

    def _set__downloadlink(self, downloadlink):
        if self.downloadlink[0:7] == 'https://':
            self.downloadlink = downloadlink
        else:
            print('enter a correct link')

    def get_downloadlink(self):
        return self._downloadlink

    filesize = property(get_filesize, _set__filesize)
    downloadlink = property(get_downloadlink, _set__downloadlink)


class PhysicalBook(Book):

    def __init__(self, title, author, ISBN, price, weight, in_stock):
        self.weight = weight
        self.in_stock = in_stock

        super().__init__(title, author, ISBN, price)

    def __str__(self):
        return self.title

    def set_weight(self, weight):
        self._weight = weight

    def get_weight(self):
        return f'{self._weight} gramm'

    weight = property(get_weight, set_weight)


class Customer:

    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.money = 100
        self.book = None

    def __str__(self):
        return self.name

    def info(self):
        print(f'Name:{self.name}')
        print(f'Email:{self.email}')
        print(f'Address:{self.address}')
        print(f'Money:{self.money}')
        print(f'Book:{self.book}')

    def buy_book(self, book, price):

        if self.money >= price:
            self.make_deal(book, price)
            cart_list.append(price)
        else:
            print('Not enough money')

    def make_deal(self, book, price):
        self.money -= price
        self.book = book


class PremiumCustomer(Customer):
    def __init__(self, name, email, address, discount):
        self.discount = discount

        super().__init__(name, email, address)

    def final_price(self, discount):
        final_price = self.price * (100 - discount) / 100
        return final_price

    def buy_book_vip(self, book,price,discount):
        price == PremiumCustomer.final_price(discount)
        if self.money >=price:
            self.make_deal(book, price)
        else:
            print('Not enough money')

        super().make_deal(self, book, price)


twen = Book('Tom Soyer', 'Mark Twen', '6737238904', 15)
defoe = Book('Robinson Crusoe', 'Daniel Defoe', '5672343459123', 3)
print(twen.__dict__)
print(twen.title)
print(twen._Book__title_of_book)
print(defoe.title)
print(defoe.__dict__)
print(defoe.price)
print(twen)
print(defoe)

kipling = Ebook('Jungle book', 'Kipling', '5678943221234', 14, 'pdf', 765, 'https://mail.ru')
print(kipling.format)

hawking = PhysicalBook('Black Holes', 'Stephen Hawking', '9876543098234', 30, 564, True)
print(hawking.in_stock)
print(hawking.weight)
peter = Customer('Peter', 'peter@mail.ru', 'Belarus,city Minsk')
print(peter)
print(peter.address)

peter.info()
peter.buy_book(hawking, 30)
peter.info()
peter.buy_book(twen, 15)
peter.info()
peter.buy_book(kipling, 35)
peter.info()
print(cart_list)

ivan = Customer('Ivan', 'ivan@mail.ru', 'Switzerland, city Basel')
ivan.info()
ivan.buy_book(defoe, 3)
ivan.info()
ivan.buy_book(hawking, 30)
ivan.info()
print(cart_list)

danil = PremiumCustomer('Danil', 'danil@mail.ru', 'Germany,city Berlin', 20)
danil.info()
danil.buy_book_vip(defoe,3, 20)
danil.info()

