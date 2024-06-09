# Створіть клас Vehacle який матиме атрибути make та model та метод get_info() 
# який буде повертати інформацію про марку та модель авто. 
# Створіть ще два класи Car та Moto які будуть додавати 
# додаткові атрибути wheels і успадковуватись від Vehacle . 
# Створіть сутності класів Car та Moto та викличте там метод get_info()


class Vehacle:
    
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def get_info(self):
        return f"Information is make is: '{self.make}', model is: '{self.model}'"


class Car(Vehacle):
    
    def __init__(self, make, model, wheels):
        super().__init__(make, model) 
        self.wheels = wheels
        
    def get_info(self):
           return f"{super().get_info()}, Wheels: {self.wheels}"


class Moto(Vehacle):
    
      def __init__(self, make, model, wheels):
            super().__init__(make, model) 
            self.wheels = wheels
    
      def get_info(self):
           return f"{super().get_info()}, Wheels: {self.wheels}"
            
            
auto = Car("Germay", "Mercedes", 4)
motocycle = Moto("Japan", "Jamaha", 2)

print(auto.get_info())
print(motocycle.get_info())
