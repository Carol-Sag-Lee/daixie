# -*- coding: utf-8 -*-


from os import makedirs
from os.path import splitext, join, isdir, sep, altsep
from subprocess import call
from re import compile

from daixie import app

from smtplib import *
from email.mime.text import MIMEText
import base64, hashlib 

def pretty_email(email):
    postfix = email.split('@')[1]
    name = email.split('@')[0]
    str_list = list(name)
    length = len(str_list)
    for index in range(0, length):
        if not index in (0, length-1):
            str_list[index] = '*'
    return ''.join(str_list) + '@' + postfix


#测试机器
def send_email(to,title,body):
    fromer = 'Routh@Routh.com'
    mail_host = 'software.nju.edu.cn'
    mail_user = 'mf1332041@software.nju.edu.cn' 
    mail_pass = '**********'
    msg = MIMEText(body,_subtype='html',_charset='utf-8') 
    msg['Subject'] = title
    msg['From'] = fromer
    msg['To'] = to
    try:
        smtp = SMTP()
        smtp.connect(mail_host)
        smtp.login(mail_user, mail_pass)
        smtp.sendmail(fromer, to, msg.as_string())
        smtp.close()
        return True
    except Exception,e:
        print str(e)
        return False


#线上机器，将2去掉，把测试机器改成2
def send_email2(to,title,body):
    fromer = 'xiaoma@offerduoduo.com'
    mail_host = '127.0.0.1'
    #mail_user = 'xiaoma' 
    #mail_pass = ''
    msg = MIMEText(body,_subtype='html',_charset='utf-8') 
    msg['Subject'] = title
    msg['From'] = fromer
    msg['To'] = to
    try:
        smtp = SMTP()
        smtp.connect(mail_host)
        #smtp.login(mail_user, mail_pass)
        smtp.sendmail(fromer, to, msg.as_string())
        smtp.close()
        return True
    except Exception,e:
        print str(e)
        return False 