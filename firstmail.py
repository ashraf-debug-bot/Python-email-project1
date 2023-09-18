import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Mohamed ashraf'
email['to'] = 'newashraf511@gmail.com'
email['subject'] = 'hello ashraf greet from a'

email.set_content('I am ashraf thank you for seeing my email')

# Corrected SMTP hostname
with smtplib.SMTP(host='smtp.gmail.com', port=25) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('newashraf511@gmail.com', 'rduduukhuriviypv')
    smtp.send_message(email)
    print("ready!!")

