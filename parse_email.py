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
	
	print sub + payload