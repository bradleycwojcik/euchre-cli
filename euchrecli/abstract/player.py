
from random import choice, choices

from . import Team
from euchrecli.util.card_util import Card, Suit


class Player():

    def __init__(self, name: str, team: Team) -> None:
        self.name = name
        self.team = team

        # reset every hand
        self.is_dealer = False
        self.hand = []

        # reset every trick
        self.trick_winner = False

    def call_pick_up(self, face_up_card: Card, partner_is_dealer: bool) \
            -> bool:
        """Decide whether to call pick up of face up card or to pass.

        Returns:
            bool: whether or not to call pick up
        """
        pass

    def call_trump_suit(self, unsuitable: Suit) -> Suit:
        """Decide whether to call desired trump suit or to pass.

        Args:
            unsuitable (Suit): Trump suit cannot be this suit

        Returns:
            Suit: Called trump suit or unsuitable to pass
        """
        pass

    def pick_up_card(self, pick_up: Card) -> Card:
        """Choose whether or not to replace card in hand with picked up one.

        Args:
            pick_up (Card): Card to pick up.

        Returns:
            Card: Card to be discarded.
        """
        pass

    def play_card(self, played_cards: [Card], trump_suit: Suit) -> Card:
        pass

    def won_trick(self) -> None:
        self.trick_winner = True
        self.team.won_trick()

    def __repr__(self) -> str:
        return f"Player({self.name}, {self.team}, {self.is_dealer})"

    def __str__(self) -> str:
        if self.is_dealer:
            return f"{self.name} - dealer"
        else:
            return f"{self.name}"