from nltk.stem.snowball import SnowballStemmer
import string
import email.parser 
import re,cgi


def parseText(f):

	# f.seek(0)

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
		ans=""
		email_data= re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '',email_data, flags=re.MULTILINE)
		cleanr = re.compile('<.*?>')
		email_data = re.sub(cleanr, '',email_data)
		email_data=email_data.replace("'","")
		email_data=email_data.replace('"',"")
		for x in email_data:
			if x>='a' and x<='z' or x>='A' and x<='Z'or x==' ':
				ans=ans+x
		stemmer=SnowballStemmer("english")
		stemmed_words=[stemmer.stem(i) for i in ans.split()]
		ans=' '.join(stemmed_words)

	return ans