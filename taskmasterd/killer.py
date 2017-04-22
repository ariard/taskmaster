# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    killer.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:54:34 by ariard            #+#    #+#              #
#    Updated: 2017/04/22 01:50:23 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import signal

from task_signal import *

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

def killer(pid):
    global queue_pid
    global table_prog
    global table_process

    signal = get_signal(table_prog[table_process[pid][1]].stopsignal)
    os.kill(pid, signal)
    time.sleep(table_prog[table_process[pid][1]].stopwaits)
    if pid not in queue_pid:
        os.kill(pid, signal.SIGKILL)
