import os
import pickle
import sys

from parse_email import parseText

# curr_path=os.getcwd()
# path=""
# email_path=os.chdir(path)
# email_list=os.listdir(path)
# print email_list[0]
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
	print "processing",file_name
	email=open(file_location,"r")
	email_text=parseText(email)
	# print email_text
	label_data.append(col[0])
	email_data.append(email_text)
	# print fr
	email.close()
print "Email processed"
fr.close()

# email=open(email_list[0])
# email_text=parseText(email)