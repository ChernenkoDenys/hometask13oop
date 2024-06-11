import re


class User:
    
    def __init__(self, name, user_id):
        self._name = name
        self._user_id = user_id

    @property
    def name(self):
        return self._name
    
    @property
    def user_id(self):
        return self._user_id
    
    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id
        
    def __str__(self):
        return f"User: {self._name}, with user_id: {self._user_id}"
    
    def __rerp__(self):
        return f"User({self._name}, {self._user_id})"
    

class Book:
    total_copies = 0
    
    def __init__(self, title, author, isbn, copies, total_copies):
        self.validate_isbn(isbn)
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        Book.total_copies += copies
    
    def update_total_copies(self, type):
        if type == 'del':
            self.total_copies -= 1
        elif type == 'add':
            self.total_copies += 1
        else:
            raise ValueError("Unsupported operation") 
        
    def update_copies(self, type):
        if type == 'del':
            self.copies -= 1
        elif type == 'add':
            self.copies += 1
        else:
            raise ValueError("Unsupported operation")
    
    @staticmethod
    def validate_isbn(isbn):
        isbn_pattern = re.compile(r"^ISBN [0-9]{1}-[0-9]{3}-[0-9]{5}-[0-9]{1}$")
        if re.match(isbn_pattern, isbn) is None:
            raise TypeError("ISBN is wrong type")
    
    def __str__(self):
        return f"Book with title: {self.title}, and author is: {self.author}"

    def __repr__(self):
        return f"Book(Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Copies: {self.copies}, Total: {self.total_copies})"
    

class Library:
    library_list = []
    
    def __init__(self):
        self.books = []
        self.__users = []
        Library.library_list.append(self)
               
    def register_user(self, user):
        if user not in self.__users:
            self.__users.append(user)
        else:
            print("User already registered")
            
    @property
    def user(self):
        return self.__users
    
    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return "Not found"
        
    def show_all_books(self):
        for book in self.books:
            print(book)
       
    @classmethod
    def get_all_libraries(cls):
        return cls.library_list

    def __repr__(self):
        return f"Library with books: {self.books}, and users: {self.__users}"
    
    
class Customer(User):
    
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self._borrowed_books = []

    def borrow_book(self, library: Library, book: Book):
        found_book = library.find_book_by_isbn(book.isbn)
        if found_book == "Not found" or found_book.copies <= 0:
            print("Book wasn't found or no copies available")
        else:
            found_book.update_copies('del')
            self._borrowed_books.append(found_book)
        
    def return_book(self, library: Library, book: Book):
        found_book = library.find_book_by_isbn(book.isbn)
        if book in self._borrowed_books and found_book != "Not found":
            found_book.update_copies('add')
            self._borrowed_books.remove(book)
        else:
            print("This book was not borrowed by the customer")

    @property
    def borrowed_books(self):
        return self._borrowed_books
    
    def __repr__(self):
        return f"Customer(Name: {self.name}, User_ID: {self._user_id}, Borrowed_Books: {self._borrowed_books})"

class Employee(User):
    
    def __init__(self, name, user_id, salary, library: Library):
        super().__init__(name, user_id)
        self.__salary = salary
        self.library = library
        
    def add_book_to_library(self, book: Book):
        existing_book = self.library.find_book_by_isbn(book.isbn)
        if existing_book == "Not found":
            self.library.books.append(book)
        else:
            existing_book.update_copies('add')
            existing_book.update_total_copies('add')
    
    def delete_book_from_library(self, book: Book):
        existing_book = self.library.find_book_by_isbn(book.isbn)
        if existing_book != "Not found" and existing_book.copies > 0:
            existing_book.update_copies('del')
            existing_book.update_total_copies('del')
            if existing_book.total_copies == 0:
                self.library.books.remove(existing_book)
        else:
            print("Book not found in library or no copies left")
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, new_salary):
        self.__salary = new_salary
    
    def __repr__(self):
        return f"Employee(Name: {self.name}, UserID: {self.user_id}, Salary: {self.__salary}, Library: {self.library})"


city_library = Library()
second_library = Library()


book_1_city = Book('1984', 'George Orwell', 'ISBN 0-061-96436-0', 3, 3)
book_1_second = Book('1984', 'George Orwell', 'ISBN 0-061-96437-0', 2, 2)
book_2 = Book('Rofl', 'Me', 'ISBN 0-061-96431-0', 2, 2)

customer_1 = Customer('Denys', 1)
employee_1 = Employee('Ivan', 2, 4500, city_library)
employee_2 = Employee('John', 3, 4500, second_library)

employee_1.add_book_to_library(book_1_city)
employee_2.add_book_to_library(book_1_second)
employee_2.add_book_to_library(book_2)

customer_1.borrow_book(city_library, book_1_city)

