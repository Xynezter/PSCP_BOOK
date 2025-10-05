"""l"""
card = input().upper()
FRIST = {
    "A": "Ace", "J": "Jack", "Q": "Queen", "K": "King",
    "2": "2", "3": "3", "4": "4", "5": "5",
    "6": "6", "7": "7", "8": "8", "9": "9", "10": "10"
}
LAST = {
    "D": "Diamonds",
    "H": "Hearts",
    "S": "Spades",
    "C": "Clubs"
}
if card.startswith("10"):
    RANK_VALUE = "10"
    suit = card[2]
else:
    RANK_VALUE = card[0]
    suit = card[1]
print(FRIST[RANK_VALUE] + " of " + LAST[suit])
