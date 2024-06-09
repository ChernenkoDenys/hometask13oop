# До попереднього завдання додайте клас Electric та додайте туди приватний атрибут battery та метод charge() 
# який буде встановлювати атрибут battery до 100. 
# Створіть окремий клас ElectricCar та ElectricMoto та успадкуйтесь від Vehicle та Electric. 
# Створіть інстанси всіх класів, та викличте метод mro для кожного інстансу, 
# щоб подивитись порядок успадкування в кожному класі.


class Electric:
    
    def __init__(self, battery=100):
        self.__battery = battery
    
    def get_battery_info(self):
        return f"Battery is {self.__battery}"


class Vehicle:
    
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def get_info(self):
        return f"Information is make is: '{self.make}', model is: '{self.model}'"


class Car(Vehicle):
    
    def __init__(self, make, model, wheels=4):
        super().__init__(make, model) 
        self.wheels = wheels
        
    def get_info(self):
           return f"{super().get_info()}, Wheels: {self.wheels}"


class Moto(Vehicle):
    
      def __init__(self, make, model, wheels=2):
            super().__init__(make, model) 
            self.wheels = wheels
    
      def get_info(self):
           return f"{super().get_info()}, Wheels: {self.wheels}"
       
       
class ElectricCar(Vehicle, Electric):
    
    def __init__(self, make, model, wheels=4):
         super().__init__(make, model)
         self.wheels = wheels

    def get_info(self):
        return f"{super().get_info()}, Wheels: {self.wheels}"
    
    
class ElectricMoto(Vehicle, Electric):
    
    def __init__(self, make, model, wheels=2):
         super().__init__(make, model)
         self.wheels = wheels

    def get_info(self):
            return f"{super().get_info()}, Wheels: {self.wheels}"

    
motocycle = Moto('Jamaha', 'Japan', 2)
automobile = Car('Germany', 'Mercedes', 4)
electro_moto = ElectricMoto('Jamaha', 'Japan', 2)
eletric_car = ElectricCar('Germany', 'Mercedes', 4)
electir = Electric()

print(electir.get_battery_info())
print(eletric_car.get_info())


print(Moto.mro())
print(Car.mro())
print(ElectricCar.mro())
print(ElectricMoto.mro())
print(Electric.mro())