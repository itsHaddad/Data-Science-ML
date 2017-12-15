from sklearn import tree


# [height, weight, shoe size]

x = [[190,80,44],
     [177,40,40],
     [160,60,38],
     [154,54,37],
     ]
# [hair, weight], can't use this here I think. But it would have been interesting to know if it could work or not.
x1 = [["black", 90], ["brown",50], ["blonde",60], ["black", 60]]

y = ['male', 'female','male','female']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

prediction = clf.predict([[140,60,42]])

#prediction = clf.predict([["black", 70]])

print (prediction)