# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    taskmasterd.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/29 17:28:00 by ariard            #+#    #+#              #
#    Updated: 2017/05/08 20:11:05 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys
import signal
import time
import socket
import configparser
import threading
import logging

from daemonize import *
from server import *
from debug import *
from task_error import *
from syslogging import *
from serviter import num_threads

import settings


if __name__ == '__main__' :
    
    DG_init(0)
    if len(sys.argv) < 2:
        error_msg("usage : <config_file>")
    try:
        path_config = os.path.abspath(sys.argv[1])
    except FileNotFoundError:
        error_msg("No such configuration file")
    DG("start")
    daemonize()
    logging.basicConfig(format='%(asctime)s , %(levelname)s : %(message)s',filename='/tmp/.taskmasterdlog', level=logging.INFO)
    settings.init()
    server = Server(path_config)
    server.start_keeper()
#    server.start_dispatcher()
    logging.info("Taskmasterd server started")
    server.start_manager(server.config, server.list_progs)
    DG("after launch server")

    while True:
        global num_threads
        server.c, server.addr = server.ss.accept()
        DG('Connection received from : ' + str(server.addr))
        logging.info("Connection client %s from %s", server.addr[1], server.addr[0])
        server.c.recv(1024)
        server.c.send(str(num_threads).encode('utf-7'))
        server.start_serviter()
        num_threads += 1
        DG('debug: [' + str(num_threads) + '] threads are actually running')
    server.ss.close()
    DG("usual end")

#server.init #server.listen #server.deploy #server.exit
