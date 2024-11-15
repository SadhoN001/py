# polymorphism------------------------------------------->
class Player: #abastrac class
    def __init__(self,country):
        self.country=country
    def play(self):
        print(f"LOVE {self.country} Country")
        
class Footballplayer(Player):
    def __init__(self,club,country):
        self.club=club
        super().__init__(country)
    def play(self):
        print(f"i love {self.club} club and country {self.country}")
        
        
class Cricketplayer(Player):
    def __init__(self,studium):
        self.studium=studium
    def play(self):
        print(f"i love {self.studium} stadium")
        
x=Player("Argentina")
x.play()
a=Footballplayer("PSG","France")
a.play()
# b=Cricketplayer("Sagorika")# kaj baki ase error cmt it
# b.play()