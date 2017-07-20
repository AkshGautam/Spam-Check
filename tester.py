import sys

from process import processing


# import sys
# # sys.setdefaultencoding() does not exist, here!
# reload(sys)  # Reload does the trick!
# sys.setdefaultencoding('UTF8')
features_train, features_test, labels_train, labels_test = processing()
from sklearn.naive_bayes import GaussianNB
clf=GaussianNB()
clf.fit(features_train,labels_train)
pred=clf.predict(features_test) 
from sklearn.metrics import accuracy_score
print (accuracy_score(pred,labels_test))