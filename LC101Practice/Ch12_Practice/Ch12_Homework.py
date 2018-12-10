# TODO: add the Car class

class Car:
    
    def __init__(self, init_gas):
        
        self.gas_level = init_gas
        
    def get_gas_level(self):
        return self.gas_level
    
    def add_gas(self, gas):
        return self.gas_level + gas
    
    def fill_up(self):
        if self.get_gas_level() >= 13:
            return 0
        return 13 - self.get_gas_level()
    
    def __str__(self):
        return "gas level" + str(self.get_gas_level)

# some tests to check your code, Do Not Post These in Vocareum
from test import testEqual
testEqual( Car(10).fill_up(), 3 )
testEqual( Car(20).fill_up(), 0 )
testEqual( Car(5.5).fill_up(), 7.5 )
testEqual( Car(12.5).fill_up(), 0.5 )
testEqual( Car(13).fill_up(), 0 )
