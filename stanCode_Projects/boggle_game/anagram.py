"""
File: anagram.py
Name: Joanne
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    while True:
        s = input('Find anagrams for: ')
        start = time.time()
        if s == EXIT:
            break
        else:
            lst = find_anagrams(s)
            print(str(len(lst))+' anagrams: '+str(lst))
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    with open('dictionary.txt', 'r') as f:
        lst = []
        for line in f:
            word = line.strip()
            lst.append(word)
    return lst


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    dic = read_dictionary()
    lst = find_anagrams_helper(s, '', len(s), [], dic)

    return lst


def find_anagrams_helper(s, current_str, answer_len, lst, dic):
    if len(current_str) == answer_len and current_str not in lst and current_str in dic:
        print("Searching...")
        lst.append(current_str)
        print(current_str)
    else:
        for i in range(len(s)):
            a = s[i]
            current_str += a
            new_str = s[:i] + s[i+1:]
            if len(current_str) == 1 or has_prefix(current_str, dic):
                find_anagrams_helper(new_str, current_str, answer_len, lst, dic)
            current_str = current_str[:-1]
    return lst


def has_prefix(sub_s, dic):
    """
    :param sub_s:
    :return:
    """
    for word in dic:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
