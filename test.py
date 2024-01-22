import random

from card_deck import get_cards


def test(seed):
    random.seed(seed)
    cards = get_cards()
    random_cards = random.sample(cards, len(cards))
    str_cards = ", ".join([str(card.value) + "_" + card.suit for card in random_cards])
    print(str_cards)


test("543d4e144ec540fb9d0cd9e6e86770ae")