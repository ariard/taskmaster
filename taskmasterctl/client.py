# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    client.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ataguiro <ataguiro@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/19 23:52:12 by ataguiro          #+#    #+#              #
#    Updated: 2017/04/28 21:06:40 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket
import readline
import os

# Line editing inits

readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')
readline.parse_and_bind('Meta-h: backward-kill-word')
readline.parse_and_bind('"\C-u": universal-argument')
readline.parse_and_bind('set horizontal-scroll-mode On')

# host and port config

host = 'localhost'
port = 4242

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
    or "stop" in line or "reload" in line or line == "shutdown"):
        return 1
    return 0

def send_to_server(line, sc):
	sc.send(line.encode('utf8'))

def wait_answer(sc):
	reply = sc.recv(1024)
	print(">> " + str(reply.decode('utf-8')))

def prompt(sc):
	while True:
		line = input("\033[1;32mtaskmaster>\033[0m ")
		if (line_is_command(line)):
			if "reload" in line:
				sp = line.split()
				if len(sp) == 2:
					sp[1] = os.path.abspath(sp[1])
					line = sp[0] + " " + sp[1]
			send_to_server(line, sc)
			if (line == 'exit'):
				break
		elif (line == 'help'):
			print ("exit, start prog, restart prog, status prog, stop prog, reload file, help")
		else:
			print("taskmaster:", line, ": command not found")
		wait_answer(sc)

def launch(host, port):
	sc = socket.socket()
	print("Trying to connect", host, "on port", port," ...")
	sc.connect((host, port))
	cnum = sc.recv(1024)
	cnum = cnum.decode('utf8')
	welcome(cnum)
	prompt(sc)

if __name__ == '__main__':
	launch(host, port)
