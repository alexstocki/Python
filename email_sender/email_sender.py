import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path, PurePath

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'xotitomanzanita@gmail.com'
email['to'] = 'alexstocki22@gmail.com'
email['subject'] = 'No te pierdas esta oportunidad!'

email.set_content(html.substitute({'name':'Lucianita', 'who':'Xote'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('xotitomanzanita@gmail.com', 'Manzanita20!')
    smtp.send_message(email)
    print('Mensaje enviado, lince ;)\n') 