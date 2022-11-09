import os
import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()

#login to gmail
email = '******@gmail.com'
password = os.environ.get("APP_PASSWORD")
smtp_object.login(email, password)

#send mail
from_address = email
to_address = '***@gmail.com'
subject = 'subject'
message = '''
message
'''
msg = "Subject: " + subject + '\n' + message
smtp_object.sendmail(from_address,to_address, msg.encode('utf-8'))

#close session
smtp_object.quit()