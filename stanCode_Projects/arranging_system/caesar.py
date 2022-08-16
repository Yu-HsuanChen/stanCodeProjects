"""
File: caesar.py
Name:Joanne
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program can decipher the string which consists of the
    shifted ALPHABET that is produced by the number input.
    """
    number = int(input("Secret number: "))
    string = input("What's the ciphered string?")
    string = string.upper()
    # for case-insensitive
    answer = decipher(number, string, ALPHABET)
    print("The deciphered string is: "+str(answer))


def decipher(a, b, c):
    """
    :param a:the number to produce shifted ALPHABET
    :param b:the ciphered string
    :param c:the original sequence of ALPHABET
    :return:the deciphered string
    """
    new_alphabet = ''
    new_alphabet += c[25 - a + 1:]
    new_alphabet += c[:25 - a]
    # the shifted ALPHABET
    ans = ''
    for i in range(len(b)):
        ch = b[i]
        if ch.isalpha():
            code = new_alphabet.find(ch)
            ans += c[code]
        else:
            ans += ch
        # make sure of only deciphering the alphabet
    return ans


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
