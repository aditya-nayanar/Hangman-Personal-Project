import requests

def welcome_msg():
    ''' Welcome users to the game and check if user wants to play'''
    while True:
        startmsg = input("Welcome! Would you like to play Hangman? (Y/N)").lower()
        if startmsg not in ['y', 'n']:
            print("Please type Y to start playing or N to quit")
            continue
        elif startmsg in 'n':
            print("Goodbye!")
            quit()
        elif startmsg in 'y':
            break
def generate_word():
    '''Generate random word'''
    word = "https://random-word-api.herokuapp.com/word"
    response = requests.get(word)
    word = list(response.text)

    word.pop(0)
    word.pop(0)
    word.pop(-1)
    word.pop(-1)

    if response.ok:
        return "".join(word)
    else:
        print("Error: API not working")
        quit()

def play_round(word, lives):
    '''Start a round of hangman based on a given word and number of lives'''
    # print("\nDEBUGGING: Word to generated is", word)
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

        # Cheat code to show word to guess
        if guess == '%':
            print("\nWord to guess:", word)
            continue
        # Check if user wants to quit
        if guess == '#':
            quit()
        # Check if guess is not a letter or right sized word
        elif not len(guess) == 1 and not len(guess) == len(word):
            print("Your guess is not a letter or a word the same length, try again!")
            continue
        # Check if the guess is a word and matches word
        if len(guess) > 1:
            # Check if word has been guessed already
            if guess in prev_guesses_word:
                print("You have already guessed this word, try again!")
                continue
            # Check if correct word
            if guess in word:
                print("\nWell done! The word was:", word)
                break
            print("Your guess is incorrect")
            prev_guesses_word.append(guess)
            lives -= 1
            continue
        # If not word, check if letter has been guessed already
        if guess in prev_guesses_letter:
            print("You have already guessed this word, try again!")
            continue
        # Check if letter is in the word
        if guess in word:
            for i in range(len(word)):
                pass
                if guess in word[i]:
                    word_list[i] = guess
            # If only one letter remaining to guess, check if word is complete
            if '_' not in word_list:
                print("\nWell done! The word was:", word)
                break
            continue
        print("\'", guess, "\'", "is not not in the word")
        prev_guesses_letter.append(guess)
        lives -= 1


def main():

    # Welcome user
    welcome_msg()

    # Set lives
    lives = 8

    # Start playing
    while True:
        # Start one round
        print("Preparing word...")
        play_round(generate_word(), lives)

        # Once completed, check if user wants to keep playing
        retry = str(input("Would you like to play again? (Y/N)")).lower()
        if retry not in ['y', 'n']:
            print("Please type Y to retry or N to quit")
            continue
        elif retry in 'n':
            print("Goodbye!")
            quit()
        elif retry in 'y':
            continue

if __name__ == '__main__':
    main()