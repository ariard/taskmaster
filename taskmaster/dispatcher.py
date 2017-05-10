# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    dispatcher.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/05/08 15:53:31 by ariard            #+#    #+#              #
#    Updated: 2017/05/10 16:17:11 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import time
from select import select

import taskmaster.settings as settings

from taskmaster.debug import *


def dispatcher():

    DG("launching dispatcher")
    while 1: 
        my_fds = list()
        for fd in settings.fds:
            if settings.attach_process and settings.tab_process[settings.attach_process].process_fd[1] != fd and \
            settings.tab_process[settings.attach_process].process_fd[2] != fd:
                my_fds.append(fd)
            elif settings.attach_process == 0:
                DG("had fd")
                my_fds.append(fd)
        if len(my_fds) > 0:
            rfds, wfds, xfds = select(my_fds, [], [])

        for fd in my_fds:
            if fd in rfds:
                data = os.read(fd, 1024) 
                if data:
                    filename = settings.fd2realfile[fd]
                    tmp_fd = os.open(filename, os.O_CREAT | os.O_WRONLY | os.O_APPEND)
                    os.write(tmp_fd, data)
                    os.close(tmp_fd)

        time.sleep(1)
