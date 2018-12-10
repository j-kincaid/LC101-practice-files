def find_gcd(numerator, denominator):
    while numerator % denominator != 0:
        old_num = numerator
        old_den = denominator

        numerator = old_den
        denominator = old_num % old_den

    return denominator

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

def main():
    myfraction = Fraction(12, 16)

    print(myfraction)
    myfraction.simplify()
    print(myfraction)

if __name__ == "__main__":
    main()