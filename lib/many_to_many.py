class Author:
    
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]

    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self):
        sum_of_royalties = 0
        for contract in Contract.all:
            if contract.author == self:
                sum_of_royalties += contract.royalties
        return sum_of_royalties


class Book:

    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise ValueError("Author is expected to be of type Author Class.")
        else:
            self.author = author
        if not isinstance(book, Book):
            raise ValueError("Book is expected to be of type Book Class.")
        else:
            self.book = book
        if not isinstance(date, str):
            raise ValueError("Date is expected to be of type String Class.")
        else:
            self.date = date
        if not isinstance(royalties, int):
            raise ValueError("Royalties is expected to be of type Integer Class.")
        else:
            self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
