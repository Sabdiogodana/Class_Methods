class  Vehicle:
    color = "White"
    def __init__(self,name,max_speed,mileage):
        self.name = name 
        self.max_speed = max_speed
        self.mileage = mileage


    def   my_car(self):
        return f"I bought {self.color} {self.name} which has speed of {self.max_speed} and {self.mileage} mileage"

    def   congratulate(self):
        return f"Hello Sabdio congratulation for buying {self.color} {self.name}which has speed of {self.max_speed} and {self.mileage} mileage "

    def capacitor(self,capacity ):       