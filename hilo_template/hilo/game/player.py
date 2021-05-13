from game.dealer import Dealer
class Player: # translates to 1's & 0's as it runs
                # translates
    def init(self):
        self.points = 300
        self.dealer = Dealer()

    def choice(self):
        self.option = input("Keep Playing y/n")

    def guess(self):
        guess = input("Higher or Lower? h/l")
        return guess
    
    def get_points(self):
        
        if self.dealer.win == True:
            self.points = self.points + 100
        else:
            self.points = self.points - 75
