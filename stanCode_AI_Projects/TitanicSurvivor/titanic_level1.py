"""
File: titanic_level1.py
Name: Po-Ting Lee
----------------------------------
This file builds a machine learning algorithm from scratch 
by Python. We'll be using 'with open' to read in dataset,
store data into a Python dict, and finally train the model and 
test it on kaggle website. This model is the most flexible among all
levels. You should do hyper-parameter tuning to find the best model.
"""
import csv
import math

TRAIN_FILE = 'titanic_data/train.csv'
TEST_FILE = 'titanic_data/test.csv'

nan_cache = {}

def data_preprocess(filename: str, data: dict, mode='Train', training_data=None):
    """
    Process data from a CSV file.

    :param filename: str, the name of the file to be processed.
    :param data: dict, an empty dictionary to store the processed data.
    :param mode: str, indicates if it's training or testing mode.
    :param training_data: dict, contains training data if mode is 'Test'.
    :return data: dict, contains processed data with column names as keys.
    """

    # Read the data
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)

        for column_name in header:
            data[column_name] = []

        # Populate data dictionary
        for row in csv_reader:
            for column_index, column_value in enumerate(row):
                # Convert specific columns to integers
                if header[column_index] in ['Survived', 'Pclass', 'SibSp', 'Parch']:
                    data[header[column_index]].append(int(column_value))
                else:
                    data[header[column_index]].append(column_value)

    # Select columns by mode
    if mode == 'Train':
        columns_to_keep = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    else:
        columns_to_keep = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']

    # Filter columns
    filtered_data = {column: data[column] for column in columns_to_keep}

    # Dealing missing values
    if mode == 'Train':
        # Remove rows with missing values
        non_empty_index = [i for i in range(len(filtered_data['Age'])) if all(filtered_data[col][i] != '' for col in filtered_data)]
        for column in filtered_data:
            filtered_data[column] = [filtered_data[column][i] for i in non_empty_index]
    elif mode == 'Test' and training_data is not None:
        # Replace null 'Age' values with the mean age from the training data
        ages = [float(val) for val in training_data['Age'] if val != '']
        mean_age = sum(ages) / len(ages) if ages else 0
        filtered_data['Age'] = [float(val) if val != '' else mean_age for val in filtered_data['Age']]

        fares = [float(val) for val in training_data['Fare'] if val != '']
        mean_fare = round(sum(fares) / len(fares), 3) if fares else 0
        filtered_data['Fare'] = [float(val) if val != '' else mean_fare for val in filtered_data['Fare']]


    for key, value in filtered_data.items():
        if key in ['Age', 'Fare']:
            # Convert string values to floats
            filtered_data[key] = [float(val) if val != '' else nan_cache[key] for val in value]
        elif key == 'Sex':
            # Convert 'male' to 1 and 'female' to 0
            filtered_data[key] = [1 if sex == 'male' else 0 for sex in value]
        elif key == 'Embarked':
            # Convert 'S', 'C', and 'Q' to 0, 1, and 2
            filtered_data[key] = [0 if embarked == 'S' else 1 if embarked == 'C' else 2 for embarked in value]

    return filtered_data

def one_hot_encoding(data: dict, feature: str):
    """
	:param data: dict[str, list], key is the column name, value is its data
	:param feature: str, the column name of interest
	:return data: dict[str, list], remove the feature column and add its one-hot encoding features
	"""
    if feature in data:
        target_lst = data[feature]
        num_category = []
        for target in target_lst:
            if target not in num_category:
                num_category.append(target)

        for i in range(len(num_category)):
            data[feature+'_'+str(i)] = []

        for i in range(len(target_lst)):
            for j in range(len(num_category)):
                if feature == 'Pclass':
                    target = target_lst[i] - 1
                else:
                    target = target_lst[i]
                if target == j:
                    data[feature+'_'+str(j)].append(1)
                else:
                    data[feature+'_'+str(j)].append(0)
    data.pop(feature)
    return data


def normalize(data: dict):
    """
	:param data: dict[str, list], key is the column name, value is its data
	:return data: dict[str, list], key is the column name, value is its normalized data
	"""

    for column_name, column_data in data.items():
        if all(isinstance(value, (int, float)) for value in column_data):
            min_value = min(column_data)
            max_value = max(column_data)
            normalized_column = [(value - min_value) / (max_value - min_value) for value in column_data]
            data[column_name] = normalized_column
    return data


def learnPredictor(inputs: dict, labels: list, degree: int, num_epochs: int, alpha: float):
    """
    Train a simple machine learning model using gradient descent.

    :param inputs: dict[str, list], a dictionary where each key represents a type of data and its corresponding value is a list of values.
    :param labels: list[int], a list indicating the actual outcome for each set of data.
    :param degree: int, a number representing the complexity of the model.
    :param num_epochs: int, the number of times the model will go through the entire dataset during training.
    :param alpha: float, a number representing the step size used in the learning process.
    :return weights: dict[str, float], a dictionary containing the weights assigned to each feature.
    """

    def increment(d1, scale, d2):
        """
        Increment dictionary d1 by scale * d2.
        :param d1: dict, the dictionary to be incremented.
        :param scale: float, the scaling factor.
        :param d2: dict, the dictionary to be scaled and added to d1.
        """
        for key, value in d2.items():
            d1[key] = d1.get(key, 0) + scale * value

    def dotProduct(d1, d2):
        """
        Compute the dot product between two dictionaries.
        :param d1: dict, the first dictionary.
        :param d2: dict, the second dictionary.
        :return: float, the dot product between d1 and d2.
        """
        if len(d1) < len(d2):
            return dotProduct(d2, d1)
        else:
            return sum(d1.get(key, 0) * value for key, value in d2.items())

    # Initialize weights
    weights = {}
    keys = list(inputs.keys())
    num_features = len(keys)

    if degree == 1:
        for i in range(num_features):
            weights[keys[i]] = 0
    elif degree == 2:
        for i in range(num_features):
            weights[keys[i]] = 0
        for i in range(num_features):
            for j in range(i, num_features):
                weights[keys[i] + keys[j]] = 0

    # Start training
    for epoch in range(num_epochs):
        for i in range(len(labels)):
            feature = {}
            if degree == 1:
                for j in range(num_features):
                    feature[keys[j]] = inputs[keys[j]][i]
            else:
                for j in range(num_features):
                    feature[keys[j]] = inputs[keys[j]][i]
                for j in range(num_features):
                    for k in range(j, num_features):
                        feature[keys[j] + keys[k]] = inputs[keys[j]][i] * inputs[keys[k]][i]
            # Calculate prediction
            prediction = util.dotproduct(weights, feature)
            prediction = 1/(1+math.exp(-prediction))
            error = prediction - labels[i]

            # Update weights
            utl.increment(weights, -alpha * error, feature)

    return weights










