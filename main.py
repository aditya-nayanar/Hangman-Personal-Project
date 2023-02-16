import requests

def generate_word():
    # word = "https://random-word-api.herokuapp.com/word"
    # response = requests.get(word)
    # word = list(response.text)
    #
    # word.pop(0)
    # word.pop(0)
    # word.pop(-1)
    # word.pop(-1)
    #
    # return "".join(word)
    return "testing"

def play_round(word, lives):
    print("\nDEBUGGING: Word to generated is", word)
    print("The word to guess has", len(word), "letters")
    print("Type \"#\" to quit at anytime")

    # Prepare lists for adding guesses and recording previous guesses
    word_list = []
    for x in range(len(word)):
        word_list.append('_')
    prev_guesses_letter = []
    prev_guesses_word = []

    # Start receiving guesses from user
    while True:
        # Check if there are remaining lives
        if lives == 0:
            print("\nYou have no lives remaining :(", "\nThe word was", word)
            break
        # Receive user guess
        print("")
        print("".join(word_list), "\nLives remaining:", lives)
        print("Previous incorrect letter guesses", prev_guesses_letter)
        print("Previous incorrect word guesses", prev_guesses_word)
        guess = str(input("Guess a letter or word: ")).lower().strip()

        # Check if user wants to quit
        if guess == '#':
            quit()
        # Check if guess is not a letter or right sized word
        elif not len(guess) == 1 and not len(guess) == len(word):
            print("Your guess is not a letter or a word the same length, try again!")
            continue
        # Check if letter or word has been guessed already
        elif guess in prev_guesses_letter or prev_guesses_word:
            print("You have already guessed this letter or word, try again!")
            continue
        # Check if the guess is a word and matches word
        if len(guess) > 1:
            if guess in word:
                print("Well done! The word was:", word)
                break
            print("You guess is incorrect")
            lives -= 1
            continue
        # Check if letter is in the word
        if guess in word:
            for i in range(len(word)):
                pass
                if guess in word[i]:
                    word_list[i] = guess
            continue
        print("\'", guess, "\'", "is not not in the word")
        lives -= 1


def main():

    # Welcome message and start menu for players
    # while True:
    #     startmsg = input("Welcome! Would you like to play Hangman? (Y/N)").lower()
    #     if startmsg not in ['y', 'n']:
    #         print("Please type Y to start playing or N to quit")
    #         continue
    #     elif startmsg in 'n':
    #         print("Goodbye!")
    #         quit()
    #     elif startmsg in 'y':
    #         print("The game has started")
    #         break

    # Generate word for player to guess
    word = generate_word()

    # Play a round
    play_round(word, 2)



    while True:
        retry = str(input("Would you like to play again? (Y/N)")).lower()
        if retry not in ['y', 'n']:
            print("Please type Y to retry or N to quit")
            continue
        elif retry in 'n':
            print("Goodbye!")
            quit()
        elif retry in 'y':
            break

    play_round(generate_word(), 2)






if __name__ == '__main__':
    main()