# Another method for our Fraction class!
# The arithmetic method works for adding fractions 
# only when their denominators are the same. 
# The add method will take a Fraction as a parameter. 

def find_gcd(numerator, denominator):
    while numerator % denominator != 0:
        old_num = numerator
        old_den = denominator

        numerator = old_den
        denominator = old_num % old_den

    return denominator 

#  ^ Same old get_gcd() function

class Fraction:

    def __init__(self, top, bottom):

        self.num = top        # the numerator is on top
        self.den = bottom     # the denominator is on the bottom

    def __repr__(self):
        return str(self.num) + "/" + str(self.den)

    def simplify(self):
        common = find_gcd(self.num, self.den)

        self.num = self.num // common
        self.den = self.den // common

    def __add__(self,fraction2): 
        # Here is the fraction as parameter

        new_num = self.num * fraction2.den + self.den * fraction2.num
        new_den = self.den * fraction2.den

        common = find_gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)
        # The new Fraction represents the sum. 

def main():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 4)

    f3 = f1 + f2    # calls the __add__ method of f1
    print(f3)

if __name__ == "__main__":
    main()
