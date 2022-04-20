#!/usr/bin/env python

import sys
import smtplib
from email.mime.text import MIMEText
from smtplib import SMTPAuthenticationError, SMTPRecipientsRefused

recp = sys.argv[1] if len(sys.argv) >= 2 else 'zhangyh@cs.utah.edu'

sender = 'u1399304@eng.utah.edu'
receivers = [recp]


content = '''
Hi xx,

do not have money , get software cds from here !

my name is jason , i recently visited www.clothingplus.fi / and wanted to offer my services . we could help you with your wearable electronics website . we create websites that mean business for you ! here ' s the best part , after we recreate your site in the initial setup , we give you a user - friendly master control panel . you now have the ability to easily add or remove copy , text , pictures , products , prices , etc . when you want to

Spam bot
'''

port = 1025
msg = MIMEText(content)

msg['Subject'] = 'A Spam Sample AAA'
msg['From'] = 'example@example.org'
msg['To'] = recp

with smtplib.SMTP('localhost', port) as server:
    try:
        # server.login('username', 'password')
        server.sendmail(sender, receivers, msg.as_string())
        print("Successfully sent Spam")
    except smtplib.SMTPDataError as e:
        print('Refused, reason: %s' % e.smtp_error)

