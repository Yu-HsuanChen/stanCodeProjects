"""
File: boggle.py
Name: Joanne
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	lst = []
	for i in range(4):
		target = ''
		x = input(str(i+1)+' row of letters: ')
		x = x.lower()
		if len(x) != 7:
			print('Illegal input')
			break
		else:
			for ele in x:
				if ele != ' ':
					target += ele
			lst.append(target)
	start = time.time()
	find_anagrams(lst)
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open('dictionary.txt', 'r') as f:
		lst = []
		for line in f:
			word = line.strip()
			lst.append(word)
	return lst


def has_prefix(sub_s, dic):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dic:
		if word.startswith(sub_s):
			return True
	return False


def find_anagrams(lst):
	dic = read_dictionary()
	ans_lst = []
	for i in range(4):
		for j in range(4):
			cur_str = ''
			used_lst = []
			chr = lst[i][j]
			cur_str += chr
			used_lst.append((i, j))
			find_anagrams_helper(lst, cur_str, dic, i, j, ans_lst, used_lst)
	print("There are "+str(len(ans_lst))+' words in total.')


def find_anagrams_helper(lst, cur_str, dic, x, y, ans_lst, used_lst):
	if cur_str in dic and len(cur_str) >= 4 and cur_str not in ans_lst:
		print('Found \"'+str(cur_str)+'\"')
		ans_lst.append(cur_str)
	else:
		for i in range(-1, 2):
			for j in range(-1, 2):
				if 0 <= (x+i) < 4 and 0 <= (y+j) < 4 and (i, j) != (0, 0) and (x+i, y+j) not in used_lst:
					chr1 = lst[x+i][y+j]
					cur_str += chr1
					used_lst.append((x+i, y+j))
					if has_prefix(cur_str, dic):
						find_anagrams_helper(lst, cur_str, dic, x+i, y+j, ans_lst, used_lst)
						if has_prefix(cur_str, dic):
							find_anagrams_helper(lst, cur_str, dic, x + i, y + j, ans_lst, used_lst)
					cur_str = cur_str[:-1]
					used_lst.pop()


if __name__ == '__main__':
	main()
