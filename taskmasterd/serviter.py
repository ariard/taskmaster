# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    servitor.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:49:16 by ariard            #+#    #+#              #
#    Updated: 2017/04/22 19:44:15 by ariard           ###   ########.fr        #
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
    table_prog = settings.table_prog
    table_process = settings.table_process 
    prog_to_pid = settings.prog_to_pid

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
            for name_prog in cmd_list[1:]:
                numprocs = table_prog[name_prog].numprocs[:] 
                while numprocs > 0:
                   server.start_killer(prog_to_pid[name_prog])
                   prog_to_pid[name_prog] = prog_to_pid[name_prog][1:]
                   numprocs -= 1

        elif cmd_lst[0] == 'reload':
            server.config = configparser.ConfigParser()
            try:
                server.config.read_file(open(cmd_lst[1]))
            except FileNotFoundError:
                error_msg("No such configuration file")
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
