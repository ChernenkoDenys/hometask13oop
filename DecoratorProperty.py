# До класу Account додайте за допомогою декоратора @property гетер та сетер для приватного атрибуту balance. 
# При встановлені цього параметру зробіть перевірку у сетері, щоб це значення було більшим за 0. 


class Account:
    
    def __init__(self, account_holder, balance=0):
        self.__balance = balance
        self._account_holder = account_holder
        
    def check_balance(self):
        return f"Your balance is: {self.__balance}"
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter    
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Cannot set the balance less than zero")
        
        self.__balance = amount
    

    
    
account_one = Account('Denys', 150)
print(account_one.balance)
try:
    account_one.balance = -150
except ValueError as e:
    print(e)  


account_one.balance = 200
print(account_one.check_balance())  