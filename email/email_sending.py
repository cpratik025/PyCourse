import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Pratik Chorsiya'
email['to'] = 'TOEMAIL.com'
email['subject']= 'Just a python email code'

email.set_content('Python Email Content!!!!')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as mail:
    mail.ehlo()
    mail.starttls()
    mail.login('FROMEMAIL.com','Password')
    mail.send_message(email)
    print('All Good Boss')

