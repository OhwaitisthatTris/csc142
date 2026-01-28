import random

# Move a card from deck to hand
def draw_card(hand, deck):
    hand.append(deck.pop())  # take last card from deck

# Calculate the value of a hand
def calculate_hand(hand):
    value = 0
    aces = 0

    for card in hand:
        if card in ["J", "Q", "K"]:
            value += 10
        elif card == "A":
            value += 11
            aces += 1
        else:
            value += int(card)

    # Adjust Aces if needed
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1

    return value

def main():
    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    random.shuffle(deck)

    player_hand = []
    dealer_hand = []

    # Initial deal
    draw_card(player_hand, deck)
    draw_card(player_hand, deck)
    draw_card(dealer_hand, deck)
    draw_card(dealer_hand, deck)

    print("Your hand:", player_hand, "Value:", calculate_hand(player_hand))
    print("Dealer shows:", dealer_hand[0])

    # Player turn
    while calculate_hand(player_hand) < 21:
        action = input("Hit or Stand? (h/s): ").lower()
        if action == "h":
            draw_card(player_hand, deck)
            print("You drew:", player_hand[-1])
            print("Your hand:", player_hand, "Value:", calculate_hand(player_hand))
        else:
            break

    # Dealer turn
    while calculate_hand(dealer_hand) < 17:
        draw_card(dealer_hand, deck)

    print("Dealer's hand:", dealer_hand, "Value:", calculate_hand(dealer_hand))

    # Determine winner
    player_value = calculate_hand(player_hand)
    dealer_value = calculate_hand(dealer_hand)

    if player_value > 21:
        print("You bust! Dealer wins.")
    elif dealer_value > 21:
        print("Dealer busts! You win.")
    elif player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins.")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
