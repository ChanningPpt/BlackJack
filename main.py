# Create deck of cards
# Shuffle deck of cards
# Deal cards
# Ask player to hit or stand
# Draw card(s) for dealer
# Decide winner

import random

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck = []

for suit in suits:
    for rank in ranks:
        deck.append(f'{rank} of {suit}')

random.shuffle(deck)

def dealCards(deck, hand):
    card = deck.pop()
    hand.append(card)

def calculateHandValue(hand):
    value = 0
    has_ace = False

    for card in hand:
        rank = card.split()[0]

        if rank.isdigit():
            value += int(rank)
        elif rank in ['Jack', 'Queen', 'King']:
            value += 10
        elif rank == 'Ace':
            has_ace = True
            value += 11

    if has_ace and value > 21:
        value -= 10
    return value

playerHand = []
dealerHand = []

dealCards(deck, playerHand)
dealCards(deck, playerHand)
dealCards(deck, dealerHand)
dealCards(deck, dealerHand)

while True:
    print(f'Player hand: {playerHand} ({calculateHandValue(playerHand)})')
    print(f'Dealer hand: [{dealerHand[0]}, <face down>]')

    if calculateHandValue(playerHand) > 21:
        print('Player busts!')
        break

    action = input('Do you want to hit or stand? ').lower()
    if action == 'hit':
        dealCards(deck, playerHand)
    elif action == 'stand':
        break
    else:
        print('Invalid action. Please try again.')
        continue

print(f'Player hand: {playerHand} ({calculateHandValue(playerHand)})')
print(f'Dealer hand: {dealerHand} ({calculateHandValue(dealerHand)})')

if calculateHandValue(playerHand) > 21:
    print('Player busts!')
elif calculateHandValue(dealerHand) > 21:
    print('Dealer busts! Player wins!')
elif calculateHandValue(playerHand) > calculateHandValue(dealerHand):
    print('Player wins!')
elif calculateHandValue(playerHand) < calculateHandValue(dealerHand):
    print('Dealer wins!')
else:
    print('Push!')