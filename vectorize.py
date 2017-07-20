import os
import pickle
import sys
import re
import codecs
import string
from parse_email import parseText
# import sys
# # sys.setdefaultencoding() does not exist, here!
# reload(sys)  # Reload does the trick!
# sys.setdefaultencoding('UTF8')

path=os.getcwd()
path=path+"/CSDMC2010_SPAM/CSDMC2010_SPAM/TRAINING/"
fr=open("SPAMTrain.label","r")

email_data=[]
label_data=[]
ct=0
for x in fr:
	col=x.split()
	file_name=col[1]
	file_location=os.path.join(path,file_name)
	print ("processing",file_name)
	f=open(file_location,"r")
	email_text=parseText(f)
	label_data.append(col[0])
	email_data.append(email_text)
	f.close()
print("Email processed")
fr.close()
pickle.dump(email_data,open("raw_email_data.pkl","w"))
pickle.dump(label_data,open("spam_label.pkl","w"))

