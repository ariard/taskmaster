# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    servitor.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:49:16 by ariard            #+#    #+#              #
#    Updated: 2017/04/23 18:27:03 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket
import configparser 

from debug import * 
from execute import *
from task_error import *
from statutor import *

import settings

num_threads = 0

def serviter(clientsocket, addr, server):

    while True:
        m = clientsocket.recv(1024)
        m = m.strip()
        cmd_lst = m.split(' ')
        if not m:
            print('That motherfucking client ' + str(addr[1]) + ' sent a SIGINT signal, stopping...')
            break

        elif cmd_lst[0] == 'exit' or cmd_lst[0] == 'quit':
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
