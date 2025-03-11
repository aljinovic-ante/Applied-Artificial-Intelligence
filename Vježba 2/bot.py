import random
from player import Player

class Bot(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def action(self,state):
        hand=state["hand"]
        table=state["table"]
        played_cards=state["played_cards"]
        print("Cards in hand: ", hand)
        print("Cards on table: ", table)
        print("Cards first elem on table: ", table[0][0])
        print("Already played cards: ", played_cards)
        ##
        # U svakoj rundi jedan od igrača baca kartu, a drugi odgovara sa svojom kartom. 
        # Ruku dobiva igrač čiji broj karte dijeli broj karte drugog igrača (npr. 3 pobjeđuje 6 ili 9).
        # Ako nijedna karta ne dijeli drugu tada igrač koji je igrao prvi dobiva ruku. 
        # Ako obje karte dijele jedna drugu (odnosno jednake su), drugi igrač dobiva ruku.
        print("HUMAN CARD: ",table[0])
        sorted_bot_hand=sorted(hand,key=lambda x: x[0],reverse=True)
        print("hand obicni ",hand)
        print("sortirano ",sorted_bot_hand)
        for card in sorted_bot_hand:
            if table[0][0] in {11,12,13}:
                if table[0][0]%card[0]==0:
                    print("STA VRACAN: ",self.hand.index(card))
                    return self.hand.index(card)
        
        ##
        rand_num=random.randint(0, 4)
        return rand_num
