# translates to 1's & 0's as it runs
                # translates

class Player:
    """[This is a class documentation block comment.]
    (What this is)
    (What the methods are and do)
    
    Attributes: [attributes are just variables with data]
        option: ADD STUFF HERE
        keep_playing: ADD STUFF HERE
        card_guess: ADD STUFF HERE
    """
    
    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Player): An instance of Player.
        """
        self.option = "y"
        self.keep_playing = True
        self.card_guess = ""

    def choice(self):
        """Decides whether to keep playing the game or not. 

        Args: 
            self (Player): An instance of Player.
        """
        self.option = input("Keep Playing y/n ")
        if self.option == "n":
            self.keep_playing = False

    def guess(self):
        """Decides whether the guess is higher or lower. 

        Args: 
            self (Player): An instance of Player.
        """
        self.card_guess = input("Higher or Lower? h/l ")
        
        
    #Do we need this, below?
"""
    def guess(self):
        guess = input("Higher or Lower? h/l")
        return guess
"""