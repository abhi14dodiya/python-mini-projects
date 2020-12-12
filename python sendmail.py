import smtplib # we ned this for as protocol 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = '' # your mail id
email_password = '' # dont share your password file with othres
email_send = ''#target mail id 

subject = '   '#title of the mail

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = '''you can write you full message here '''# this is body section of mail


msg.attach(MIMEText(body,'plain'))
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)#this will req to google
server.starttls()
server.login(email_user,email_password) # will let  your program  into your gmail 

for i in range(1,5):  #this is just fun part where you can send mail multipal time but don't use as spam tool.
    
    server.sendmail(email_user,email_send,text)
    print(i)
server.quit()
