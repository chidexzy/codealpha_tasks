import random
import os

def clear_screen():
    # Clear the terminal screen for better display
    os.system('cls' if os.name == 'nt' else 'clear')

def get_word_list():
    # Return a list of words for the hangman game
    return ['python', 'programming', 'computer', 'keyboard', 'software']


def display_word_progress(word, guessed_letters):
    # Display the word with guessed letters revealed
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def display_game_state(word, guessed_letters, wrong_letters, attempts_left):
    # Display the complete game state
    clear_screen()
    print("=" * 50)
    print("            HANGMAN GAME")
    print("=" * 50)
    print(f"Word: {display_word_progress(word, guessed_letters)}")
    print(f"\nAttempts remaining: {attempts_left}")
    
    if guessed_letters:
        correct_guesses = [letter for letter in guessed_letters if letter in word]
        if correct_guesses:
            print(f"Correct letters: {', '.join(sorted(correct_guesses))}")
    
    if wrong_letters:
        print(f"Wrong letters: {', '.join(sorted(wrong_letters))}")
    
    print("-" * 50)

def get_player_guess(guessed_letters, wrong_letters):
    # Get and validate player's letter guess
    all_guessed = guessed_letters.union(wrong_letters)
    
    while True:
        try:
            guess = input("Enter a letter: ").lower().strip()
            
            # Validate input
            if not guess:
                print("Please enter a letter!")
                continue
            
            if len(guess) != 1:
                print("Please enter only one letter!")
                continue
            
            if not guess.isalpha():
                print("Please enter a valid letter!")
                continue
            
            if guess in all_guessed:
                print(f"You already guessed '{guess}'. Try a different letter!")
                continue
            
            return guess
            
        except KeyboardInterrupt:
            print("\n\nGame interrupted. Thanks for playing!")
            exit()
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

def check_win_condition(word, guessed_letters):
    # Check if the player has won the game
    return all(letter in guessed_letters for letter in word)

def play_hangman():
    # Game setup
    word_list = get_word_list()
    word = random.choice(word_list).lower()
    guessed_letters = set()
    wrong_letters = set()
    max_attempts = 6
    attempts_left = max_attempts
    
    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word.")
    print("Good luck!\n")
    input("Press Enter to start the game...")
    
    # Game loop
    while attempts_left > 0:
        # Display current game state
        display_game_state(word, guessed_letters, wrong_letters, attempts_left)
        
        # Check win condition
        if check_win_condition(word, guessed_letters):
            print(f"\n🎉 Congratulations! You won!")
            print(f"The word was: '{word.upper()}'")
            print(f"You guessed it with {attempts_left} attempts remaining!")
            return True
        
        # Get player guess
        guess = get_player_guess(guessed_letters, wrong_letters)
        
        # Process the guess
        if guess in word:
            guessed_letters.add(guess)
            print(f"\n✓ Good guess! '{guess}' is in the word.")
        else:
            wrong_letters.add(guess)
            attempts_left -= 1
            print(f"\n✗ Sorry, '{guess}' is not in the word.")
        
        # Brief pause to show feedback
        if attempts_left > 0:
            input("Press Enter to continue...")
    
    # Game over - player lost
    display_game_state(word, guessed_letters, wrong_letters, attempts_left)
    print(f"\n💀 Game Over! You ran out of attempts.")
    print(f"The word was: '{word.upper()}'")
    return False

def play_again():
    # Ask player if they want to play again
    while True:
        try:
            choice = input("\nWould you like to play again? (y/n): ").lower().strip()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")
        except KeyboardInterrupt:
            print("\n\nThanks for playing!")
            return False
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

def display_game_stats(games_played, games_won):
    # Display game statistics
    if games_played > 0:
        win_percentage = (games_won / games_played) * 100
        print(f"\n📊 Game Statistics:")
        print(f"Games played: {games_played}")
        print(f"Games won: {games_won}")
        print(f"Win percentage: {win_percentage:.1f}%")

def main():
    # Main function to run the game with replay functionality
    games_played = 0
    games_won = 0
    
    print("🎮 Welcome to the Enhanced Hangman Game! 🎮")
    print("=" * 50)
    
    try:
        while True:
            # Play a game
            won = play_hangman()
            games_played += 1
            
            if won:
                games_won += 1
            
            # Display statistics
            display_game_stats(games_played, games_won)
            
            # Ask if player wants to play again
            if not play_again():
                break
        
        # Final goodbye message
        clear_screen()
        print("=" * 50)
        print("           Thanks for playing!")
        print("=" * 50)
        display_game_stats(games_played, games_won)
        print("\nSee you next time! 👋")
        
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Thanks for playing!")

if __name__ == "__main__":
    main()
