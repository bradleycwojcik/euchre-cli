
from random import shuffle
from euchrecli.card_util import Suit, Face, Card
from euchrecli.player_util import Player


def create_deck() -> [Card]:
    suits = [
        Suit('Spade', 'Black'),
        Suit('Club', 'Black'),
        Suit('Diamond', 'Red'),
        Suit('Heart', 'Red')
    ]
    faces = [
        Face('Nine', 9),
        Face('Ten', 10),
        Face('Jack', 11),
        Face('Queen', 12),
        Face('King', 13),
        Face('Ace', 14)
    ]

    deck = []
    for suit in suits:
        for face in faces:
            card = Card(suit, face)
            deck.append(card)

    shuffle(deck)
    return deck

def deal_hand(players: [Player], deck: [Card]) -> None:
    index = 0
    for player in players:
        for _ in range(5):
            player.hand.append(deck[index])
            deck.pop(index)