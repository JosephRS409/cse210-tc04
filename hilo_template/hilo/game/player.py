# from game.dealer import Dealer
class Player:
    def __init__(self):
        self.option = "y"
        self.keep_playing = True
        self.card_guess = ""

    def choice(self):
        self.option = input("Keep Playing y/n ")
        if self.option == "n":
            self.keep_playing = False

    def guess(self):
        self.card_guess = input("Higher or Lower? h/l ")

