# translates to 1's & 0's as it runs
                # translates

class Player:
    """[This is a class documentation block comment.]
    Allows user to interact with the game. User can choose to keep playing 
    and choose high or low.
    
    Attributes: [attributes are just variables with data]
        option: User's choice of "Y" to choose to keep playing.
        keep_playing: Boolean value -- from option (Y): set True to keep playing.
        card_guess: sets string value for card value
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
        # Removed guess variable. Used card_guess attribute instead.
        
        # Note to team: Add User Input Validation in 
        # the future to make code idiot proof.
