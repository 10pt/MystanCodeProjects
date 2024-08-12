"""
File: interactive.py
Name: Po-Ting Lee
------------------------
This file uses the function interactivePrompt
from util.py to predict the reviews input by 
users on Console. Remember to read the weights
and build a Dict[str: float]
"""

from util import interactivePrompt

def featureExtractor(x):

    features = {}

    for word in x.split():
        features[word] = features.get(word, 0) + 1
    return features

def main():

    weights = {}
    with open('weights', 'r') as file:
        for line in file:
            token, weight = line.strip().split()
            weight = float(weight)
            weights[token] = weight

    interactivePrompt(featureExtractor, weights)


if __name__ == '__main__':
	main()
