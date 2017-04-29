# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    serviter.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:49:16 by ariard            #+#    #+#              #
#    Updated: 2017/04/29 20:13:48 by ariard           ###   ########.fr        #
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
            DG('exit request received from ' + str(addr[1]) + ' ... stopping')
            break

        elif cmd_lst[0] == 'start':
            try:
                program = "program:" + cmd_lst[1].strip('_0123456789')
                server.config.get(program, "command")
                server.start_manager(server.config, [program])
                clientsocket.send(b"\0")
            except configparser.NoSectionError:
                DG("error no such program")
                clientsocket.send(("taskmasterd: No such program " + cmd_lst[1]).encode("utf-8"))

        elif cmd_lst[0] == 'restart':
            try:
                server.start_killer(settings.tab_process[cmd_lst[1]].pid)
                program = "program:" + cmd_lst[1].strip('_0123456789')
                server.config.get(program, "command")
                server.start_manager(server.config, [program])
                clientsocket.send(b"\0")
            except configparser.NoSectionError:
                DG("error no such program")
                clientsocket.send(("taskmasterd: No such program " + cmd_lst[1]).encode("utf-8"))
                

        elif cmd_lst[0] == 'stop':
            if cmd_lst[1] in settings.tab_process:
                server.start_killer(settings.tab_process[cmd_lst[1]].pid)
                clientsocket.send(b"\0")
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
                clientsocket.send(b"\0")
            except Error :
                clientsocket.send(("taskmasterd: No such program " + cmd_lst[1]).encode("utf-8"))

        elif cmd_lst[0] == 'status':
            tab = getStatus()
            for line in tab:
                DG(line)
                clientsocket.send(line.encode("utf-8"))

        elif cmd_lst[0] == 'config':
            program = "program:" + cmd_lst[1].strip('_0123456789')
            conf = getConfig(server.config, program)
            for line in conf:
                DG(line)
                clientsocket.send((line + "\n").encode("utf-8"))

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

        
    global num_threads
    num_threads -= 1
    DG('debug: [' + str(num_threads) + '] threads are actually running')
    clientsocket.close()
