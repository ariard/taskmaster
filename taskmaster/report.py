# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    report.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: echo <marvin@42.fr>                        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/24 22:34:44 by echo              #+#    #+#              #
#    Updated: 2017/04/30 16:26:45 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
import smtplib

from email.mime.text import MIMEText

def report(name):
    me = 'taskmaster@42.fr'
    you = 'ataguiro@student.42.fr'

    now = time.strftime("%c")
    msg = MIMEText(str(now) + ', program "' + name + '" crashed !')

    msg['Subject'] = '[CRASH] Program [' + name  + '] crashed !'
    msg['From'] = me
    msg['To'] = you

    try:
        s = smtplib.SMTP('smtp.free.fr')
        s.sendmail(me, you, msg.as_string())
        s.quit()
    except:
        pass

def manual_report(msg):
    me = 'taskmasterd@42.fr'
    you = "originadam@gmail.com"

    now = time.strftime("%c")
    msg = MIMEText(str(now) + ".")  
  
    msg['Subject'] = '[MANUAL ALERT]'
    msg['From'] = 'Taskmaster 42'
    msg['To'] = you

    s = smtplib.SMTP('smtp.free.fr')
    s.sendmail(me, you, msg.as_string())
    s.quit()
