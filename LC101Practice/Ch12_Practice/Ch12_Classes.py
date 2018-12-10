class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

        self.area = self.length * self.width # Recalculate every time 
        # any of the other parameters change

def area(self):
    return self.width * self.length

def is_smaller(self, another_rec):
    return self.Area() < another_rec.area()

def perimeter(self):
    return self.width * 2 + self.length * 2

def is_square(self):
    return self.width == self.length


rec = Rectangle(5,7)
print(rec.area())
rec.length = 8
print(rec.area())