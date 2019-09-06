
# =======================================+SCRIPT BY YASSINE BAGHDADI+===========================================
#
# ==========================================+ Date : 05-09-2019 +===============================================
#
# ================================+contact : www.facebook.com/yassine.baghdadi.391+=============================
#
# ====================================+github : www.github.com/DeveYassineBaghdadi =============================
#
#===============================================================================================================


import smtplib
import getpass
import time

sender = 'your email adress'
password = 'your email password'
sendTo = ['me@exemole.com','me@exemole.com','me@exemole.com','me@exemole.com'] 

sub = 'this is the subject of the message ...'
body = 'here write your message ...'
msg =f'subject: {sub},\n\n{body}'

def login():
	snd.ehlo()
	snd.starttls()
	snd.ehlo()
	snd.login(sender, password)

def send ():
	for i in sendTo:
		try:
			snd.sendmail(sender,i,msg)
			print(i , ' is done ')
		except Exception as e:
			print (' not sent to ',i)
		time.sleep(1)
with smtplib.SMTP('smtp.gmail.com' , 587) as snd:
	login()
	send()
