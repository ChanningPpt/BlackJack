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

playerChips = 100

while True:
    print(f'You have {playerChips} chips.')
    bet = int(input('Place your bet: '))

    if bet > playerChips:
        print("You don't have enough chips!")
        continue

    playerChips -= bet

    playerHand.clear()
    dealerHand.clear()

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
        print('Dealer wins!')
    elif calculateHandValue(dealerHand) > 21:
        print('Player wins!')
        playerChips += 2 * bet
    elif calculateHandValue(playerHand) > calculateHandValue(dealerHand):
        print('Player wins!')
        playerChips += 2 * bet
    elif calculateHandValue(playerHand) < calculateHandValue(dealerHand):
        print('Dealer wins!')
    else:
        print('Push!')
        playerChips += bet

    if playerChips == 0:
        print("You've run out of chips! Game over!")
        break

    playAgain = input('Do you want to play again? (yes/no) ').lower()
    if playAgain != 'yes':
        break