# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    task_signal.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/15 18:50:45 by ariard            #+#    #+#              #
#    Updated: 2017/04/22 20:00:53 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import signal

from debug import *

import settings

def check_exit(number, frame):
    queue_pid = settings.queue_pid

    while True:
        try:
            pid = os.waitpid(0, 0)
            queue_pid += pid;
#            DG("queue pid is:" + str(queue_pid))
        except:
            break
