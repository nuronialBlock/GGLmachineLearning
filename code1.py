from sklearn import tree

# Coder/labels: pro, mid, beginner - 0, 1, 2
# features: Hours - Solved
# 1,4 -> 2
# 2,1 -> 1
# 3,2 -> 1
# 4,2 -> 1
# 5,1 -> 0

features = [[1,4], [2,1], [3,2], [4,2], [5,1]]
labels = [2,1,1,1,0]
clf = tree.DecisionTreeClassifier().fit(features, labels)

print clf.predict([[5,1]])