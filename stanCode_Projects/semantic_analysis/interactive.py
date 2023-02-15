"""
File: interactive.py
Name: Joanne
------------------------
This file uses the function interactivePrompt
from util.py to predict the reviews input by 
users on Console. Remember to read the weights
and build a Dict[str: float]
"""

from util import *
from submission import *


def main():
	trainExamples = readExamples('polarity.train')
	validationExamples = readExamples('polarity.dev')
	weights = learnPredictor(trainExamples, validationExamples, extractWordFeatures, numEpochs=40, alpha=0.01)
	interactivePrompt(extractWordFeatures, weights)


if __name__ == '__main__':
	main()