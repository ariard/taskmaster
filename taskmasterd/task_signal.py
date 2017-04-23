# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    task_signal.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/15 18:50:45 by ariard            #+#    #+#              #
#    Updated: 2017/04/23 18:17:27 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import signal

from debug import *

import settings

def check_exit(number, frame):

    while True:
        try:
            pid = os.waitpid(0, 0)
            settings.queue_pid += pid;
#            DG("queue pid is:" + str(queue_pid))
        except:
            break
