# Podracer class defined with max_speed, condition (perfect, trashed, repaired)
# and price attributes
class Podracer:
    def __init__(self, max_speed, price):
        self.max_speed = max_speed
        self.price = price
    condition = ['perfect','trashed','repaired']
# Define a repair() method that will update the condition of the podracer
# to "repaired"
    def repair(self):
        return self.condition[2]

# Define a new class, AnakinsPod that inherits the Podracer class 
class AnakinsPod(Podracer):
    def __init__(self, max_speed, price):
        super().__init__(max_speed, price)
    # contains a "boost" method to multiply max_speed by 2
    def boost(self):
        return self.max_speed * 2

# Define another class that inherits Podracer and call this one SebulbasPod
class SebulbasPod(Podracer):
    def __init__(self, max_speed, price):
        super().__init__(max_speed, price)
# contains a method "flame_jet" to update the condition of another podracer to "trashed"
    def flame_jet(self):
        return self.condition[1]


lisas_pod = Podracer(500, 2500)
lbtrash_pod = SebulbasPod(25, 50)
lbana_pod = AnakinsPod(300, 3000)
print(lisas_pod.repair())
print(lbtrash_pod.flame_jet())
print(lbana_pod.boost())

# Encapsulation is being used here by separating the repair and trashed conditions along
# with the boosting of speed, this is good for organizing concerns. 

# Inheritance is also being used which allows us to simply call the values declared in 
# the parent class

# I do not believe Abstraction or Polymorphism are being used here as we aren't hiding
# or transforming anything


# If this problem were done functionally we would not have been able to hide the condition
# variable in one function without writing more lines of code and it would not have been
# separated as it is with the class option

# OOP allowed us to separate processes clearly and reuse variables