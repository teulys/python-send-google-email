import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

mail_content = '''Alerta de lectura diaria
La lectura diaria no se registro en la base de datos de firebase'''
#The mail addresses and password
sender_address = os.environ['SENDER_EMAIL']
sender_pass = os.environ['SENDER_PASS']
receiver_address = os.environ['RECEIVER_EMAIL']
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Alerta de lectura diaria.'   #The subject line
#The body and the attachments for the mail
# message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')