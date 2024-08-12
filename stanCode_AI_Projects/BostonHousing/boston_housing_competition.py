"""
File: boston_housing_competition.py
Name: Po-Ting Lee
--------------------------------
This file demonstrates how to analyze boston
housing dataset. Students will upload their 
results to kaggle.com and compete with people
in class!

You are allowed to use pandas, sklearn, or build the
model from scratch! Go data scientists!
"""

import pandas as pd
from sklearn import preprocessing, linear_model, tree, model_selection
import numpy as np

def main():
    # Load and preprocess the training data
    train_data = pd.read_csv('boston_housing/train.csv')
    train_data, val_data = model_selection.train_test_split(train_data, test_size=0.4, random_state=42)

    # Extract features and target
    original_features = ['crim', 'zn', 'indus', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'black', 'lstat']
    x_train = train_data[original_features].copy()
    y_train = train_data['medv']
    x_val = val_data[original_features].copy()
    y_val = val_data['medv']

    # Feature engineering: adding squared terms for all original features
    for feature in original_features:
        x_train.loc[:, f'{feature}_squared'] = x_train[feature] ** 2
        x_val.loc[:, f'{feature}_squared'] = x_val[feature] ** 2

    # Standardize the features
    standardizer = preprocessing.StandardScaler()
    x_train = standardizer.fit_transform(x_train)
    x_val = standardizer.transform(x_val)

    # Linear Regression model
    regressor = linear_model.LinearRegression()
    regressor.fit(x_train, y_train)
    predictions_train = regressor.predict(x_train)
    predictions_val = regressor.predict(x_val)

    mse_train = np.sqrt(np.mean((predictions_train - y_train) ** 2))
    mse_val = np.sqrt(np.mean((predictions_val - y_val) ** 2))

    print("Linear Regression Training RMSE:", mse_train)
    print("Linear Regression Validation RMSE:", mse_val)

    # Decision Tree model
    d_tree = tree.DecisionTreeRegressor()
    d_tree.fit(x_train, y_train)
    predictions_train_tree = d_tree.predict(x_train)
    predictions_val_tree = d_tree.predict(x_val)

    mse_train_tree = np.sqrt(np.mean((predictions_train_tree - y_train) ** 2))
    mse_val_tree = np.sqrt(np.mean((predictions_val_tree - y_val) ** 2))

    print("Decision Tree Training RMSE:", mse_train_tree)
    print("Decision Tree Validation RMSE:", mse_val_tree)

    # Load and preprocess the test data
    test_data = pd.read_csv('boston_housing/test.csv')
    x_test = test_data[original_features].copy()
    for feature in original_features:
        x_test.loc[:, f'{feature}_squared'] = x_test[feature] ** 2
    x_test = standardizer.transform(x_test)

    # Predict on test data using the best model (choose based on validation RMSE)
    if mse_val < mse_val_tree:
        predictions = regressor.predict(x_test)
    else:
        predictions = d_tree.predict(x_test)
    out_file(predictions, 'RSME_predict4.csv')

def out_file(predictions, filename):
    """
    :param predictions: numpy.array, a list-like data structure that stores medv predictions
    :param filename: str, the filename you would like to write the results to
    """
    print('\n===============================================')
    print(f'Writing predictions to --> {filename}')

    # Read the test data including the IDs
    test_data = pd.read_csv('boston_housing/test.csv')
    IDs = test_data.ID

    with open(filename, 'w') as out:
        out.write('ID,medv\n')
        for i in range(len(predictions)):
            out.write(str(IDs[i]) + ',' + str(predictions[i]) + '\n')

    print('===============================================')




if __name__ == '__main__':
    main()
