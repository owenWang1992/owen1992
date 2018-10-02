#-*- encoding: utf-8 -*-
#-*- encoding: gbk -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import smtplib
import time
import imaplib
import email
import base64
import os

FROM_EMAIL  = "sihaowang4test@gmail.com"
FROM_EMAIL1  = "wshwjh@gmail.com"
IMAP_SERVER = "imap.gmail.com"
IMAP_SERVER2 = "outlook.office365.com"
IMAP_PORT   = 993

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

def saveHtmlFile(str, filename):
    Html_file= open(filename,"w")
    Html_file.write(str)
    Html_file.close()

def openMessage(messageid):
    htmlFileName = "file://" + os.path.join((os.path.split(__file__))[0], messageid + ".html")
    openHtmlFile(htmlFileName)


def openHtmlFile(filename):
    options = webdriver.ChromeOptions()
    #options.add_argument("--incognito")
    #options.add_argument('--ignore-certificate-errors')
    #options.add_argument('--ignore-ssl-errors')
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get(filename)
    time.sleep(15)
    driver.close()
    driver.quit()


def create_mail(imap_server, username, password):
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(username, password)
    return mail

def read_email_from_gmail():
    try:
        username = FROM_EMAIL1
        pwd= input("Password for " + username + ": ")
        mail = create_mail(IMAP_SERVER, username, pwd)
        mail.select('inbox')

        type, data = mail.search(None, 'FROM', '"Experian"')
        #type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = list(map(lambda x: str(int(x)), mail_ids.split()))
        mailCount = 0
        for message_id in reversed(id_list):
            mailCount = mailCount + 1
            if mailCount > 10:
                break
            result, data = mail.fetch(message_id, "(RFC822)")

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1].decode('utf-8'))
                    email_subject = msg['subject']
                    email_from = msg['from']
                    raw_subject = email.header.decode_header(msg["subject"])
                    subject = my_unicode(raw_subject[0][0], raw_subject[0][1])
                    print(message_id)
                    print('From : ' + email_from )
                    print('Subject : ' + subject)
                    print('Date:' + msg['Date']+'\n')
                    for part in msg.walk():
                        if part.get_content_type() == 'text/html':
                            saveHtmlFile(part.get_payload(), str(int(message_id)) + ".html")
                            #print(part.get_payload())
                            break

        if len(id_list):
            messageToOpen = input("Select messageid to open:")
            if messageToOpen in id_list:
                openMessage(messageToOpen)

    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    read_email_from_gmail()
