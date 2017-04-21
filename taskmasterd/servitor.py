# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    servitor.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:49:16 by ariard            #+#    #+#              #
#    Updated: 2017/04/21 20:52:17 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket
import configparser 

from debug import * 
from execute import *

num_threads = 0

def new_client(clientsocket, addr, monitor)
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

        elif cmd_lst[0] == 'start' or cmd_lst[0] == 'restart'
            for i in cmd_lst[1:]:
               program = Program(monitor.config, i)        
                while program.numprocs > 0:
                    launcher(program)
                    program.numprocs -= 1

        elif cmd_lst[0] == 'stop' 
            for i in cmd_list[1:]:
                running_program = table_prog[i]
                while running_program.numprocs > 0:
                   monitor.start_killer(running_program)
                   running_program.numprocs -= 1

        elif cmd_lst[0] == 'reload'
            config = configparser.ConfigParser()
            config.read_file(open(cmd_lst[1]))
            monitor.config = config 
            monitor.list_programs = list()
            monitor.list_programs.extend(config.sections())
            monitor.start_configurator()

#        elif cmd_lst[0] == 'status'    
            

        #m = raw_input('> ')
        #clientsocket.send(m + "\n")
    global num_threads
    num_threads -= 1
    print('debug: [' + str(num_threads) + '] threads are actually running')
    clientsocket.close()
