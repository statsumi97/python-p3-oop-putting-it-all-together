#!/usr/bin/env python3

#Shoe in shoe.py has the brand and size passed to __init__, and values can be set to new instance.
#Shoe in shoe.py prints "size must be an integer" if size is not an integer.
#Shoe in shoe.py says that the shoe has been repaired.
#Shoe in shoe.py creates an attribute on the instance called 'condition' and set equal to 'New' after repair.

class Shoe:
    condition = 'New'

    def __init__(self, brand=None, size=0):
        self.brand = brand
        self.size = size
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size (self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = 'New'