#blueprint
#..........................................
# class   Car:
#    #constructor method
#    def __init__(self,name,model):   
#       #self -> instance of the class->  current object
#     # __ init__ -> constructor method -> define properties of the object  
#     # instance varables -> name and model    
#       self.name= name;
#       self.model= model
#       print(self,"obj")
#       print("Car name is",self.name)

# #.....................................................
# # created an object


# audi= Car("audi","audi model")

# print(audi.a())







#   
# class -> blueprint of the object
# object -> instance of the class


class Biriyani:
      # constructor method

      def __init__(self,oil,meat,rice):
         #  instance properties
          self.oil=oil
          self.meat=meat
          self.rice=rice
      # instance method
      # instance methodds ->  methods which are used to access the instance properties of the class
      def cook(self):
          print(self.meat+" biriyani prepared")  
         

musroom_biriyani=Biriyani("oil","musroom","sonamasura_rice")
print(musroom_biriyani.oil)


musroom_biriyani.meat="mutton"

musroom_biriyani.cook()

panner_biriyani=Biriyani("oil","panner","sonamasura_rice")
print(panner_biriyani.oil)

panner_biriyani.cook()






# bike 
# gears -> 
# color -> 
# model->

class Bike: 
      def __init__(self,color,gears,model):
          self.color=color
          self.gears=gears
          self.model=model
      
      def Break(self):
            print(model+"r15 applied the brake") 
             # self.model
     


yamaha=Bike("red",5,"r15 v4")

yamaha.Break("hi")

royal_enfield=Bike("black",6,"classic 350")

