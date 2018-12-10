class Chatbot:
    """ An object that can engage in rudimentary conversation with a human. """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        self.bored = False
        self.normal = True
        """ Returns the Chatbot's way of introducing itself. """
        return "Hello, my name is " + self.name

    
    def response(self, prompt_from_human):
        """ Returns the Chatbot's response to something the human said. """
        return "It is very interesting that you say: '" + prompt_from_human + "'"


def main():
    
# make a chatbot
    sally = Chatbot("Sally")
# introduce the chatbot and allow the user to say something
    human_message = input(sally.greeting())
# respond to the user
    print(sally.response(human_message))
    

    
if __name__ == "__main__":
    main()
    
# TODO define a class called BoredChatbot

class BoredChatbot(Chatbot):
    
    
    def bored(self):
        # An Chatbot with a short attention span gets bored
        if len(human_message) > 20:
            return BoredChatbot.response(self)
        else:
            return Chatbot.response(self)
        
    
def main():
    
    bored = BoredChatbot(self)
    return "Hello my name is " + self.name
    bored.response(self, prompt_from_human)
    """ Returns the Chatbot's response to something the human said. """
    return "zzz... Oh excuse me, I dozed off reading your essay." + prompt_from_human + "'"

        
if __name__ == "__main__":
    main()