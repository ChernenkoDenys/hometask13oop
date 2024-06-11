# Використовуючи всі набуті знання у успадкуванні та інкапсуляції спроектуй просту банківську систему. 
# Створи клас Customer та BankAccount. Ти можеш створювати базові класи, абстрактні класи, на твій розсуд. 
# Customer повинен мати такі атрибути як name, email, customer_id. 
# BankAccount повинен мати balance, owner, account_number. 
# У кастомера повинні бути методи для отримання інфи про атрибути. 
# У BankAccount повинні бути методи поповнення та виведення коштів з усіма валідаціями, 
# а також метод для отримання account_number
import re
  

class Customer:
    
    def __init__(self, name, email, customer_id):
        self.check_valid_types(name, email, customer_id)
        
        self.name = name
        self.__email = email
        self.__customer_id = customer_id
    
    @property    
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, valid_email):
        email_pattern = re.compile(r"^[A-za-z0-9_]+@[A-Za-z]+\.[A-Za-z]{2,}$")
        if not isinstance(valid_email, str) or re.match(email_pattern, valid_email) is None:
            raise TypeError("Email isn't in correct type")
        
        self.__email = valid_email
    
    @email.deleter
    def email(self):
        del self.__email
    
    @property
    def customer_id(self):
        return self.__customer_id
    
    @customer_id.setter
    def customer_id(self, new_customer_id):
        self.__customer_id = new_customer_id
        
    @customer_id.deleter
    def customer_id(self):
        del self.__customer_id
    
    def get_name(self):
        return self.name
    
    def change_name(self, new_name):
        name_pattern = re.compile(r"^[A-Za-z]+$")
        if not isinstance(new_name, str) or re.match(name_pattern, new_name) is None:
            raise TypeError("Name is inccorect type")
        
        self.name = new_name

    @staticmethod
    def check_valid_types(name, email, customer_id):
        name_pattern = re.compile(r"^[A-Za-z]+$")
        email_pattern = re.compile(r"^[A-za-z0-9_]+@[A-Za-z]+\.[A-Za-z]{2,}$")
        
        if not isinstance(name, str) or re.match(name_pattern, name) is None:
            raise TypeError("Name is incorrect type")
        elif not isinstance(email, str) or re.match(email_pattern, email) is None:
            raise TypeError("Email is inccorect type")
        elif not isinstance(customer_id, int):
            raise TypeError("Customer id is inccorect type")
            

class BankAccount:
    
    def __init__(self, balance, owner, account_number):   
        self.check_valid_types(balance, owner, account_number)     
        
        self.__balance = balance
        self.owner = owner
        self.__account_number = account_number
    
    @property
    def balance(self):
        return self.__balance

    @property
    def account_number(self):
        return self.__account_number
    
    @account_number.setter
    def account_number(self, new_acc_number):
        self.__account_number = new_acc_number
    
    @account_number.deleter
    def account_number(self):
        del self.__account_number
    
    def add_balance(self, amount):
        if amount <= 0:
            raise ValueError("Add to balance more than 0")
        
        input_name = input("Write owner name of bank account: ")
        input_email = input("Write owner email of bank account: ")
        
        owner_name = self.owner.get_name()
        owner_email = self.owner.email

        if input_email == owner_email and input_name == owner_name:
            print("Validation passed, operation success")
            self.__balance += amount
        else:
            print("Validation not passed, access denied")
    
    def sub_balance(self, amount):
        if amount <= 0:
                raise ValueError("Add to balance more than 0")
        
        input_name = input("Write owner name of bank account: ")
        input_email = input("Write owner email of bank account: ")
        
        owner_name = self.owner.get_name()
        owner_email = self.owner.email

        if input_email == owner_email and input_name == owner_name:
            print("Validation passed, operation success")
            if amount > self.balance:
                raise ValueError("Cannot sub more amount than balance")
            else:
                self.__balance -= amount

        else:
            print("Validation not passed, access denied")
            
    @staticmethod
    def check_valid_types(balance, owner, account_number):
        if not isinstance(balance, (int,float)):
            raise TypeError("Balance must be either int or float")
        elif not isinstance(owner, Customer):
            raise TypeError("Owner isn't valid type")
        elif not isinstance(account_number, int):
            raise TypeError("Customer ID must be a number")
        

customer_person = Customer('Denys', 'den8@mail.com', 13456)
customer_person.email = 'd@mail.com'
bank_acc = BankAccount(150, customer_person, 1590)

bank_acc.add_balance(150)
print(bank_acc.balance)
