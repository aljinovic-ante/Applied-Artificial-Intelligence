from itertools import count
from bot import Bot
from human import Human
from deck import Deck

class Game:
    def __init__(self,deck,player_one,player_two):
        self.deck=deck
        self.player_one=player_one
        self.player_two=player_two
    
    def __repr__(self):
        print(count(self.deck))