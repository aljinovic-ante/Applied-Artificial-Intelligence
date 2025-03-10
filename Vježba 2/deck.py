import random

class Deck:
    def __init__(self):
        self.suits=["clubs","diamonds","hearts","spades"]
        self.ranks=[1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.deck=[]
        for rank in self.ranks:
            for suit in self.suits:
                self.deck.append((rank,suit))

    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        return self.deal_five(),self.deal_five()
    
    def print(self):
        for card in self.deck:
            print(card)
    
    def deal_five(self):
        if len(self.deck) < 5:
            raise ValueError("Not enough cards left in deck!")
        five_cards = self.deck[:5]
        self.deck = self.deck[5:]
        return five_cards

    def take_one(self):
        if len(self.deck) < 1:
            raise ValueError("Not enough cards left in deck!")
        return self.deck.pop(0)

    def remove(self,card):
        self.deck.remove(card)

deck=Deck()
print(deck.shuffle())
deck.print()
a,b=deck.deal()

print(a,b)
print("hello")