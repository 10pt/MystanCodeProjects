"""
File: validEmailAddress_2.py
Name: Po-Ting Lee
----------------------------
Please construct your own feature vectors
and try to surpass the accuracy achieved by
Jerry's feature vector in validEmailAddress.py.
feature1:  '@' in the str
feature2:  '.' before '@'
feature3:  some strings before '@'
feature4:  some strings after '@'
feature5:  '.' after '@'
feature6:  't\' in the str
feature7:  '\a' in the str
feature8:  '\' in the str
feature9:  '..' in the str
feature10: length > 9

Accuracy of your model: 0.884615384615385
"""

import numpy as np

WEIGHT = [                           # The weight vector selected by you
	[0.4],                           # (see assignment handout for more details)
	[-0.39],
	[-0.5],
	[-0.5],
	[1],
	[-6],
	[-0.5],
	[-6],
	[-7],
	[-1]
]

DATA_FILE = 'is_valid_email.txt'     # This is the file name to be processed


def main():
	maybe_email_list = read_in_data()
	predict_result = []
	for maybe_email in maybe_email_list:
		feature_vector = feature_extractor(maybe_email)
		weight_vector = np.array(WEIGHT)
		weight_vector = weight_vector.T
		score = weight_vector.dot(feature_vector)
		print(np.sum(score))
		if np.sum(score) > 0:
			predict_result.append(1)
			score = np.zeros((10, 1))
		else:
			predict_result.append(0)
			score = np.zeros((10, 1))
	print("Predict result", predict_result)
	total = 0
	real_data = [0] * 13 + [1] * 13
	for y_pre, y_true in zip(predict_result, real_data):
                if y_pre == y_true:
                        total += 1
        print("Acc: ", total/len(real_data))

def feature_extractor(maybe_email):
	"""
	:param maybe_email: str, the string to be processed
	:return: list, feature vector with value 0's and 1's
	"""

	feature_vector = np.zeros((10, 1))
	for i in range(len(feature_vector)):
		if i == 0:
			feature_vector[i][0] = 1 if '@' in maybe_email else 0
		elif i == 1:
			if feature_vector[0]:
				feature_vector[i][0] = 1 if '.' in maybe_email.split('@')[0] else 0
		elif i == 2:
			if feature_vector[0]:
				feature_vector[i][0] = 0 if len(maybe_email.split('@')[0]) else 1
		elif i == 3:
			if feature_vector[0]:
				feature_vector[i][0] = 0 if len(maybe_email.split('@')[1]) else 1
		elif i == 4:
			if feature_vector[0]:
				feature_vector[i][0] = 1 if '.' in maybe_email.split('@')[1] else 0
		elif i == 5:
			if feature_vector[0]:
				feature_vector[i][0] = 1 if maybe_email.count('t\"') else 0
		elif i == 6:
			if feature_vector[0]:
				feature_vector[i][0] = 1 if '\\a' in maybe_email.split('@')[0] else 0
		elif i == 7:
			if feature_vector[0]:
				feature_vector[i][0] = 1 if '[\\]' in maybe_email.split('@')[0] else 0
		elif i == 8:
			if feature_vector[0]:
				feature_vector[i][0] = 1 if '..' in maybe_email else 0
		elif i == 9:
			if feature_vector[0]:
				feature_vector[i][0] = 1 if len(maybe_email) > 9 else 0


	return feature_vector



def read_in_data():
	"""
	:return: list, containing strings that may be valid email addresses
	"""
	maybe_email_list = []
	with open(DATA_FILE, 'r') as f:                         # 1. Read the file.
		for email in f:                                 # 2. Read the contents.
			email = email.strip()                   # 3. Remove the newline (\n).
			maybe_email_list.append(email)          # 4. Append the email to the list.

	return maybe_email_list


if __name__ == '__main__':
	main()
