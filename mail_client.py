#!/usr/bin/env python

import sys
import smtplib
from email.mime.text import MIMEText

recp = sys.argv[1] if len(sys.argv) >= 2 else 'zhangyh@cs.utah.edu'

sender = 'u1399304@eng.utah.edu'
receivers = [recp]


content = '''
Hi [name],

It was great to talk to you on [day or date] and find out a bit more about
[name or description of project]. I’ve taken a closer look at the details, and
I’m now pleased to share your quote below.
Here are the open questions we discussed, which I’ve now answered:
The total cost will be [amount] [plus or including taxes]. This quote is valid
until [expiry date] and I’ve attached a detailed quote to this email.
If you’re happy to go ahead, my next available start date is currently [date],
so please let me know if this works for you.

Many thanks,

[Email signature]
'''

port = 1025
msg = MIMEText(content)

msg['Subject'] = 'A simple email'
msg['From'] = 'example@example.org'
msg['To'] = recp

with smtplib.SMTP('localhost', port) as server:

    # server.login('username', 'password')
    server.sendmail(sender, receivers, msg.as_string())
    print("Successfully sent email")

