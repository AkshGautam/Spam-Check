from nltk.stem.snowball import SnowballStemmer
import string
import email.parser 


def parseText(f):


	f.seek(0)
	# all_data=f.read()
	# fp = open(filename)
	msg = email.message_from_file(f)
	payload = msg.get_payload()
	if type(payload) == type(list()) :
		payload = payload[0] # only use the first part of payload
	sub = msg.get('subject')
	sub = str(sub)
	if type(payload) != type('') :
		payload = str(payload)
	email_data=sub+payload

	if len(email_data)>1:
		email_data=email_data.translate(string.maketrans("",""),string.punctuation)
		stemmer=SnowballStemmer("english")
		stemmed_words=[stemmer.stem(i) for i in email_data.split()]
		email_data=' '.join(stemmed_words)

		print email_data
