import os
import smtplib
from background_task import background
from email.message import EmailMessage



@background(schedule=60)
def sendMail(reminder_map, to_adr):
    Email_address = 'notifyreminder@gmail.com'
    Email_passwd = 'notify_07'
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
