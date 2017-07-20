from sklearn import svm
from process import processing
from plot import prettyPicture, output_image

features_train, features_test, labels_train, labels_test = processing()
clf=svm.SVC(kernel="rbf",C=10000,gamma=0.001)
clf.fit(features_train,labels_train)
pred=clf.predict(features_test) 
from sklearn.metrics import accuracy_score
print (accuracy_score(pred,labels_test))
