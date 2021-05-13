from game.player import Player
import random as r
class Dealer():

    def __init__(self):
        self.keep_playing = True
        self.old_card = r.randint(1,13)
        self.new_card = 0
        self.player = Player()
        self.guess = ""
        self.points = 300

    def start_game(self):
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
        if self.points > 0:
            self.player.choice()
            return (self.points > 0 and self.player.option == "y")
        else:
            return False


    def draw_card(self):
        self.new_card = r.randint(1,13)

    def display_card(self):
        print(f"The new card is: {self.new_card}")

    def get_points(self):
        if self.player.card_guess == "h":
            if self.new_card > self.old_card:
                self.points = self.points + 100
            else:
                self.points = self.points - 75
        elif self.player.card_guess == "l":
            if self.old_card > self.new_card:
                self.points = self.points + 100
            else:
                self.points = self.points - 75

    def card_update(self):
        self.old_card = self.new_card
        self.new_card = 0
