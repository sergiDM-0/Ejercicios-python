class Microwave:
    def __init__(self,brand,power_rating):
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on = False

    def turn_on(self):
        if self.turned_on:
            print(f"The microwave {self.brand} is already on")
        else:
            self.turned_on = True
            print(f"The microwave {self.brand} is now on")

    def turn_off(self):
        if self.turned_on:
            self.turned_on = False
            print(f"The microwave {self.brand} is now off")
        else:
            print(f"The microwave {self.brand} is already off")

    def run(self,seconds : int):
        if self.turned_on:
            print(f"The microwave {self.brand} is running for {seconds} seconds")
        else:
            print(f"The microwave {self.brand} is not on")

smeg = Microwave("Smeg",1000)
smeg.turn_on()
smeg.run(10)
smeg.turn_off()