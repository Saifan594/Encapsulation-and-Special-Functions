print("\033c")

class Computer:
    def __init__(self):
        self.__maxPrice = 900
    
    def printPrice(self):
        print(f"Selling Price: {self.__maxPrice}")
    
    def setMaxPrice(self, price):
        self.__maxPrice = price

c = Computer()
c.printPrice()

c.__maxPrice = 1500
c.printPrice()

c.setMaxPrice(1500)
c.printPrice()