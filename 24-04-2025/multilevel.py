
# parent
# bike -> class 
#  method -> start 
# properties -> gears -> \


class Bike:
    def __init__(self,gears):
        self.gears=gears

    def start(self):
        return "hi this is getting started "


class Bike1(Bike):
    def __init__(self,model,gears):
        self.model=model
        super().__init__(gears);

    def breakk(self):
        return "hi i am applying breaks"


class Bike2(Bike1):
    def __init__(self, model, gears,color):
        super().__init__(model, gears)
        self.color=color

    def cor(self):
        return "hi this is "+ self.color



v=Bike2()
# child

# bike2-> class 

#  model -> propertity

# method -> break -> 