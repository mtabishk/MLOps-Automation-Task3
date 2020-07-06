import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

f = open('accuracy.txt','r')
accuracy = f.readline()
accuracy = str(accuracy)
print(accuracy)

mail_content = """Congratulations Developer,
The Accuracy of your model is:\t """+ accuracy 

#The mail addresses and password
sender_address = 'XXXXXXXXXXXXXXXXX'
sender_pass = 'XXXXXXXXXXXXXXXX'
receiver_address = 'XXXXXXXXXXXX'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Accuracy of the model.'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
