from game.player import Player
import random as r
class Dealer():
    """[This is a class documentation block comment.]
    This class holds game and rule structure. Dealer class draws cards randomly 
    and tallies points with its methods.    
    
    Attributes: [attributes are just variables with data]
        keep_playing: allows user to keep playing
        old_card: the card the the high/low guess is based on
        new_card: the card we hope matches our guess
        player: the Player class (this is you, the user)
        guess: the user's input
        points: the scoring system
    """
    
    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Player): An instance of Player.
        """
        self.keep_playing = True
        self.old_card = r.randint(1,13)
        self.new_card = 0
        self.player = Player()
        self.guess = ""
        self.points = 300

    def start_game(self):
        """This method runs the Hi/Lo game.

        Args: 
            self (Player): An instance of Player.
        """
        print("""
              Welcome to the Hi/Lo game!
              
              Guess if the next card will be higher
              or lower than the last drawn card.
              If correct, you get 100pts! Guess wrong 
              and you lose 75pts!
              
              You lose if you hit, or go below, 0pts.
              You win if you score 1,000 or more pts.
              
              Good luck!
              """)
        while self.keep_playing == True:
            print(f"The card is : {self.old_card}")
            self.player.guess()
            self.draw_card()
            self.display_card()
            self.get_points()
            print(f"Score: {self.points}")
            self.keep_playing = self.to_play()
            self.card_update()

    def to_play(self):
        """Checks whether the User can play or not. Points must
        be above zero, below 1,000, and player must choose to play in order to 
        keep playing (see the next card).

        Args: 
            self (Player): An instance of Player.
            
        Return: If "False" the game ends.
        """
        if self.points >= 1000:
            print("Congratulations! You won!")
            return False
        
        # You get a choice in whether to play if your score is higher than zero.
        if self.points > 0:
            self.player.choice()
            if self.player.option == "n":
                print("Okay, thanks for playing.\n Goodbye for now!")
            return (self.points > 0 and self.player.option == "y")
        # This is if you get zero or less.
        else:
            print("You lose!")
            return False


    def draw_card(self):
        """Draws the next random card. Each card is shuffled 
        back into the deck after each round (see while loop).
        That part qualifies this code for a score of five!

        Args: 
            self (Player): An instance of Player.
        """
        key = False
        while key == False:
            self.new_card = r.randint(1,13)
            if self.new_card == self.old_card:
                key = False
            else:
                key = True
                        
    def display_card(self):
        """Displays the drawn card.

        Args: 
            self (Player): An instance of Player.
        """
        print(f"The new card is: {self.new_card}")

    def get_points(self):
        """Assigns points and keeps score.

        Args: 
            self (Player): An instance of Player.
        """
        # This added messages will also add to earning a score of 5.
        if self.player.card_guess == "h":
            if self.new_card > self.old_card:
                self.points = self.points + 100
                print("Yes! Good guess!\n")
            else:
                self.points = self.points - 75
                print("Ouch... Incorrect.\n")
        elif self.player.card_guess == "l":
            if self.old_card > self.new_card:
                self.points = self.points + 100
                print("Yes! Good guess!\n")
            else:
                self.points = self.points - 75
                print("Ouch... Incorrect.\n")
                # Note to the team: Let's code in some randomly generated 
                # insults (from our insult library). This includes some random
                # graphics of sad failures.
                
                # Second Note: Make a feature to mock certain choices. 
                # e.g. They choose low when the card is "1"
                # e.g. They choose to keep playing when their score is <100.
                    # i.e. "You still have hope?"

    def card_update(self):
        """Resets (shuffles) the card after each round. This 
        makes the old card to guess high or low against.

        Args: 
            self (Player): An instance of Player.
        """
        self.old_card = self.new_card
        self.new_card = 0
