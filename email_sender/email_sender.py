import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path, PurePath

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'SENDER@MAIL.COM'
email['to'] = 'RECEIVER@MAIL.COM'
email['subject'] = 'TYPE YOUR SUBJECT'

email.set_content(html.substitute({'name':'DATA1', 'who':'DATA2'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('YOUR@EMAIL.COM', 'YOURPASSWORD')
    smtp.send_message(email)
    print('Mesaage sent!\n') 