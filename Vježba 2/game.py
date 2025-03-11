from itertools import count
from deck import Deck


class Game:
    def __init__(self,player_one,player_two):
        self.game_deck=Deck()
        self.player_one=player_one
        self.player_two=player_two
        self.table=[]
        self.cards_played=[]
    
    def __repr__(self):
        print("Number of Cards in deck: ",len(self.game_deck.deck))
        print("Player one cards: ",self.player_one.hand)
        print("Player two cards: ",self.player_two.hand)

    def result(self):
        count_p1 = sum(sum(1 for card in pair if card[0] in {11, 12, 13}) for pair in self.player_one.cards_won)
        count_p2 = sum(sum(1 for card in pair if card[0] in {11, 12, 13}) for pair in self.player_two.cards_won)
        print("Human pictured cards won:", count_p1)
        print("Bot pictured cards won:", count_p2)
        if count_p1 > count_p2:
            return 1
        elif count_p1 < count_p2:
            return -1
        else:
            return 0
    
    def state(self, player):
        return {"hand": player.hand, "table": self.table, "played_cards": self.cards_played}
    
    def play(self):
        #print(self.game_deck.deck)
        self.game_deck.shuffle()
        #print(self.game_deck.deck)
        self.player_one.hand=self.game_deck.deal_five()
        self.player_two.hand=self.game_deck.deal_five()
        print("Number of Cards left in deck: ",len(self.game_deck.deck))
        while len(self.game_deck.deck)>0 and len(self.player_one.hand)>0 and len(self.player_two.hand)>0:
            last_winner=None
            if last_winner==None or last_winner==self.player_one:
                # prvi igra prvi igrac
                player_one_card_index=self.player_one.action(self.state(self.player_one))
                player_one_card=self.player_one.hand[player_one_card_index]
                self.player_one.hand.remove(player_one_card)
                print("Player One played: ",player_one_card)
                self.table.append(player_one_card)
                print("Table: ",self.table)
                player_two_card_index=self.player_two.action(self.state(self.player_two))
                print("Player Two hand: ",self.player_two.hand)

                player_two_card=self.player_two.hand[player_two_card_index]
                self.player_two.hand.remove(player_two_card)
                print("Player Two played: ",player_two_card)
                self.table.append(player_two_card)
                print("Table: ",self.table)
                self.cards_played

                # check if p2 divides p1 cards
                if(player_one_card[0]%player_two_card[0]==0):
                    last_winner=self.player_two
                    self.player_two.cards_won.append((player_one_card,player_two_card))
                    self.player_two.hand.append(self.game_deck.take_one())
                    self.player_one.hand.append(self.game_deck.take_one())

                # check if p1 divides p2 cards
                elif(player_two_card[0]%player_one_card[0]==0):
                    last_winner=self.player_one
                    self.player_one.cards_won.append((player_one_card,player_two_card))
                    self.player_one.hand.append(self.game_deck.take_one())
                    self.player_two.hand.append(self.game_deck.take_one())
                
                else:
                    last_winner=self.player_one
                    self.player_one.cards_won.append((player_one_card,player_two_card))
                    self.player_one.hand.append(self.game_deck.take_one())
                    self.player_two.hand.append(self.game_deck.take_one())

                self.cards_played.append((player_one_card,player_two_card))
                self.table=[]

            else:
                # prvi igra drugi igrac
                player_two_card_index=self.player_two.action(self.state(self.player_two))
                player_two_card=self.player_two.hand[player_two_card_index]
                self.player_two.hand.remove(player_two_card)
                print("Player Two played: ",player_two_card)
                self.table.append(player_two_card)
                print("Table: ",self.table)
                player_one_card_index=self.player_one.action(self.state(self.player_one))
                player_one_card=self.player_one.hand[player_one_card_index]
                player_one_card_index=self.player_one.action(self.state(self.player_one))
                player_one_card=self.player_one.hand[player_one_card_index]
                self.player_one.hand.remove(player_one_card)
                print("Player One played: ",player_one_card)
                self.table.append(player_one_card)
                print("Table: ",self.table)

                # check if p2 divides p1 cards
                if(player_one_card[0]%player_two_card[0]==0):
                    last_winner=self.player_two
                    self.player_two.cards_won.append((player_one_card,player_two_card))
                    self.player_two.hand.append(self.game_deck.take_one())
                    self.player_one.hand.append(self.game_deck.take_one())

                # check if p1 divides p2 cards
                elif(player_two_card[0]%player_one_card[0]==0):
                    last_winner=self.player_one
                    self.player_one.cards_won.append((player_one_card,player_two_card))
                    self.player_one.hand.append(self.game_deck.take_one())
                    self.player_two.hand.append(self.game_deck.take_one())
                
                else:
                    last_winner=self.player_two
                    self.player_two.cards_won.append((player_one_card,player_two_card))
                    self.player_two.hand.append(self.game_deck.take_one())
                    self.player_one.hand.append(self.game_deck.take_one())

                self.cards_played.append((player_one_card,player_two_card))
                self.table=[]
            
        result=self.result()
        if(result==1):
            print("Player One won!")
        if(result==-1):
            print("Player Two won!")
        if(result==0):
            print("Draw")

            