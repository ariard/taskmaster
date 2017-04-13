# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    taskmasterd.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/04 21:57:30 by ariard            #+#    #+#              #
#    Updated: 2017/04/13 15:42:00 by ataguiro         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import os
import sys
import signal
import time
import socket
import configparser

from thread import *
from daemonize import *
from server import *
from monitor import *
from log import *
#from debug import *
##pb execution sur ma machine je commente temporairement

def new_client(cs, ad):
    while True:
        m = cs.recv(1024)
        print (ad, '> ', m)
        #m = raw_input('> ')
        #cs.send(m + "\n")
    cs.close()

if __name__ == '__main__' :
    
#    DG_init()
    if len(sys.argv) < 2:
        print("usage : <config_file>")
        exit(-1)

#    DG("start")
    daemonize()
    log = log()
    config = configparser.ConfigParser()
    config.read_file(open('/Users/echo/taskmaster/taskmasterd/master.config'))
    monitor = Monitor(config, (config.sections()))
    monitor.launch_all()
    host = "localhost"
    port = 2121
    s = socket.socket()
    try:
        s.bind((host, port))
    except:
        print("error bind")
    s.listen(5)
    while True:
        cs, ad = s.accept()
        start_new_thread(new_client, (cs, ad))
        print('Connection received from : ', ad)
    s.close()
#    server.init
#    server = Server('localhost', 2121)
#    server.launch
#    server.accept()
#    server.receive()
#    DG("usual end")


#server.init #server.listen #server.deploy #server.exit
