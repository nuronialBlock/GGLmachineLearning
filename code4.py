# lec 2 Practice
import numpy as np 
from sklearn.datasets import load_iris
from sklearn import tree

# Disqus:: why 20, 70, 120 fails?
iris = load_iris()
test_idx = [20, 71, 120]

# testing data 
test_data = iris.data[test_idx]
test_target =iris.target[test_idx]

#train data
train_data = np.delete(iris.data, test_idx, axis=0)
train_target = np.delete(iris.target, test_idx)

# train classifier
clf = tree.DecisionTreeClassifier().fit(train_data, train_target)
print test_target
print clf.predict(test_data)
#print iris.target