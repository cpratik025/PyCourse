import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
#set the path to the html file using path class and then wrapping that path into a template
html = Template(Path('email_html.html').read_text())
email = EmailMessage()
email['from'] = 'Pratik Chorsiya'
email['to'] = 'TOEMAIL.com'
email['subject']= 'Just a python email code'
#setting the content to replace the name variable in email_html and specifying we are passing a html file using 2nd parameter
email.set_content(html.substitute({'name' : 'Pratik'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as mail:
    mail.ehlo()
    mail.starttls()
    mail.login('FROMEMAIL.com','Password')
    mail.send_message(email)
    print('All Good Boss')

