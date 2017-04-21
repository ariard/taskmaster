# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reporter.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:45:20 by ariard            #+#    #+#              #
#    Updated: 2017/04/21 20:45:53 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from debug import *

def reporter():
    while 1:
        fifo = open("/tmp/fifo", "r")
        for line in fifo:
            starter = line.split(";")
#           DG("starter :" + line)
        fifo.close()
