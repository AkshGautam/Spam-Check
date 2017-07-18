from nltk.stem.snowball import SnowballStemmer
import string
import email.parser 
import re,cgi

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
		email_data= re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '',email_data, flags=re.MULTILINE)
 		tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
 		no_tags = tag_re.sub('',email_data)
 		email_data = cgi.escape(no_tags)
		email_data=email_data.translate(string.maketrans("",""),string.punctuation)
		# to remove excess whitespaces
		' '.join(email_data.split())
		email_data.strip()
		# To check the string which in this case is not as expected /x93 instead of punctuation removal
		# lis=email_data.split()
		# print lis
		# stemmer not working cos the above code is not removing punctuation
		# stemmer=SnowballStemmer("english")
		# stemmed_words=[stemmer.stem(i) for i in email_data.split()]
		# email_data=' '.join(stemmed_words)
		# print email_data

	return email_data