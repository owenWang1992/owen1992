#!/usr/bin/env python
#
# Very basic example of using Python 3 and IMAP to iterate over emails in a
# gmail folder/label.  This code is released into the public domain.
#
# This script is example code from this blog post:
# http://www.voidynullness.net/blog/2013/07/25/gmail-email-with-python-via-imap/
#
# This is an updated version of the original -- modified to work with Python 3.4.
#
import sys
import imaplib
import getpass
import email
import email.header
import datetime

EMAIL_ACCOUNT = "sihaowang4test@gmail.com"
EMAIL_PWD = "sihaowang419"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993
EMAIL_ACCOUNT = "notatallawhistleblowerIswear@gmail.com"

# Use 'INBOX' to read inbox.  Note that whatever folder is specified,
# after successfully running this script all emails in that folder
# will be marked as read.
EMAIL_FOLDER = "Top Secret/PRISM Documents"


def checkgmail():
    """
    Do something with emails messages in the folder.  
    For the sake of this example, print some headers.
    """
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(EMAIL_ACCOUNT, EMAIL_PWD)
        mail.select('inbox')
        rv, data = mail.search(None, "ALL")
        if rv != 'OK':
            print("No messages found!")
            return

        for num in data[0].split():
            rv, data = mail.fetch(num, '(RFC822)')
            if rv != 'OK':
                print("ERROR getting message", num)
                return

        msg = email.message_from_bytes(data[0][1])
        hdr = email.header.make_header(email.header.decode_header(msg['Subject']))
        subject = str(hdr)
        print('Message %s: %s' % (num, subject))
        print('Raw Date:', msg['Date'])
        # Now convert to local date-time
        date_tuple = email.utils.parsedate_tz(msg['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
            print("Local Date:",
                  local_date.strftime("%a, %d %b %Y %H:%M:%S"))
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    checkgmail()
