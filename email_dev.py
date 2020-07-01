import os
import smtplib
# Email address and password are stored ini environment variables for security
EMAIL = os.environ.get('EMAIL_USER')
PASSWORD = os.environ.get('EMAIL_PASS')

sender = EMAIL
reciever = 'mtabishkhanday@gmail.com'
passwd = PASSWORD

server = smtplib.SMTP('smtp.gmail.com',587)
# Encrypts our traffic
server.starttls()
server.login(sender,passwd)
# Enter message that you want to send
message = 'Git repository is committed'
# Sends email
server.sendmail(sender,reciever,message)
# print send message
print("Email send successfully")
