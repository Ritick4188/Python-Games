import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " Of " + self.suit


class Deck():

    def __init__(self):

        self.all_card = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_card.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_card)

    def deal_one(self):
        return self.all_card.pop()


class Player():

    def __init__(self, name):
        self.name = name
        self.all_card = []

    def remove_card(self):
        return self.all_card.pop(0)

    def add_cards(self, new_card):
        if type(new_card) == type([]):
            self.all_card.extend(new_card)
        else:
            self.all_card.append(new_card)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_card)} cards.'


player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

round_num = 0

while game_on:
    round_num += 1
    print(f'Round {round_num}')

    if len(player_one.all_card) == 0:
        print('Player One, Out of The Card!')
        game_on = False
        break

    if len(player_two.all_card) == 0:
        print('Player Two, Out of The Card!')
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_card())

    player_two_cards = []
    player_two_cards.append(player_two.remove_card())

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        else:
            print('War!')

            if len(player_one.all_card) < 5:
                print('Player One Unable To Declare War')
                print("Player Two Win!")
                game_on = False
                break

            elif len(player_two.all_card) < 5:
                print('Player Two Unable To Declare War')
                print("Player One Win!")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())

