"""
File: similarity.py
Name:Joanne
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program can find the most similar sequence
    in the long sequence to the short sequence.
    """
    long_sequence = input("Please give me a DNA sequence to search: ")
    long_sequence = long_sequence.upper()
    # for case-insensitive
    short_sequence = input("What DNA sequence would you like to match? ")
    short_sequence = short_sequence.upper()
    # for case-insensitive
    best_match = find_match(long_sequence, short_sequence)
    print("The best match is "+str(best_match))


def find_match(a, b):
    """
    :param a:the long one,the sequence to find the most similar sequence to b
    :param b:the short one,the target sequence to be compared with
    :return:the most similar sequence from a to b
    """
    if a.find(b) != -1:
        return b
    # if there is the same sequence as b in a
    else:
        base_a = a[:len(b)]
        # the first sequence which has the same size as b in a
        base = 0
        # the number of the same strand between base_a and b
        for i in range(len(b)):
            ch1 = base_a[i]
            ch2 = b[i]
            if ch1 == ch2:
                base += 1
            else:
                base += 0
        ans = base_a
    # to have the first data to be compared
        for j in range(len(a) - len(b)):
            # to compare the sequence from a one by one
            new_a = a[j + 1:j + len(b) + 1]
            # start from the second sequence which has the same size as b in a
            correct = 0
            # the number of the same strand between new_a and b
            for k in range(len(b)):
                ch3 = new_a[k]
                ch4 = b[k]
                if ch3 == ch4:
                    correct += 1
                else:
                    correct += 0
            if base < correct:
                base = correct
                ans = new_a
            # to compare which is more similar to b
        return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
