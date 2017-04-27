# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    serviter.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:49:16 by ariard            #+#    #+#              #
#    Updated: 2017/04/27 18:23:28 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket
import configparser 
import logging
import signal

from debug import * 
from execute import *
from task_error import *
from statutor import *
from syslogging import *
from report import report
from extract import *

import settings

num_threads = 0
LOGFILE='logs'

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename=LOGFILE, filemode='a')

def serviter(clientsocket, addr, server):
    
    while True:
        m = clientsocket.recv(1024)        
        #report(addr, "ls", "originadam@gmail.com")
        dec = m.decode("utf-8")
        cmd_lst = dec.split(' ')
#        DG("cmd_lst[0] + " + cmd_lst[0])
#        try:
#            DG("cmd_lst[1] + " + cmd_lst[1])
#        except:
#            pass
#        if m:
#            print(m + b'\n')
#            logging.info(command(m.decode('utf-8'), addr))


        if cmd_lst[0] == 'exit' or cmd_lst[0] == 'quit' or not m:
            logging.warning(flow(addr, 0))
            print('exit request received from ' + str(addr[1]) + ' ... stopping')
            break

        elif cmd_lst[0] == 'start':
            try:
                program = "program:" + cmd_lst[1].strip('_0123456789')
                server.config.get(program, "command")
                server.start_manager(server.config, [program])
            except configparser.NoSectionError:
                DG("error no such program")
                clientsocket.send(("taskmasterd: No such program " + cmd_lst[1]).encode("utf-8"))

        elif cmd_lst[0] == 'restart':
            try:
                server.start_killer(settings.tab_process[cmd_lst[1]].pid)
                program = "program:" + cmd_lst[1].strip('_0123456789')
                server.config.get(program, "command")
                server.start_manager(server.config, [program])
            except configparser.NoSectionError:
                DG("error no such program")
                clientsocket.send(("taskmasterd: No such program " + cmd_lst[1]).encode("utf-8"))
                

        elif cmd_lst[0] == 'stop':
            if cmd_lst[1] in settings.tab_process:
                server.start_killer(settings.tab_process[cmd_lst[1]].pid)
            else:
                clientsocket.send(("taskmasterd: No such program " + cmd_lst[1]).encode("utf-8"))

        elif cmd_lst[0] == 'reload':
            DG("reload")
            DG(cmd_lst[1])
            server.config = configparser.ConfigParser()
            try:
                path_config = os.path.abspath(cmd_lst[1])
                server.config.read(path_config)
                server.list_progs = extractProg(server.config.sections())
                server.start_manager(server.config, server.list_progs)
            except Error :
                clientsocket.send(("taskmasterd: No such program " + cmd_lst[1]).encode("utf-8"))

        elif cmd_lst[0] == 'status':
            tab = getStatus()
            DG(str(tab))
            clientsocket.send(str(tab).encode("utf-8"))

        elif cmd_lst[0] == 'config':
            program = "program:" + cmd_lst[1].strip('_0123456789')
            config_program = server.config.options("program:" + program)
            clientsocket.send(config_program.encode("utf-8"))

        elif cmd_lst[0] == 'alert':
            pass
               

        elif cmd_lst[0] == 'shutdown':
            for name in settings.tab_process:
                DG("pid is " + str(settings.tab_process[name].pid))
                server.start_killer(settings.tab_process[name].pid)
            try:
                os.remove("/tmp/.taskmasterd")
            except:
                pass
            clientsocket.send("Taskmasterd is shutdown".encode("utf-8"))
            os.kill(server.pid, signal.SIGKILL)
            sys.exit(-1)

    global num_threads
    num_threads -= 1
    print('debug: [' + str(num_threads) + '] threads are actually running')
    clientsocket.close()
