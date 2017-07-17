import smtplib
content="Aur"
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('dimwit1994@gmail.com','')
for _ in range(5):	
	mail.sendmail('dimwit1994@gmail.com','akshgautia@gmail.com',content)
mail.close()