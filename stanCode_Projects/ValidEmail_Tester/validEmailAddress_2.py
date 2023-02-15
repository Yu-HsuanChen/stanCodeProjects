"""
File: validEmailAddress_2.py
Name: 
----------------------------
Please construct your own feature vectors
and try to surpass the accuracy achieved by
Jerry's feature vector in validEmailAddress.py.
feature1:  TODO: if there is no "@"
feature2:  TODO: if there is "." before "@"
feature3:  TODO: if there is text before "@"
feature4:  TODO: if there is text after "@"
feature5:  TODO: if the email start with alphabet
feature6:  TODO: if there is no alphabet before "@"
feature7:  TODO: if the first letter is an upper alphabet
feature8:  TODO: if there is '..' after "@"
feature9:  TODO: if ends with '.tw'
feature10: TODO: if the length of email is smaller than 13

Accuracy of your model: 0.8461538461538461
"""

WEIGHT = [                           # The weight vector selected by you
	[-0.7],                              # (Please fill in your own weights)
	[-0.2],
	[0.2],
	[0.2],
	[0.1],
	[-0.6],
	[-0.5],
	[-0.6],
	[0.1],
	[-0.7]
]

DATA_FILE = 'is_valid_email.txt'     # This is the file name to be processed


def main():
	maybe_email_list = read_in_data()
	ans_lst = []
	for maybe_email in maybe_email_list:
		feature_vector = feature_extractor(maybe_email)
		total = 0
		print(feature_vector)
		for i in range(len(WEIGHT)):
			total += WEIGHT[i][0] * feature_vector[i]
		ans_lst.append(total)
	sum = 0
	for i in range(len(ans_lst)):
		if i <= 12 and ans_lst[i] < 0:
			sum += 1
		elif i > 12 and ans_lst[i] >= 0:
			sum += 1
	acu = sum / len(maybe_email_list)
	print(ans_lst)
	print(acu)


def feature_extractor(maybe_email):
	"""
	:param maybe_email: str, the string to be processed
	:return: list, feature vector with value 0's and 1's
	"""
	feature_vector = [0] * len(WEIGHT)
	for i in range(len(feature_vector)):
		if i == 0:
			feature_vector[i] = 1 if '@' not in maybe_email else 0
		elif i == 1:
			if not feature_vector[0]:
				feature_vector[i] = 1 if '.' in maybe_email.split('@')[0] else 0
		elif i == 2:
			if not feature_vector[0]:
				feature_vector[i] = 1 if len(maybe_email.split('@')[0]) > 0 else 0
		elif i == 3:
			if not feature_vector[0]:
				feature_vector[i] = 1 if len(maybe_email.split('@')[-1]) > 0 else 0
		elif i == 4:
			feature_vector[i] = 1 if maybe_email[0].isalpha() else 0
		elif i == 5:
			if not feature_vector[0]:
				feature_vector[i] = 1 if alpha_check(maybe_email.split('@')[0]) else 0
		elif i == 6:
			feature_vector[i] = 1 if maybe_email[0].isalpha() and maybe_email[0].isupper() else 0
		elif i == 7:
			feature_vector[i] = 1 if '..' in maybe_email.split('@')[-1] else 0
		elif i == 8:
			feature_vector[i] = 1 if maybe_email[-3:] == '.tw' else 0
		elif i == 9:
			feature_vector[i] = 1 if len(maybe_email) < 13 else 0
	return feature_vector


def read_in_data():
	"""
	:return: list, containing strings that may be valid email addresses
	"""
	# TODO:
	with open(DATA_FILE, 'r') as f:
		lst = []
		for line in f:
			lst.append(line.strip())
	return lst


def alpha_check(email):
	lst = []
	for i in range(len(email)):
		if email[i].isalpha() or email[i].isdigit():
			lst.append('1')
		else:
			lst.append('0')
	if '1' not in lst:
		return True
	else:
		return False



if __name__ == '__main__':
	main()
