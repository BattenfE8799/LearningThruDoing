"""
module for items class 
"""


class Item():
    """ The base class for all items"""
    
    def __init__(self, name, description, value, weight, can_pickup, can_drop):
        """ attributes for all items to have """ 
        # ^^ constructor that is called whenever a new object is created 
        # initializes all attributes for the class
        # sets the attribute as the object/variable that was passed as a parameter
        self.__name = name      # I am using __ before each attribute to show its different from the local variables for less confusion                
        self.__description = description
        self.__value = value
        self.__weight = weight
        
        # flags for items
        self.__can_pickup = True
        self.__can_drop = True
        
    def __str__(self): 
        # ^^ allows the ability to print an object and see useful information
        # returns string of information about the object that the player can understand
        return "{}\n=====\n{}\nValue: {}\nWeight: {}\n".format(self.name, self.description, self.value, self.weight)
    
class Gold(Item):
    """ Gold class """
    #subclass of Items class that deals with gold/treasure/money
    def __init__(self, amount):
        # called the superclass/baseclass(Items) constructor, it needs to be called if it is not exactly like the superclass's
        super().__init__(name="Gold",description="A round coin with {} stamped on the front.".format(str(self.amount)), value=self.amount,weight=0,can_pickup=True, can_drop=False)
        # add the attributes that are needed and are not in the superclass
        self.__amount = amount         # defines the amount of this gold
        
        # if a subclass doesn't define its own str method/or other method that the superclass has, the superclass method will be used in its place
        # for this class, the value is the same as the amount so theres no reason to print out both attributes
        
class Weapon(Item):
    """ Weapon class. subclass of Item class"""
    
    def __init__(self,name,description,value,weight, can_pickup, can_drop, damage, durability):
        # called the superclass/baseclass(Items) constructor, it needs to be called if it is not exactly like the superclass's
        super().__init__(name="Gold",description="A round coin with {} stamped on the front.".format(str(self.amount)), value=self.amount,weight=0,can_pickup=True, can_drop=False)
        # add the attributes that are needed and are not in the superclass
        self.__damage = damage         # defines the amount of damage the weapon does
        self.__durability = durability # defines the durability of the weapon
        
class Rock(Weapon):
    """rock weapon class"""
    
    
        
        
        
        
        