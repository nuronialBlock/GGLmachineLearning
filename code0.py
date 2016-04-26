from sklearn import tree 

# bumpy - 0
# smooth - 1
features = [[140, 1], [130, 1], [150, 0], [170, 0]] 
# apple - 0
# orange - 1
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier() # Rules
clf = clf.fit(features,labels) # Algorithm to find patterns in data
print clf.predict([[150,0]])