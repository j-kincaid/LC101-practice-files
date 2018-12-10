# Sameness can be ambiguous. Ok, When like
# you have two fractions. 

class Fraction:

    def __init__(self, top, bottom):

        self.num = top        # the numerator is on top
        self.den = bottom     # the denominator is on the bottom

    def __repr__(self):
        return str(self.num) + "/" + str(self.den)

    def same_fraction(f1, f2):
        return (f1.get_numerator()) == f2.get_numerator()) and (f1.get_denominator()) == f2.get_denominator())

myfraction = Fraction(3, 4)
yourfraction = Fraction(3, 4) # They contain the same numerator and denominator
print(myfraction is yourfraction) # False

ourfraction = myfraction 
print(myfraction is ourfraction) # True but they are aliases of the same object. 
## The = operator produces the shallow equality result.  

    
# I keep getting an error when I run this but the point is 
# that sameness is nuanced. 
# == on Points returns False
# == on lists returns True

