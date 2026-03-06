import random

class Coin():
    
    def __init__(self, value, type):
        self.value = value
        self.type = type
    
    def __str__(self):
        return "Coin: {} {}".format(self.value, self.type)
    
    def spinCoin(self):
        return random.randint(0,1) 
    
    
coin = Coin(1, "Euro")
print(coin)

res = coin.spinCoin()

if res:
    print("HEAD")
else:
    print("CROSS")


