class Fraction:

    """ An example of a class for creating fractions """
    def __init__(self, top, bottom): # defining numerator and denominator

        self.num = top
        self.den = bottom 

    def __repr__(self): 
        return str(self.num) + "/" + str(self.den)

    def get_numerator(self):
        return self.num

    def get_denominator(self):
        return self.den

def main():
    rug = Fraction(5, 7)
    print(rug)

    print(rug.get_numerator())
    print(rug.get_denominator())

if __name__ == "__main__":
    main()
