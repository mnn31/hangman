



def pick_word():

    word = 'manan'
    return word






def play(orig):
    lives = 10
    cur = ['?'] * len(orig)
    li_orig = list(orig)
    while (lives != 0 and cur != li_orig):
        print(cur)
        guess = input('Guess a letter: ')
        if guess in orig:
            for i in range(len(orig)):
                if orig[i] == guess:
                    cur[i] = guess

        else:
            lives -= 1
            print('Wrong guess. You have', lives, 'lives left')

    print('Game over')

        

    






## MAIN PROGRAM ##
orig = pick_word()
play(orig)





