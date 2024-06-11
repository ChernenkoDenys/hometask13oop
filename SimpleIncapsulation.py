# Створіть клас Account та приватний атрибут balance. 
# Додайте метод який буде повертати значення приватного атрибуту. 
# Створіть протектед атрибут account_holder.


class Account:
    
    def __init__(self, account_holder, balance=0):
        self.__balance = balance
        self._account_holder = account_holder
        
    def check_balance(self):
        return f"Your balance is: {self.__balance}"
    
    
account_one = Account('Denys', 150)
print(account_one.check_balance())