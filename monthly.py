#!/usr/bin/env python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import datetime
import os

def gen_monthly_stats():
    return os.system('vnstat -u && vnstati -vs -i wlp4s0 -o /home/kofi/workspace/personal/py/ius/img/monthly_summary.png -m')

def send_mail(to, subject, text, files=[]):
    assert type(to)==list
    assert type(files) == list
    
    USERNAME = os.environ['GMAIL_SMTP_ID']
    PASSWORD = os.environ['GMAIL_SMTP_PASSWORD']
    DATE     = formatdate(localtime=True)
    MONTH    = datetime.datetime.now().strftime("%B")
    
    msg = MIMEMultipart()
    msg['From'] = USERNAME
    msg['To'] = COMMASPACE.join(to)
    msg['Date'] = DATE
    msg['Subject'] = subject + MONTH
    msg.attach( MIMEText(text) )

    for file in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(file,"rb").read() )
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
        msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.ehlo_or_helo_if_needed()
    server.login(USERNAME,PASSWORD)
    server.sendmail(USERNAME, to, msg.as_string())
    server.quit()

if gen_monthly_stats() == 0:
    recipients   = [os.environ['MY_EMAIL_ADDRESS']]
    subject      = "Internet usage for the month: "
    body         = "Please find attached your internet usage for the month"
    summary_imgs = ["/home/kofi/workspace/personal/py/ius/img/monthly_summary.png"]

    send_mail(recipients, subject, body, summary_imgs)