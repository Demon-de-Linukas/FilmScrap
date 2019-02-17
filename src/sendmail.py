# -*- coding: utf-8 -*-
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header
from src.film import get_film_list_zkm


def generate_html(all_film):
    i=1
    html=''
    for film in all_film:
        msg = """
        <p style="font-size:110%">{}.</p>
        <p ><a href="{}"><u><b>{}</b></u></a></p>
        <p><img src="{}"></p>
        <p><strong>--------------------------------------------</strong></p>
        """
        html+='\n%s'%msg.format(i,all_film[film][0]['href'],film,all_film[film][0]['img_ref'])
        i+=1
    return html


def send_mail(parsed_html):
    sender = ''
    receivers = ['']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    mail_host="smtp.gmail.com"#aspmx.l.google.com"  #设置服务器
    mail_user=""    #用户名
    mail_pass=""   #口令



    mail_msg =parsed_html

    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = Header("ZKM Films", 'utf-8')
    message['To'] = Header("The me", 'utf-8')

    subject = 'Films in ZKM of Week %s'%(time.strftime("%W"))
    message['Subject'] = Header(subject, 'utf-8')


    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 587)    # 25 为 SMTP 端口号
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.ehlo()
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print(
        "邮件发送成功")
        return True
    except smtplib.SMTPException:
        print(
        "Error: 无法发送邮件")
        return False