from game.player import Player
import random as r
class Dealer():

    def init(self):
        self.keep_playing = True
        self.old_card = r.randint(1,13)
        self.new_card = 0
        self.player = Player()

    def start_game(self):
        while self.keep_playing == True:
            print(f"The card is : {self.old_card}")
            self.player.guess()
            self.draw_card()
            self.display_card()
            self.player.get_points()
            self.player.choice()

    def to_play(self):
        return (self.points > 0 and self.option == "y")

    def draw_card(self):
        self.new_card = r.randint(1,13)

    def display_card(self):
        pass

    def ask_guess(self):
        pass

    def game(self):
        pass

