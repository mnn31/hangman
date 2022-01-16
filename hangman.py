
import random


DEBUG = False
WORDS_FILENAME = "words.txt"

def pick_word(wli):
    word = random.choice(wli).lower().strip()
    return word


def read_word_list(word_filename):
    wordfile = open(word_filename, mode='r')
    # read
    wordlist = wordfile.readlines()

    wordfile.close()
    return wordlist


def play(orig):
    lives = 10
    cur = ['?'] * len(orig)
    print(cur)
    li_orig = list(orig)
    while (lives != 0 and cur != li_orig):
        guess = input('Guess a letter: ')[0]
        if guess in orig:
            for i in range(len(orig)):
                if orig[i] == guess:
                    cur[i] = guess
            print(cur)

        else:
            lives -= 1
            print('Wrong guess. You have', lives, 'lives left')

    print('Game over')

        



## MAIN PROGRAM ##
wli = read_word_list(WORDS_FILENAME)
orig = pick_word(wli)
if DEBUG:
    print("Picked word is", orig)

play(orig)





