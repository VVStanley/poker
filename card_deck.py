import random
import uuid
from typing import List, Optional

face_cards = {11: "J", 12: "Q", 13: "K", 14: "A", }


class Card:
    def __init__(self, value, suit, denomination):
        self.suit = suit
        self.value = value
        self.denomination = denomination

    def __str__(self):
        return f"{self.value} {self.suit}"

    def __repr__(self):
        return self.__str__()


class User:
    def __init__(self, index):
        self.index = index
        self.hand: List[Card] = []

    def add_card(self, card: Card):
        self.hand.append(card)

    def __str__(self):
        return f"User {self.index}; cards: " + ", ".join([str(card) for card in self.hand])

    def __repr__(self):
        return self.__str__()

    def check_cards(self, cards: List['Card']):
        return sum([c.denomination for c in cards + self.hand])


class Game:

    def __init__(self, users_count: int, seed: str = "c6bcbdfd3ce0437ab8fd7445dbcc54a1"):
        self.seed = seed
        self.users = [User(i) for i in range(users_count)]
        self.cards_generator = get_random_cards(cards=get_cards(), seed=seed)
        self.flop = []
        self.tern = None
        self.river = None

        self.deal_cards()

    @property
    def _flop(self):
        return ", ".join([str(card) for card in self.flop])

    def _get_card(self):
        return next(self.cards_generator)

    def _get_cards(self):
        return self.flop + [self.tern] + [self.river]

    def _card_reset(self):
        next(self.cards_generator)

    def deal_cards(self):
        for _ in range(2):
            for user in self.users:
                user.add_card(self._get_card())

        self._card_reset()
        for _ in range(3):
            self.flop.append(self._get_card())

        self._card_reset()
        self.tern = self._get_card()

        self._card_reset()
        self.river = self._get_card()

    def stol(self) -> None:
        print(f"""
            {self.users[0]}
            
            
            cards: {self._flop}, {self.tern}, {self.river}
            
            
            {self.users[1]}
        
        """)


def get_cards():
    cards = []
    for value in list(range(2, 15)):
        # for suit in ["clubs", "diamond", "spades", "hearts"]:
        for suit in ["♠", "♦", "♣", "♥"]:
            if value in face_cards:
                card_value = face_cards[value]
                cards.append(Card(card_value, suit, value))
            else:
                cards.append(Card(value, suit, value))
    return cards


def get_random_cards(cards, seed=None):
    seed = seed or uuid.uuid4().hex
    random.seed(seed)
    cards = random.sample(cards, len(cards))
    for card in cards:
        yield card


def deal_cards(count_users: int):
    users = [User(i) for i in range(count_users)]
    cards_generator = get_random_cards(cards=get_cards())
    for _ in range(2):
        for user in users:
            user.add_card(next(cards_generator))
    return users, cards_generator
