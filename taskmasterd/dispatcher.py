# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    dispatcher.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/05/08 15:53:31 by ariard            #+#    #+#              #
#    Updated: 2017/05/08 19:59:44 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import time
from select import select

from debug import *

import settings

def dispatcher():

    DG("launching dispatcher")
    while 1: 
        DG("my settings fds" + str(settings.fds))
        my_fds = list()
        for fd in settings.fds:
            my_fds.append(fd)
        DG("before select")
        DG("my fds is " + str(my_fds))
        if len(my_fds) > 0:
            rfds, wfds, xfds = select(my_fds, [], [])

        DG("still")
        for fd in my_fds:
            if fd in rfds:
                DG("reading data from fd")
                data = os.read(fd, 1024) 
                if data:
                    filename = settings.fd2realfile[fd]
                    tmp_fd = os.open(filename, os.O_CREAT | os.O_WRONLY | os.O_APPEND)
                    os.write(tmp_fd, data)
                    os.close(tmp_fd)

        time.sleep(2)
