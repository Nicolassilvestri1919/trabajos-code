
class Fruit:
    def __init__(self, name, color, taste, is_rotten, price):
        self.name = name
        self.color = color
        self.taste = taste
        self.is_rotten = is_rotten
        self.price = price
        
    def is_delicious(self):
        if self.is_rotten:
            return f"The {self.name} is rotten."
        else:
            return f"The {self.name} is good."
    
    def get_info(self):
        return f"The {self.name} is {self.color}, has a {self.taste} taste, and costs ${self.price}."
    
 
    def __del__(self):
        print("Apple and Banana erased")
    
 
apple = Fruit("Apple", "Red", "sweet", False, 0.75)
banana = Fruit("Banana", "Yellow", "sweet", True, 0.5)
 
 
print(apple.is_delicious())  
print(apple.get_info())      
 
print(banana.is_delicious())  
print(banana.get_info())      
 
 
 
apple.color = "Green"
apple.price = 1.0
 
del apple
del banana
 
 
