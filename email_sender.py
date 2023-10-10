"""A quick program that uses python in order to send an email
"""
from email.message import EmailMessage

#Password is stored in a separate file "app2.py" as password variable so we don't have to show the password in line 6 for security reasons
# from app2.py import password
import ssl
import smtplib

#insert any email as sender
email_sender = 'testEmail@gmail.com'
#insert password of sender email
email_password = 'fakePassword'

email_receiver = 'testemail123@gmail.com'

subject = "Email Subject"
body = """
Dear [person], I hope you have a good day.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string)