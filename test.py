import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards."""
    # Check for a blackjack (Ace + 10-value card) and return 0 instead of the actual score
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Check for an Ace and convert it from 11 to 1 if the score exceeds 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    """Compares the final scores of the user and the computer and determines the result of the game."""
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose!"

    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Computer has Blackjack. You lose!"
    elif user_score == 0:
        return "You have Blackjack. You win!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Blackjack!")
    results = []

    while True:
        # Deal initial cards
        user_cards = []
        computer_cards = []
        is_game_over = False

        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        while not is_game_over:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)

            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            # Check for a blackjack, user score of 0, or computer score less than 17
            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over = True
            else:
                should_continue = input("Type 'y' to get another card, or 'n' to pass: ")

                if should_continue == 'y':
                    user_cards.append(deal_card())
                else:
                    is_game_over = True

        # Deal computer's cards
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        result = compare(user_score, computer_score)
        print(result)
        results.append(result)

        print("Game Results:")
        for index, result in enumerate(results):
            print(f"Game {index + 1}: {result}")

        play_again = input("Do you want to play again? Type 'y' or 'n': ")
        if play_again != 'y':
            break

# Start the game
play_game()
