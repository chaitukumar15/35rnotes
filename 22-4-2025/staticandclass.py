

# class ->blueprint for creating objects
# object -> instance of a class 1.properties(atributes/varables) 2.behaviour(methods/actions)



# man ->  properties -> hand = 2 , legs =2 eys =2, nose=1, mouth=1 -> (variables)
# # behaviour -> walk, talk, eat, sleep, run -> -> `methods/actions`
# methods-> functions inside a class

# object conssits of 1. properties 2. behaviour

# class ->  blueprint of both properties and behaviour(actions)



# create properties -> dot (.)




# instance -> pro | methods 
# class methods | properties

# object-> real time entity (properties and behaviour(actions))
# class -> combinations of properties and behaviour(actions) -> blueprint

class bike:
    model="v1" 
# class variable -> shared by all instances(object) of the class
    def __init__(self,color,gears):
         self.color=color;
         self.gears=gears
        #  self.model=model

    # instance method -> self is the instance of the class
    # self is needed
    def g(self):
       return "hello"+self.color
    
    @classmethod
    def j(cla):
        return f" {cla.model }"
    @staticmethod
    def add():
        return "hi"
    
shine=bike("red",4)


print(shine.j())








