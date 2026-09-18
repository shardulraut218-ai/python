
import random

print("WELCOME TO THE GAME !!!")
def play_game():
    words = ["Giraffe", "Linux", "Unix", "Ubuntu", "Wireshark"]
    secret_word = random.choice(words).lower() 
    
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    print("--- Game Started! ---") 

    while guess != secret_word and not(out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Guess the word: ").lower() 
            guess_count += 1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print("Out of Guesses, You Lose !!!")
        print(f"The secret word was: {secret_word}")
    else:
        print("You win!")


if __name__ == "__main__":
    
    while True :
        play_game()
    
        play_again = input("\nDo you want to play again (y/n)")
        if play_again != 'y' :
            print("Thanks For playing! Goodbye.")
            break
