from game.player import player
import random as r
class dealer():

    def init(self):
        self.keep_playing = True
        self.old_card = r.randint(1,13)

    def start_game(self):
        pass

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
