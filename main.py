import hashlib
import random
import sqlite3
import uuid

from card_deck import get_cards

connection = sqlite3.connect("tutorial.db")
cursor = connection.cursor()

h = hashlib.sha256()

cid = uuid.uuid4().hex


def rand(r_hex="", amount=1_000_000):
    for i in range(amount):
        seed = r_hex or uuid.uuid4().hex
        random.seed(seed)
        cards = get_cards()
        random_cards = random.sample(cards, len(cards))

        str_cards = ", ".join([str(card.value) + "_" + card.suit for card in random_cards])

        h.update(str_cards.encode('utf-8'))
        hr = h.hexdigest()
        if r_hex:
            print(hr)
        cursor.execute(f"""INSERT INTO data (ID, HEX, CARDS) VALUES ('{hr}', '{seed}', '{str_cards}')""")


# rand("50cd11afee054daaacbd557ebee98692", 1)
rand()

r = cursor.execute("""SELECT count(*) FROM data""")

c = r.fetchall()[0]

print(c)

connection.commit()
connection.close()
