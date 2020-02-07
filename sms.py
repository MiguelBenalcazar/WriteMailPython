import os
import smtplib 
import imghdr
from email.message import EmailMessage

FROM_EMAIL = "WRITE EMAIL"
PASSWORD_EMAIL = "WRITE PASSWORD TO THE EMAIL"
TO_EMAIL = "WRITE EMAIL TO SEND"

msg = EmailMessage()
msg['Subject'] = 'Hi'
msg['From']  = FROM_EMAIL
msg['To'] = TO_EMAIL
msg.set_content('It is done')

files = ['README.md', 'image.jpg']
for file in files:
    with open(file,'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    # msg.add_attachment(file_data, maintype='image', subtype = file_type, filename =file_name )
    msg.add_attachment(file_data, maintype='application', subtype = 'octet-stream', filename =file_name )

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(FROM_EMAIL, PASSWORD_EMAIL)
    smtp.send_message(msg)

