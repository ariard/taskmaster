# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    log.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/07 04:12:39 by ariard            #+#    #+#              #
#    Updated: 2017/04/15 20:54:18 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import time

class log:
    def __init__(self):
        self.logfile = open("/tmp/logfile" + str(os.getpid()), "w+")
        self.logfile.write(str(os.getpid()))
        self.logfile.write("Session begins at :" + str(time.localtime()) + "\n")

    def update(self, event):
        self.logfile.write(str(os.getpid()))
        self.logfile.write(event)
