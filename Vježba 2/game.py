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
        # print("Human pictured cards won:", count_p1)
        # print("Bot pictured cards won:", count_p2)
        if count_p1 > count_p2:
            return 1
        elif count_p1 < count_p2:
            return -1
        else:
            return 0
    
    def state(self, player):
        return {"hand": player.hand, "table": self.table, "played_cards": self.cards_played}
    
    def play(self,flag):
        self.game_deck.shuffle()
        self.player_one.hand = self.game_deck.deal_five()
        self.player_two.hand = self.game_deck.deal_five()
        last_winner = flag

        while self.game_deck.deck and self.player_one.hand and self.player_two.hand:
            if last_winner in {"p1", self.player_one}:
                current_player, other_player = (self.player_one, self.player_two)
            else:
                current_player, other_player = (self.player_two, self.player_one)

            current_card = current_player.hand.pop(current_player.action(self.state(current_player)))
            other_card = other_player.hand.pop(other_player.action(self.state(other_player)))
            self.table.extend([current_card, other_card])

            if current_card[0] % other_card[0] == 0:
                last_winner = other_player
            elif other_card[0] % current_card[0] == 0:
                last_winner = current_player
            else:
                last_winner = current_player

            last_winner.cards_won.append((current_card, other_card))
            current_player.hand.append(self.game_deck.take_one())
            other_player.hand.append(self.game_deck.take_one())
            self.cards_played.append((current_card, other_card))
            self.table.clear()
        
        result = self.result()
        if result == 1:
            print("Player One won!")
        elif result == -1:
            print("Player Two won!")
        else:
            print("Draw")
        return result