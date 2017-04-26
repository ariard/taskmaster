# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    killer.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:54:34 by ariard            #+#    #+#              #
#    Updated: 2017/04/26 22:26:12 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import signal

from task_signal import *

import settings

def getSignal(stopsignal):
    signals = ["TERM", signal.TERM, "HUP", signal.HUP, "INT", signal.INT, \
        "QUIT", signal.QUIT, "KILL", signal.KILL, "USR1", signal.USR1, \
        "USR2", signal.USR2] 

    a = 0
    for i in signals:
        if a == 0:
            return i
        if stopsignal == i:
            a == 1

def killer(named_process):

    father = settings.tab_process[named_process]
    pid = settings.tab_process[named_process].pid
    signal = get_signal(settings.tab_prog[father].stopsignal)
    os.kill(pid, signal)
    time.sleep(settings.tab_prog[father].stopwaits)
    if pid not in queue_pid:
        os.kill(pid, signal.SIGKILL)
