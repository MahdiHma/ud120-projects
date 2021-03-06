#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
# features_train = features_train[:len(features_train) / 100]
# labels_train = labels_    train[:len(labels_train) / 100]

#########################################################
### your code goes here ###
t0 = time()
clf = SVC(kernel='rbf', C=10000)

clf.fit(features_train, labels_train)
print "fit time:", round(time() - t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "fit time:", round(time() - t0, 3), "s"
print len(pred[pred == 1])
print accuracy_score(pred, labels_test)
#########################################################
