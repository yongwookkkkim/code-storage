import random

class player():
    def __init__(self, capital=5000, hand=[]):
        self.capital=capital
        self.hand=hand

class card():
    def __init__(self, suit, number):
        self.suit=suit
        self.number=number

deck = []
suits=["spade","clover","heart","diamond"]
numbers=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
for suit in suits:
    for number in numbers:
        deck.append(card(suit,number))