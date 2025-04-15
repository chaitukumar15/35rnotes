#blueprint
#..........................................
class   Car:
   #constructor method
   def __init__(self,name,model):
      #self -> instance of the class->  current object
    # __ init__ -> constructor method -> define properties of the object      
      self.name= name;
      self.model= model
      print(self,"obj")
      print("Car name is",self.name)


#.....................................................
# created an object
audi= Car("audi","audi model")


bmw= Car("bmw","bmw model")



