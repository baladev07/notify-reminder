import os
import smtplib
from background_task import background
from email.message import EmailMessage

Email_address = os.environ.get('Email_address')
Email_passwd = os.environ.get('Email_passwd')


@background(schedule=60)
def mail(reminder_map, to_adr):
    msg = EmailMessage()
    msg['subject'] = reminder_map['remindersub']
    msg['From'] = Email_address
    msg['To'] = to_adr
    msg.set_content(reminder_map['reminderbody'])
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        # msg=f'subject:{subject}\n\n{content}'
        smtp.login(Email_address, Email_passwd)
        # smtp.sendmail(Email_address,to_adrr,msg)
        smtp.send_message(msg)
        print("mail sent")
        del msg['subject']
