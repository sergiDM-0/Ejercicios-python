class Microwave:
    def __init__(self,brand,power_rating):
        self.brand = brand
        self.power_rating = power_rating


smeg: Microwave = Microwave("Smeg",1000)
print(smeg.brand)
print(smeg.power_rating)