#-*- encoding: utf-8 -*-
#-*- encoding: gbk -*-
import smtplib
import time
import imaplib
import email

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "sihaowang4test" + ORG_EMAIL
FROM_PWD    = "sihaowang419"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

def my_unicode(s, encoding):
    if encoding:
        return str(s, encoding)
    else:
        return str(s)

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for message_id in range(latest_email_id,first_email_id - 1, -1):
            result, data = mail.fetch(str(message_id), "(RFC822)")

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1].decode('utf-8'))
                    email_subject = msg['subject']
                    email_from = msg['from']
                    raw_subject = email.header.decode_header(msg["subject"])
                    subject = my_unicode(raw_subject[0][0], raw_subject[0][1])
                    print('From : ' + email_from )
                    print('Subject : ' + subject)
                    print('Date:' + msg['Date']+'\n')
                    """
                    if msg.is_multipart():
                        for payload in msg.get_payload():
                            print(payload.get_payload())
                    else:
                        print(msg.get_payload())
                    """
                

    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    read_email_from_gmail()
