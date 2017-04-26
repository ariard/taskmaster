# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    syslogging.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: echo <marvin@42.fr>                        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/22 14:53:30 by echo              #+#    #+#              #
#    Updated: 2017/04/26 20:06:26 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def command(m, addr):
	return ("received command: '" + str(m) + "' from " + str(addr[0]) + ":" + str(addr[1]))

def flow(addr, dig):
	return ("'" + str(addr[1]) + "' " + ("joined " if dig else "left ") + "from '" + str(addr[0]) + "'")

def crash(addr, name):
	return ("'" + str(name) + "' program crashed")
