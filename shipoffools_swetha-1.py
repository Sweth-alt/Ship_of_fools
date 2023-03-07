import random
class Die:
    '''Class Die has two methods which are used to roll the dice and get their values'''

    def __init__(self):
        self._value=0

    def roll(self):
        '''roll method is used roll the dice and the values are stored in self._values'''
        self._value=random.randint(1,6) 
    def get_value(self):
        '''get_value method is used to get values after rolling'''
        self.roll()
        return self._value

class Dicecup:
    '''Dicecup handles 5 objects and banks and releases the dice individually'''

    def __init__(self):
        self._dices=[]
        for i in range(5):
            self._dices.append([Die(),0])
    def value(self, position):
        '''value method is used to take the value of dice based on its index'''
        return self._dices[position][0].get_value()
    def bank(self, position):
        '''def bank banks the dice of particular index'''
        self._dices[position][1]=1 
    def is_banked(self, position)->bool:
        '''def for cheking the banked die'''
        if self._dices[position][1]==1:
            return True
        else:
            return False
    def release(self, position):
        '''release  method used to release the banked one of particular index'''
        self._dices[position][1]=0
    def release_all(self):
        '''release_all  releases all banked dice'''
        for position in range(5):
            self._dices[position][1]=0
    def roll(self):
        '''roll method makes use of objects of Die class and gathers all the values from the roll method of Die class and stores  those values in list'''
        for i,die in enumerate(self._dices):
            if die[0]==0:
                self._dices[i][0].roll()  


class ShipOfFoolsGame:
    '''ShipOfFoolsGame class is the original implementation of the game which has a single method called round
       and responsible for the score of the player and also take the object of Diecups'''
    def __init__(self):
        self._cup=Dicecup()
        self._winning_score=21

    def round(self):
        '''def round plays 1st round and has 3 chances for 1st player'''
        has_ship = False
        has_captain = False
        has_crew = False
        cargo_score = 0
        self._cup.release_all()

        for turn in range(3):
            self._cup.roll()
            value=[self._cup._dices[i][0].get_value() for i in range(5)]
            die_unbanked=[]
            for i in range(5):
                if self._cup.is_banked(i):
                    die_unbanked.append("B")
                    value[i]=0
                else:
                    die_unbanked.append(value[i])
            print(die_unbanked)
            if not has_ship and (6 in value):
                self._cup.bank(value.index(6))
                print("Die",value.index(6)+1,"is banked for ship")
                has_ship = True        
            if has_ship and not has_captain and (5 in value):
                self._cup.bank(value.index(5))
                has_captain = True
                print("Die",value.index(5)+1,"is banked for captain")               
            if has_captain and not has_crew and (4 in value):
                self._cup.bank(value.index(4))
                has_crew = True
                print("Die",value.index(4)+1,"is banked for crew")          
            if has_captain and has_crew and has_ship:
                if turn<=1:
                    for mark in range(5):
                        if value[mark] > 3 and not self._cup.is_banked(mark):
                            self._cup.bank(mark)
                            print("Die",mark+1,"is banked with value",value[mark])
                            cargo_score=cargo_score+value[mark]                      
                if turn==2:
                    for mark in range(5):
                        if self._cup.is_banked(mark):
                            pass
                        else:
                            cargo_score = cargo_score+value[mark]
                            self._cup.bank(mark)
        if has_captain and has_crew and has_ship:
            for add in range(5):
                if not self._cup.is_banked(add):
                    cargo_score = cargo_score+value[add]
            print("Score of Cargo ",cargo_score)
        else:
            print("Score of Cargo ",cargo_score)      
        return cargo_score

class Player:
    '''player class represents the individual player and responsible for the score of the players and stores the score in the ._score attribute'''
    def __init__(self, name_of_player):
        self._name = self.set_name(name_of_player)
        self._score = 0
    
    def set_name(self, name):
        ''' set_name method is used to set the name the player'''
        return name

    def current_score(self):
        '''current_score method updates the score of the each player and stores the score in ._score attribute'''
        return self._score

    def reset_score(self):
        '''reset_score method resets the score of the player after completion of the each and every single round'''
        self._score = 0
    
    def play_round(self, begin):
        '''play_round method make use of ShipOfFoolsGame object and assigns the round method to the each player'''
        self._score=self._score+begin.round()
    
class PlayRoom:
    '''play_round method make use of ShipOfFoolsGame object and assigns the round method to the each player'''
    def __init__(self):
        self._game = ShipOfFoolsGame()
        self._players = []
    
    def add_player(self, profile):
        '''add_player method  used to add the players to the ._playersattribute'''
        self._players.append(profile)
    
    def reset_scores(self):
        '''reset_score method which resembles the functionality of the reset_score method in the Player class'''
        for restart in self._players:
            restart.reset_score()
    
    def play_round(self):
        '''this method is same as the player_round in Player Class but act upon on group of player'''
        for participant in self._players:
            print(">>>>>>>>>------",participant._name,"------<<<<<<<<<")
            participant.play_round(self._game)
    
    def game_finished(self):
        '''game_finished method checks the score of the each player weather they reached more than 21 or not'''
        for complete in self._players:
            if complete.current_score() > 22:
                return True
        return False

    def print_scores(self):
        '''print_score gives the current score of the each player'''
        for reward in self._players:
            print("The player",reward._name,"scored",reward.current_score())
    
    def print_winner(self):
        '''print_winner method checks the individual score and prints the winner'''
        i = 0
        for winner in self._players:
            if winner.current_score() > 22:
                i=i+1
        if i>1:
            print("\n\n>>>>>>>>>>>>>Its a Draw<<<<<<<<<<<<<<<")
        elif i == 1:
            for champ in self._players:
                if champ.current_score() >= 21:
                    print("\nThe Champion of the game is ",champ._name)

if __name__ == "__main__":
    room=PlayRoom()
    series = 1
    room.add_player(Player("Swetha"))
    room.add_player(Player("Priyanka"))
    room.reset_scores()
    
    while not room.game_finished():
        print("\n>>>>>>>>>>>>This is Round",series)
        room.play_round()
        room.print_scores()
        series =series + 1
    room.print_winner()
   
