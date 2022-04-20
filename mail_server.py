import smtpd
import asyncore
import threading
from subprocess import Popen, PIPE
from email.parser import Parser, BytesParser
from spam_filter import filter

class CustomSMTPServer(smtpd.SMTPServer):
  def process_message(self, peer, mailfrom, rcpttos, data, mail_options=None,rcpt_options=None):
    print('Receiving message from:', peer)
    print('Message addressed from:', mailfrom)
    print('Message addressed to:', rcpttos)
    print('Message length:', len(data))

    email = BytesParser().parsebytes(data)
    for part in email.walk():
        if part.get_content_maintype() == 'text':
            text = part.get_payload()
            if filter(text):
                print("[-] SPAM detected!")
                return '550 Bad address: SPAM'
            # print(text)
            # Process text

    p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
    p.communicate(data)

    return

class SMTPServer():
  def __init__(self):
    self.port = 1025

  def start(self):
    '''Start listening on self.port'''
    # create an instance of the SMTP server, derived from  asyncore.dispatcher
    self.smtp = CustomSMTPServer(('0.0.0.0', self.port), None)
    # start the asyncore loop, listening for SMTP connection, within a thread
    # timeout parameter is important, otherwise code will block 30 seconds
    # after the smtp channel has been closed
    kwargs = {'timeout':1, 'use_poll': True}
    self.thread = threading.Thread(target=asyncore.loop, kwargs=kwargs)
    self.thread.start()

  def stop(self):
    '''Stop listening to self.port'''
    # close the SMTPserver to ensure no channels connect to asyncore
    self.smtp.close()
    # now it is safe to wait for asyncore.loop() to exit
    self.thread.join()

  # check for emails in a non-blocking way
  def get(self):
    '''Return all emails received so far'''
    return self.smtp.emails

if __name__ == '__main__':
    print("Starting SMTP Gateway...")
    server = CustomSMTPServer(('0.0.0.0', 1025), None)
    asyncore.loop()
