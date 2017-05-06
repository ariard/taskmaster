# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    client.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ataguiro <ataguiro@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/19 23:52:12 by ataguiro          #+#    #+#              #
#    Updated: 2017/05/06 16:24:46 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket
import readline
import os
import sys
import getpass

from debug import *
from attach import *

# Line editing inits

readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')
readline.parse_and_bind('Meta-h: backward-kill-word')
readline.parse_and_bind('"\C-u": universal-argument')
readline.parse_and_bind('set horizontal-scroll-mode On')

# host and port config

host = 'localhost'
port = 4232

def header():
	print("  _______        _                        _            ")
	print(" |__   __|      | |                      | |           ")
	print("    | | __ _ ___| | ___ __ ___   __ _ ___| |_ ___ _ __ ")
	print("    | | (_| \__ \   <| | | | | | (_| \__ \ ||  __/ |   ")
	print("    |_|\__,_|___/_|\_\_| |_| |_|\__,_|___/\__\___|_|   ")
	print("                            by ariard, ataguiro        ")
	print("")

def welcome(cnum):
	header()
	print("----------------------------------------------------------------")
	print("-- Available commands : help, start [command], restart [command]")
	print("--                      status [command], stop, exit            ")
	print("--                      reload [file]                           ")
	print("-- Server running adress : ", host                               )
	print("-- Listening on port : ", port                                   )
	print("-- You are the client number : ", cnum                           )
	print("----------------------------------------------------------------")

def line_is_command(line):
    if (line == "exit" or line == "help" or "start" in line or "restart" in line or "status" in line \
        or "stop" in line or "reload" in line or line == "shutdown" or "config" in line or "alert" in line \
        or "alert" in line or "attach" in line):
        return 1
    return 0

def wait_answer(sc):
    DG("waiting for answer")
    while True:
        try:
            reply = sc.recv(1024).decode('utf-8')
        except ConnectionResetError:
            raise ConnectionResetError
        if len(reply) > 0 and reply != '\r':
            print(reply.rstrip("\n\r"))
        if "\r" in reply:
            break

def prompt(sc):
    DG("Prompt good")
    while True:
        line = input("\033[1;32mtaskmaster>\033[0m ")
        if (line_is_command(line)):
            if "reload" in line:
                sp = line.split()
                if len(sp) == 2:
                    sp[1] = os.path.abspath(sp[1])
                    line = sp[0] + " " + sp[1]
            sc.send(line.encode('utf-8'))             
            if (line == 'exit'):
                break
            elif "attach" in line:
                attach_mode(sc)
            else:
                try:
                    wait_answer(sc)
                except ConnectionResetError:
                    print("Broken connection, exiting")
                    break
        elif (line == 'help'):
            print ("exit, start <prog>, restart <prog>, status <prog>, stop <prog>, reload <file>, help")
        else:
            print("taskmaster:", line, ": command not found")

def launch(host, port):
    DG_init() 
#    signal.signal(signal.SIGINT, )
    sc = socket.socket()
    print("Trying to connect", host, "on port", port," ...")
    sc.connect((host, port))
    sc.send(("\r\n").encode('utf-8'))
    DG("num client ok")
    cnum = (sc.recv(1024)).decode('utf-8')
    welcome(cnum)
    while True:
        psswd = getpass.getpass()
        if len(psswd) == 0:
            psswd = "\r\n"
        sc.send(psswd.encode('utf-8'))
        answer = sc.recv(1024).decode('utf-8')
        if answer == "valid":
            prompt(sc)
            sys.exit(0)
        print(answer)
        if "deconnecting" in answer:
            sys.exit(0)

if __name__ == '__main__':
    launch(host, port)
