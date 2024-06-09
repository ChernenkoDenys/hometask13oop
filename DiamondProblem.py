# Створіть діамантову проблему успадкування з класів A, B, C і D, 
# де D успадковує від B і C, а B і C успадковують від A. 
# Кожен клас повинен мати метод introduce() який буде повертати інфу про клас.
# Створіть інстанси цих класів та повикликайте метод introduce(). 
# Приберіть у деяких класах цей метод і протестуйте те як python 
# вирішує проблему діамантового успадкування у цьому випадку.


class A:
    
    @classmethod
    def introduce(cls):
        return f"{cls.__name__}"

class B(A):
    
    @classmethod
    def introduce(cls):
        return f"{cls.__name__}"


class C(A):
    
    @classmethod
    def introduce(cls):
        return f"{cls.__name__}"
    
class D(B, C):
    
    @classmethod
    def introduce(cls):
        return f"{cls.__name__}"
    
class_a = A()
class_b = B()
class_c = C()
class_d = D()

print(class_a.introduce())
print(class_b.introduce())
print(class_c.introduce())
print(class_d.introduce())