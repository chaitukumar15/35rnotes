


# object-> instance of a class
# class-> blueprint

# class -> properties and behaviour(actions)

# class pare:
#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         return "hi this is parent class" 

# class child(pare):
#     def __init__(self, name1,name):
#         super().__init__(name)
#         self.name1 = name1

#     def display1(self):
#         return "hi this is child class"
     
# # 1. nned to add parent name to child class class child(pare):



# v=child("chaitanya")

# print(v.display())

# print(v.display1())





# name-> bike

# pro -> color , model 


# method-> start 


# CHILD ->

# 1. BIKE1 
# PRO -> GEARS 


#  NOOFGEARS -> I HAVE 3 GEARS 


# class bike:
#     def __init__(self,color,model):
#         self.color = color;
#         self.model = model

#     def start(self):    
#         return "hi this is bike started"



# class bike1(bike):
#     def __init__(self,gears,color,model):

#         super().__init__(color,model)
#         self.gears = gears


#     def noofgears(self):
#         return f"i have {self.gears} gears"


# r15=bike1(6,"silver","v4")


# print(r15.noofgears())

# print(r15.start())
# print(r15.color)
# print(r15.mo


# class person:
#     def display(self):
#         return "i am a person"
# class student(person):
#     def study(self):
#         return "i am studying"
# a=student()
# print(a.display())
# print(a.study())  
       


# Create a class Vehicle with the following:

# A property brand

# A method start() that prints "Vehicle is starting..."

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return "Vehicle is starting..."
    

# Then, create a class Car that inherits from Vehicle and adds:

# A property model

# A method drive() that prints "Car is driving..."

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        return "Car is driving..."  
    
# Create an object of the Car class, set brand to "Toyota" and model to "Corolla".

# Print both brand and model.

# Call both start() and drive() methods.

my_car = Car("Toyota", "Corolla")

print(my_car.brand)  # Output: Toyota
print(my_car.model)  # Output: Corolla
print(my_car.start())  # Output: Vehicle is starting...
print(my_car.drive())  # Output: Car is driving...



