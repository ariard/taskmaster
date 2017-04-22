# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    server.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/06 23:56:10 by ariard            #+#    #+#              #
#    Updated: 2017/04/22 19:03:40 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import time
import socket
import threading
import configparser 
import os
import signal

from debug import *
from task_signal import *
from task_error import *

from manager import manager
from keeper import keeper
from watcher import watcher
from serviter import serviter
from killer import killer

def extractProg(list_sections):
    prog = list()
    DG("sections " + str(list_sections))
    for sections in list_sections:
        if sections[0:7] == "program":
            prog.append(sections)
    return (prog)

class Server:
    def __init__(self, path):
        self.config = configparser.ConfigParser()
        self.config.read(path)
        try:
            self.port = int(self.config.get('server', 'port'))
        except configparser.NoSectionError:
            error_msg("No section on server")
        except configparser.DuplicateSectionError: 
            error_msg("Duplicate section on server") 
        self.host = ''
        self.ss = socket.socket()
        self.c = None
        self.addr = None
        try:
            self.ss.bind((self.host, self.port))
        except:
            error_msg("Socket already in use")
        self.ss.listen(5)
        self.list_progs = extractProg(self.config.sections())
        signal.signal(signal.SIGCHLD, check_exit) 
        DG("Server started and waiting for clients...")

    def start_manager(self, config, list_progs):
        DG("start manager")
        t = threading.Thread(target=manager, args=(config, list_progs, self))
        t.start()
    
    def start_keeper(self):
        t = threading.Thread(target=keeper)
        t.start()

    def start_watcher(self):
        t = threading.Thread(target=watcher)
        t.start()

    def start_serviter(self):
        t = threading.Thread(target=serviter, args=(self.c[:], self.addr[:], self))
        t.start()

    def start_killer(self, pid):
        t = threading.Thread(target=killer, args=(pid))
        t.start()
