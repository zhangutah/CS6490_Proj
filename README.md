## Simple SMTP Server 

**ALL the code MUST run on the CADE Lab([eng.utah.edu](https://nx.eng.utah.edu/) )**

```
ssh u1399304@lab1-5.eng.utah.edu
```

### Bootstrap

Pls edit the `spam_filter.py` for custom filtering rules

SMTP Server:
```
python3 mail_server.py
Starting SMTP Gateway...
Receiving message from: ('127.0.0.1', 33862)
Message addressed from: u1399304@eng.utah.edu
Message addressed to: ['xxx@cs.utah.edu']
Message length: 688
[-] SPAM detected!
Receiving message from: ('127.0.0.1', 33902)
Message addressed from: u1399304@eng.utah.edu
Message addressed to: ['xxxx@cs.utah.edu']
Message length: 688
[-] SPAM detected!
Receiving message from: ('127.0.0.1', 33934)
Message addressed from: u1399304@eng.utah.edu
Message addressed to: ['xxxx@cs.utah.edu']
Message length: 971
```

Client:

```
[u1399304@lab1-6 smtp_misc]$ python3 spam_client.py
Refused, reason: b'Bad address: SPAM'

[u1399304@lab1-6 smtp_misc]$ python3 mail_client.py
Successfully sent email
```

The verified email will be sent to the target email address:

![mail.png](https://s2.loli.net/2022/04/20/5oCElmSJPL9YbQF.png)

