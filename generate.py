import random

number=random.randint(1,10)
print(number)



cards=["jack","king","queen","ace"]
random.shuffle(cards)
for card in cards:
    print(card)