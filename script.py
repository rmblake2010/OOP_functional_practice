
#Function that flattens & sorts an array of integers in an ascending order.
#function must follow functional progamming paradigm


def flatten_sort(*list):
    #declaring a new array so that the function is not manipulating data outside its scope
    sorted_list = []

    for item in list:
        for i in item:
            sorted_list.append(i)

    return sorted(sorted_list)

print(flatten_sort([3,4,2,5,23,2], [432,5342, 32]))

#How does this solution ensure data immutability?
# This data solution ensures the data is ummutable because it defines a new array within the function scope and returns that array.
# If the function manipulated the inputed array it would not be immutable

#Is this solution a pure function?
# I believe so. Because it will always return a sorted array given that an array is given as an argument.

#Is this solution a higher order function? Why or why not?
# No, because it does not accept a function as an argument or return another function.

#Would it have been easier to solve this problem using a different programming style?
# I think that this method is possibly less cumbersome that a OOP approach

#Why in particular is functional programming a helpful paradigm when solving this problem?
# Because it is a problem that can be re used and with any array that needs to be flattened & sorted.(?)

#_________________________________________________________________________________________________________________________

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"
        print(f"your podracers condition is now: {self.condition}")

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    def flame_jet(self, opponent):
        opponent.condition = "trashed"

# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
# Encapsulation: This class does demonstrate encapsulation because it keeps relitave functions and data within a class, and is distinct between different variables of the class
# #Abstraction: This class also exhibits abstraction because it can be used for any type  of "pod racer"
# Inheritance: This class is a good example of inheritance because it is passed down to two children classes.
# Polymorphism: i believe the is exemplified in the children classes. These two classes use the same interface as the podracer including there own functions within the class.
#  