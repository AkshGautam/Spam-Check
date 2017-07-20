import pickle
import numpy
import codecs
from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif

def processing(email_file="raw_email_data.pkl",label_file="spam_label.pkl"):




	email_file_handler=open(email_file, "r")
	emails=pickle.load(email_file_handler)
	email_file_handler.close()

	label_file_handler=open(label_file, "r")
	labels=pickle.load(label_file_handler)
	label_file_handler.close()
	

	features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(emails, labels, test_size=0.1, random_state=42)

	vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
								 stop_words='english')
	features_train_transformed = vectorizer.fit_transform(features_train)
	features_test_transformed  = vectorizer.transform(features_test)

	selector = SelectPercentile(f_classif, percentile=10)
	selector.fit(features_train_transformed, labels_train)
	features_train_transformed = selector.transform(features_train_transformed).toarray()
	features_test_transformed  = selector.transform(features_test_transformed).toarray()
	
	
	return features_train_transformed, features_test_transformed, labels_train, labels_test




	