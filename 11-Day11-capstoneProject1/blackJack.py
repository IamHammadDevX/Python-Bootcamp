import random

def dealCard():
    """Generate random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calcScore(cards):
    """Calculate the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(userScore, compScore):
    if userScore == compScore:
        return "Draw 🙃"
    elif compScore == 0:
        return "Lose, opponent has Blackjack 😱"
    elif userScore == 0:
        return "Win with a Blackjack 😎"
    elif userScore > 21:
        return "You went over. You lose 😭"
    elif compScore > 21:
        return "Opponent went over. You win 😁"
    elif userScore > compScore:
        return "You win 😃"
    else:
        return "You lose 😤"

userCards = []
computerCards = []
isGameOver = False

# Initial deal
for _ in range(2):
    userCards.append(dealCard())
    computerCards.append(dealCard())

while not isGameOver:
    userScore = calcScore(userCards)
    compScore = calcScore(computerCards)
    print(f"Your cards: {userCards}, current score: {userScore}")
    print(f"Computer's first card: {computerCards[0]}")

    if userScore == 0 or compScore == 0 or userScore > 21:
        isGameOver = True
    else:
        userShouldDeal = input("Type 'y' to get another card, type 'n' to pass: ")
        if userShouldDeal == "y":
            userCards.append(dealCard())
        else:
            isGameOver = True

# Computer's turn
while compScore != 0 and compScore < 17:
    computerCards.append(dealCard())
    compScore = calcScore(computerCards)

print(f"Your final hand: {userCards}, final score: {userScore}")
print(f"Computer's final hand: {computerCards}, final score: {compScore}")
print(compare(userScore, compScore))
