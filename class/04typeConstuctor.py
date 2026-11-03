class Car:     
    def __init__(self):        
        self.brand = "Toyota" 
car1 = Car() 
print(car1.brand) 

class Car: 
    def __init__(self, brand): 
        self.brand = brand 

car1 = Car("Honda") 
car2 = Car("BMW") 

print(car1.brand) 
print(car2.brand) 