# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    syslogging.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: echo <marvin@42.fr>                        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/22 14:53:30 by echo              #+#    #+#              #
#    Updated: 2017/04/30 15:11:29 by echo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def command(m, addr):
	return ("received command: '" + str(m) + "' from " + str(addr[0]) + ":" + str(addr[1]))

def flow(addr, dig):
	return ("'" + str(addr[1]) + "' " + ("joined " if dig else "left ") + "from '" + str(addr[0]) + "'")

def starting(name):
	return ("starting program : '" + str(name) + "'")

def restarting(name):
	return ("restarting program : '" + str(name) + "'")

def stopping(name):
	return ("stopping program : '" + str(name) + "'")

def reloading(path):
	return ("reloading config file : " + str(path))
