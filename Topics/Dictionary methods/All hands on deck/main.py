# cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
#          "10": 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
# sum_hand = 0
# my_cards = [input() for i in range(6)]
# for i in my_cards:
#     sum_hand += cards[i]
#
#
# average = sum_hand / 6
# print(average)

def average_card():
    card_values = {}
    hand_value = 0
    for i in range(2, 11):
        card_values[str(i)] = i
    card_values.update({"Jack": 11, "Queen": 12, "King": 13, "Ace": 14})

    hand = [input(), input(), input(), input(), input(), input()]

    for card in hand:
        hand_value += card_values[card]

    return hand_value / 6

print(average_card())