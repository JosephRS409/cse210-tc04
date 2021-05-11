class player:
    def init(self):
        self.points = 300

    def choice(self):
        self.option = input("Keep Playing y/n")

    def guess(self):
        self.guess = input("Higher or Lower? h/l")

    def to_play(self):
        return (self.points > 0 and self.option =="y")
    
    def get_points(self):
        
        if dealer.self.win == True:
            self.points = self.points + 100
        else:
             self.points = self.ponts - 75
