#!/usr/bin/env python

import sys
from sklearn import tree

def DTL(trainData, testdata):
	label = []
	features = []
	with open(trainData) as f:
		for line in f:
			int_list = [int(i) for i in line.split()]
			x = int_list[:len(int_list)-1]
			y = int_list[len(int_list)-1] 
			features.append(x)
			label[len(label): ] = [y]
	
	# training
	clf = tree.DecisionTreeClassifier().fit(features, labels)

	#predict
	with open(testdata) as f:
		for line in f:
			int_list = [int(i) for i in line.split()]
			x = int_list[:len(int_list)-1]
			y = int_list[len(int_list)-1]
			feature = []
			feature.append(x) 
			print clf.predict(feature)

	

if __name__ == "__main__":
	a = str(sys.argv[1])
	b = str(sys.argv[2])
	c = str(sys.argv[3])
	DTL(a)