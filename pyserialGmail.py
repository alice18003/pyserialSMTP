import serial
import smtplib
import datetime
import sys
import time
from email.mime.text import MIMEText
from email.utils import formatdate

timeMin = '09'
timeMax = '22'

smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.ehlo()
smtpobj.ehlo()
smtpobj.login("from_gmailaddress", sys.argv[1]) #sys.argv[1] is gmail's password

ser = serial.Serial('/dev/ttyS5', 9600)
while True:
    dt_now = datetime.datetime.now()
    data  = ser.read()
    value = int.from_bytes(data, 'big') - 48
    hour = de_now.strftime('%H')
    if value == 1:
        if hour >= timeMin and hour <= timeMax:
            ser.write(b"0");
        
            msg = MIMEText('Someone enter or exit')
            msg['subject'] = 'notification'
            msg['From'] = 'from_gmailaddress'
            msg['To'] = 'to_mailaddress'
            msg['Date'] = formatdate()
            smtpobj.sendmail("from_gmailaddress", "to_mailaddress", msg.as_string())
        else:
            ser.write(b"1");
        
            msg = MIMEText('WORNIG!!! Someone invaded!')
            msg['subject'] = 'WORNIG!!!'
            msg['From'] = 'from_gmailaddress'
            msg['To'] = 'to_mailaddress'
            msg['Date'] = formatdate()
            smtpobj.sendmail("from_gmailaddress", "to_mailaddress", msg.as_string())
    time.sleep(1)
smtpobj.close()
ser.close()
