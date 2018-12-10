
#############___________INHERITANCE__________________
# It lets you creat a custom class that "inherits" most of its 
# behavior from another class. 

class Cat: # Cat instance is stored in variable honey

    def __init__(self):
        # every Cat comes into this world tired and hungry
        self.tired = True
        self.hungry = True

    def sleep(self):
        self.tired = False
        # a Cat always wakes up hungry
        self.hungry = True

    def eat(self):
        if self.hungry:
            self.hungry = False
        else:
            # eating when already full makes a Cat sleepy
            self.tired = True

    def noise(self):
        # After she wakes up her noise() method stops the 
        # purrcolator and she starts squalling
        if self.tired:
            return "purrcolator"
        else:
            return "Breakfast yowl!"
def main():
    honey = Cat() # Cat() is stored in honey
    print("honey says:", honey.noise())
    honey.sleep()
    print("After sleeping, Honey says:", honey.noise())
    honey.eat()
    print("After eating, Honey still says:", honey.noise())
    honey.eat()
    print("After eating again, Honey says:", honey.noise())

if __name__ == "__main__":
    main()

# To demonstrate INHERITANCE, we can create a tigher subclass 
# that inherits several traits from cat but has some of its own. 

class Tiger(Cat): # notice the (Cat) in parentheses

    def angry(self):
        # a Tiger is angry whenever it is both hungry and tired
        return self.tired and self.hungry

    def noise(self):
        if self.angry():
            # an angry Tiger says GRRRR!
            return "GRRRR!"
        else:
            # a non-angry Tiger behaves like a Cat
            return Cat.noise(self)

def main():
    tony = Tiger()
    print("Tony says:", tony.noise())
    tony.sleep()
    print("After sleeping, Tony says:", tony.noise())
    tony.eat()
    print("After eating, Tony still says:", tony.noise())
    tony.eat()
    print("After eating again, Tony says:", tony.noise())

if __name__ == "__main__":
    main()

# Add a class for domesticated cats:

class HouseCat(Cat):

    def __init__(self, name):
        # first, initialize as a normal Cat
        Cat.__init__(self)
        # then set the name attribute
        self.name = name

    def satisfied(self):
        return not self.hungry and not self.tired

    def noise(self):
        if self.satisfied():
            return "Hello, my name is " + self.name + "!"
        else:
            return Cat.noise(self)

def main():
    safa = HouseCat("Safa")
    print("Safa says:", safa.noise())
    safa.sleep()
    print("After sleeping, Safa says:", safa.noise())
    safa.eat()
    print("After eating, Safa says:", safa.noise())
    safa.eat()
    print("After eating again, Safa says:", safa.noise())

if __name__ == "__main__":
    main()
