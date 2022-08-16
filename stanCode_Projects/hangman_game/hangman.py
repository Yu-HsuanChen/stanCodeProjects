"""
File: hangman.py
Name:Joanne
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program produces the game that
    users have N_TURNS chances to guess the
    dashed word by inputting one alphabet at
    a time, and the chances only decrease when
    users make the wrong guess.
    """
    answer = random_word()
    hid_ans = dashed(answer)
    # the dashed word
    print("The word looks like: "+str(hid_ans))
    print("You have "+str(N_TURNS)+" guesses left.")
    steps = N_TURNS
    # the chances users have
    while steps >= 1:
        input_ch = input("Your guess: ")
        input_ch = input_ch.upper()
        # for case-insensitive
        if len(input_ch) > 1:
            print("illegal format.")
        # only input one alphabet at a time
        elif input_ch.isalpha():
            hid_ans = find_ans(answer, input_ch, hid_ans, steps)
            if hid_ans == answer:
                break
            # if users win the game can end the loop
            else:
                steps = new_step(answer, input_ch, steps)
                if steps == 0:
                    break
                # if users lose the game can end the loop
                else:
                    print("You have " + str(steps) + " guesses left.")
        else:
            print("illegal format.")
        # only input alphabet


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def dashed(answer):
    ans = ''
    for word in answer:
        if word.isalpha():
            ans += "-"
    return ans


def find_ans(a, b, c, d):
    """
    :param a:the answer of the dashed word
    :param b:the alphabet users input to guess if it appears in a
    :param c:the dashed word so far the users guess
    :param d:the chances left
    :return:the dashed word so far the users guess,includes b
    """
    if a.find(b) != -1:
        # make the right guess
        print("You are correct!")
        ans = ''
        for i in range(len(a)):
            ch = a[i]
            ch1 = c[i]
            if ch1.isalpha():
                ans += ch1
            # to show the right guess before
            elif b == ch:
                ans += b
            # to show the right guess
            else:
                ans += "-"
        if ans == a:
            print("You win!!\nThe word was: "+str(ans))
            # if users win the game
        else:
            print("The word looks like: " + str(ans))
        return ans
        # to reassign hid_ans
    elif a.find(b) == -1:
        # make the wrong guess
        print("There is no "+str(b)+"'s in the word.")
        if d == 1:
            print("You are completely hung : (\nThe word was: "+str(a))
            # if users lose the game
        else:
            print("The word looks like: " + str(c))
        return c


def new_step(a, b, c):
    """
    :param a:the answer of the dashed word
    :param b:the alphabet users input to guess if it appears in a
    :param c:the chances left
    :return:the chances left after this guess
    """
    if a.find(b) == -1:
        c -= 1
    return c
    # to reassign steps


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
