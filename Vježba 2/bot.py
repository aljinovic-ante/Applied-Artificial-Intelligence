import random
from player import Player

class Bot(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def action(self,state):
        hand=state["hand"]
        table=state["table"]
        played_cards=state["played_cards"]
        #print("Cards in hand: ", hand)
        #print("Cards on table: ", table)
        #print("Cards first elem on table: ", table[0][0])
        #print("Already played cards: ", played_cards)

        #print("HUMAN CARD: ",table[0])
        sorted_bot_hand=sorted(hand,key=lambda x: x[0],reverse=True)
        #print("hand: ",hand)
        #print("sorted: ",sorted_bot_hand)

        bot_valuable_cards = {1, 11, 12, 13}
        bot_has_valuable = any(card[0] in bot_valuable_cards for card in hand)
        
        valuable_for_12 = {2, 3, 4, 6}

        if not table:
            for card in reversed(sorted_bot_hand):
                if card[0] not in bot_valuable_cards:
                    return self.hand.index(card)
            return self.hand.index(sorted_bot_hand[-1])

        for card in sorted_bot_hand:
            if table[0][0] == 12 and card[0] in valuable_for_12:
                return self.hand.index(card)
            if table[0][0] == 12 and card[0]==1:
                return self.hand.index(card)
            if table[0][0] == 11 and card[0] in {1, 11}:
                return self.hand.index(card)
            if table[0][0] == 13 and card[0] in {1, 13}:
                return self.hand.index(card)
            if table[0][0] % card[0] == 0 and card[0] != 1:
                return self.hand.index(card)

        if bot_has_valuable:
            for card in reversed(sorted_bot_hand):
                if card[0] not in bot_valuable_cards:
                    return self.hand.index(card)
        
        return self.hand.index(sorted_bot_hand[-1])

