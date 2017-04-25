# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    serviter.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:49:16 by ariard            #+#    #+#              #
#    Updated: 2017/04/24 23:08:19 by echo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket
import configparser 
import logging

from debug import * 
from execute import *
from task_error import *
from statutor import *
from syslogging import *
from report import report

import settings

num_threads = 0
LOGFILE='logs'

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename=LOGFILE, filemode='a')

def serviter(clientsocket, addr, server):
    
    while True:
        m = clientsocket.recv(1024)        
        #report(addr, "ls", "originadam@gmail.com")
        m = m.strip()
        cmd_lst = m.split(b' ')
        if m:
            print(m + b'\n')
            logging.info(command(m.decode('utf-8'), addr))
        elif cmd_lst[0] == 'exit' or cmd_lst[0] == 'quit' or not m:
            logging.warning(flow(addr, 0))
            print('exit request received from ' + str(addr[1]) + ' ... stopping')
            break

        elif cmd_lst[0] == 'start' or cmd_lst[0] == 'restart':
            server.start_manager(server.config, cmd_lst[1:])

        elif cmd_lst[0] == 'stop':
            if cmd_lst[1] in settings.tab_process:
                server.start_killer(settings.tab_process[cmd_lst[1]])
            else:
                error_msg("No such process " + cmd_lst[1])

        elif cmd_lst[0] == 'reload':
            server.config = configparser.ConfigParser()
            try:
                server.config.read_file(open(cmd_lst[1]))
            except FileNotFoundError:
                error_msg("No such configuration file" + cmd_lst[1])
            server.config.read_file(open(path))
            server.list_progs = extractProg(server.config.sections())
            server.start_manager(server.config, server.list_progs)

        elif cmd_lst[0] == 'status':
            tab = getStatus()
            cliensocket.send(tab + "\n")

    global num_threads
    num_threads -= 1
    print('debug: [' + str(num_threads) + '] threads are actually running')
    clientsocket.close()
