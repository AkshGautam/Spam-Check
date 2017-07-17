import os
import pickle
import sys

from parse_email import parseText

curr_path=os.getcwd()
path="/home/aksh/web_app/Sweeper/CSDMC2010_SPAM/CSDMC2010_SPAM/TRAINING"
email_path=os.chdir(path)
email_list=os.listdir(path)
print email_list[0]

email_data=[]
from_data=[]


# for i in email_list:
print len(email_list)
# email=open(email_list[0])
# email_text=parseText(email)