#!/usr/bin/env python

import sys
from sklearn import tree
import numpy as np

def DTL(trainData, testdata):
	label = []
	features = []
	with open(trainData) as f:
		for line in f:
			int_list = [float(i) for i in line.split()]
			x = int_list[:len(int_list)-1]
			y = int_list[len(int_list)-1] 
			features.append(x)
			label[len(label): ] = [y]
			print(x)
	
	# training phase
	clf = tree.DecisionTreeClassifier().fit(features, label)
	n_nodes = clf.tree_.node_count
	children_left = clf.tree_.children_left
	children_right = clf.tree_.children_right
	feature = clf.tree_.feature
	threshold = clf.tree_.threshold

	node_depth = np.zeros(shape=n_nodes)
	is_leaves = np.zeros(shape=n_nodes, dtype=bool)
	stack = [(0, -1)]  # seed is the root node id and its parent depth
	while len(stack) > 0:
	    node_id, parent_depth = stack.pop()
	    node_depth[node_id] = parent_depth + 1

	    # If we have a test node
	    if (children_left[node_id] != children_right[node_id]):
	        stack.append((children_left[node_id], parent_depth + 1))
	        stack.append((children_right[node_id], parent_depth + 1))
	    else:
	        is_leaves[node_id] = True

	for i in range(n_nodes):
	    if is_leaves[i]:
	       print("%snode=%s leaf node." % (node_depth[i] * " ", i))
	    else:
	        print("%snode=%s test node: go to node %s if feature[:, %s] <= %s else to "
	              "node %s."
	              % (node_depth[i] * " ",
	                i,
	                children_left[i],
	                feature[i],
	                threshold[i],
	                children_right[i],
                 	))

	prediction = []
	ID = 0
	classAccuracy = 0
	with open(testdata) as f:
		for line in f:
			int_list = [float(i) for i in line.split()]
			x = int_list[:len(int_list)-1]
			real = int_list[len(int_list)-1]
			feature = []
			feature.append(x) 
			predicted = float(clf.predict(feature))
			accuracy = (predicted == real)
			classAccuracy = classAccuracy + accuracy
			print("ID = %d, predicted = %3.2lf, true = %3.2lf, accuracy = %4.2lf" % (ID, predicted, real, accuracy))
			ID = ID + 1

	print("classification accuracy = %6.2lf" % ((classAccuracy * 1.0) / ID))


	

if __name__ == "__main__":
	a = str(sys.argv[1])
	b = str(sys.argv[2])
	c = str(sys.argv[3])
	DTL(a,b)