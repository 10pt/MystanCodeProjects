"""
File: titanic_level2.py
Name: 
----------------------------------
This file builds a machine learning algorithm by pandas and sklearn libraries.
We'll be using pandas to read in dataset, store data into a DataFrame,
standardize the data by sklearn, and finally train the model and
test it on kaggle website. Hyper-parameters tuning are not required due to its
high level of abstraction, which makes it easier to use but less flexible.
You should find a good model that surpasses 77% test accuracy on kaggle.
"""

import math
import pandas as pd
from sklearn import preprocessing, linear_model

TRAIN_FILE = 'titanic_data/train.csv'
TEST_FILE = 'titanic_data/test.csv'

nan_cache = {}

def data_preprocess(filename, mode='Train', training_data=None):
	"""
	:param filename: str, the filename to be read into pandas
	:param mode: str, indicating the mode we are using (either Train or Test)
	:param training_data: DataFrame, a 2D data structure that looks like an excel worksheet
						  (You will only use this when mode == 'Test')
	:return: Tuple(data, labels), if the mode is 'Train'; or return data, if the mode is 'Test'
	"""
	data = pd.read_csv(filename)
	labels = None



	# print(data.count())
	if mode == 'Train':
		columns_to_keep = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
		data = data[columns_to_keep]
		data = data.dropna()
		nan_cache['Age'] = round(data.Age.mean(), 3)
		nan_cache['Fare'] = round(data.Fare.mean(), 3)
		labels = data.pop('Survived')
		# Data process aligned with Test
		data.Age.fillna(nan_cache['Age'], inplace=True)
		data.Fare.fillna(nan_cache['Fare'], inplace=True)
		data.loc[data.Sex == 'male', 'Sex'] = 1
		data.loc[data.Sex == 'female', 'Sex'] = 0
		# Changing 'S' to 0, 'C' to 1, 'Q' to 2
		data['Embarked'].replace(['S', 'C', 'Q'], ['0', '1', '2'], inplace=True)
		return data, labels
	elif mode == 'Test':
		columns_to_keep = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
		data = data[columns_to_keep]
		data.Age.fillna(nan_cache['Age'], inplace=True)
		data.Fare.fillna(nan_cache['Fare'], inplace=True)
		data.loc[data.Sex == 'male', 'Sex'] = 1
		data.loc[data.Sex == 'female', 'Sex'] = 0
		# Changing 'S' to 0, 'C' to 1, 'Q' to 2
		data['Embarked'].replace(['S', 'C', 'Q'], ['0', '1', '2'], inplace=True)

		return data


def one_hot_encoding(data, feature):
	"""
	:param data: DataFrame, key is the column name, value is its data
	:param feature: str, the column name of interest
	:return data: DataFrame, remove the feature column and add its one-hot encoding features
	"""

	if feature == 'Sex':
		# One hot encoding for a new category Male
		data['Sex_1'] = 0
		data.loc[data.Sex == 1, 'Sex_1'] = 1
		# One hot encoding for a new category Female
		data['Sex_0'] = 0
		data.loc[data.Sex == 0, 'Sex_0'] = 1
		# No need Sex anymore!
		data.pop('Sex')
	elif feature == 'Pclass':
		# One hot encoding for a new category Pclass_0
		data['Pclass_0'] = 0
		data.loc[data.Pclass == 1, 'Pclass_0'] = 1
		# One hot encoding for a new category Pclass_1
		data['Pclass_1'] = 0
		data.loc[data.Pclass == 2, 'Pclass_1'] = 1
		# One hot encoding for a new category Pclass_2
		data['Pclass_2'] = 0
		data.loc[data.Pclass == 3, 'Pclass_2'] = 1
		# No need Pclass anymore!
		data.pop('Pclass')
	elif feature == 'Embarked':
		# One hot encoding for a new category Embarked_0
		data['Embarked_0'] = 0
		data.loc[data.Embarked == 0, 'Embarked_0'] = 1
		# One hot encoding for a new category Embarked_1
		data['Embarked_1'] = 0
		data.loc[data.Embarked == 1, 'Embarked_1'] = 1
		# One hot encoding for a new category Embarked_2
		data['Embarked_2'] = 0
		data.loc[data.Embarked == 2, 'Embarked_2'] = 1
		# No need Embarked anymore!
		data.pop('Embarked')
	return data


def standardization(data, mode='Train'):
	"""
	:param data: DataFrame, key is the column name, value is its data
	:param mode: str, indicating the mode we are using (either Train or Test)
	:return data: DataFrame, standardized features
	"""
	standardizer = preprocessing.StandardScaler()

	if mode == 'Train':
		data = standardizer.fit_transform(data)

	if mode == 'Test':
		data = standardizer.transform(data)
	return data


def main():
	"""
	You should call data_preprocess(), one_hot_encoding(), and
	standardization() on your training data. You should see ~80% accuracy on degree1;
	~83% on degree2; ~87% on degree3.
	Please write down the accuracy for degree1, 2, and 3 respectively below
	(rounding accuracies to 8 decimal places)
	TODO: real accuracy on degree1 -> 0.80196629
	TODO: real accuracy on degree2 -> 0.83707865
	TODO: real accuracy on degree3 -> 0.87359550
	"""
	train_data, Y = data_preprocess(TRAIN_FILE, mode='Train')
	test_data = data_preprocess(TEST_FILE, mode='Test')

	one_hot_encoding(train_data, 'Sex')
	one_hot_encoding(train_data, 'Pclass')
	one_hot_encoding(train_data, 'Embarked')
	one_hot_encoding(test_data, 'Sex')
	one_hot_encoding(test_data, 'Pclass')
	one_hot_encoding(test_data, 'Embarked')

	standardizer = preprocessing.StandardScaler()
	train_data = standardizer.fit_transform(train_data)
	test_data = standardizer.transform(test_data)


	degrees = [1, 2, 3]
	accuracies = []
	for degree in degrees:
		poly_phi_extractor = preprocessing.PolynomialFeatures(degree=degree)
		train_data_poly = poly_phi_extractor.fit_transform(train_data)

		# Fit the model
		h = linear_model.LogisticRegression(max_iter=10000)
		classifier = h.fit(train_data_poly, Y)

		# Print training accuracy
		train_acc = classifier.score(train_data_poly, Y)
		print(f'Training Accuracy (degree {degree}): {train_acc}')
		accuracies.append(train_acc)

	return accuracies

if __name__ == '__main__':
	main()
