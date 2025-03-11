import random

class Player:
    def __init__(self,name):
        self.name=name
        self.hand=[]
        self.cards_won=[]

    def action(self,state):
        hand=state["hand"]
        table=state["table"]
        played_cards=state["played_cards"]
        print("Cards in hand: ", hand)
        print("Cards on table: ", table)
        print("Already played cards: ", played_cards)
        ###
        # for card in hand:
        #     if card%table[0][0]==0:
        #         card
        #         return self.hand.
            
        ###
        rand_num=random.randint(0, 4)
        return rand_num

        
