#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


mail = MIMEMultipart() 
#发送邮件服务器
smtpserver = 'XXX.XXX.com'
#发送邮箱用户名和密码
user = 'XXX@XXX.com'
password = 'PASSWD'
#收件人，多个收件人用逗号隔开
username_recv = 'XXX@XXX.com,XXX@XXX.com'
 
#邮件正文内容
mail.attach(MIMEText('''
请检查磁盘情况

'''))
mail['From'] = Header(user)
mail['To'] = Header(username_recv)
subject = sys.argv[1]
mail['Subject'] = Header(subject) 
smtp = smtplib.SMTP()
smtp.connect(smtpserver,25)
smtp.login(user,password)
smtp.sendmail(user,username_recv.split(','),mail.as_string())
smtp.quit()
