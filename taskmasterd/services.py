# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    services.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/29 22:05:34 by ariard            #+#    #+#              #
#    Updated: 2017/04/30 15:43:40 by echo             ###   ########.fr        #
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
from report import report, manual_report
from extract import *

import settings

def services(clientsocket, addr, server):

    while True:
        m = clientsocket.recv(1024)
        logging.info(command(m, addr))
        dec = m.decode("utf-8")
        cmd_lst = dec.split(' ')
        try:
            if cmd_lst[1] == "all":
                cmd_lst = getAll(cmd_lst[0])
        except IndexError:
            pass
        
        if cmd_lst[0] == 'exit' or cmd_lst[0] == 'quit' or not m:
            logging.warning(flow(addr, 0))
            DG('exit request received from ' + str(addr[1]) + ' ... stopping')
            break

        elif cmd_lst[0] == 'start':
            for cmd in cmd_lst[1:]:
                try:
                    program = "program:" + cmd.strip('_0123456789')
                    server.config.get(program, "command")
                    logging.info(starting(cmd))
                    server.start_manager(server.config, [program])
                    clientsocket.send(b"\0")
                except configparser.NoSectionError:
                    DG("error no such program")
                    clientsocket.send(("taskmasterd: No such program " + cmd).encode("utf-8"))

        elif cmd_lst[0] == 'restart':
            for cmd in cmd_lst[1:]:
                try:
                    server.start_killer(settings.tab_process[cmd].pid)
                    program = "program:" + cmd.strip('_0123456789')
                    server.config.get(program, "command")
                    logging.info(restarting(cmd))
                    server.start_manager(server.config, [program])
                    clientsocket.send(b"\0")
                except configparser.NoSectionError:
                    DG("error no such program")
                    clientsocket.send(("taskmasterd: No such program " + cmd).encode("utf-8"))

        elif cmd_lst[0] == 'stop':
            for cmd in cmd_lst[1:]:
                if cmd in settings.tab_process:
                    logging.info(stopping(cmd))
                    server.start_killer(settings.tab_process[cmd].pid)
                    clientsocket.send(b"\0")
                else:
                    clientsocket.send(("taskmasterd: No such program " + cmd).encode("utf-8"))

        elif cmd_lst[0] == 'reload':
            server.config = configparser.ConfigParser()
            try:
                path_config = os.path.abspath(cmd_lst[1])
                logging.info(reloading(path_config))
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
            for cmd in cmd_lst[1:]:
                program = "program:" + cmd.strip('_0123456789')
                conf = getConfig(server.config, program)
                clientsocket.send(("[" + program + "]\n").encode("utf-8"))
                for line in conf:
                    DG(line)
                    clientsocket.send((line + "\n").encode("utf-8"))
                clientsocket.send("\n".encode("utf-8"))

        elif cmd_lst[0] == 'alert':
            manual_report(cmd_lst[1])

        elif cmd_lst[0] == 'shutdown':
            logging.warning("Shutting down taskmasterd...")
            for name in settings.tab_process:
                DG("pid is " + str(settings.tab_process[name].pid))
                server.start_killer(settings.tab_process[name].pid)
            try:
                os.remove("/tmp/.taskmasterd")
            except:
                pass
            clientsocket.send("Taskmasterd is shutdown".encode("utf-8"))
            os.kill(server.pid, signal.SIGKILL)
