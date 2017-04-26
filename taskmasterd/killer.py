# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    killer.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:54:34 by ariard            #+#    #+#              #
#    Updated: 2017/04/27 00:02:05 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import signal
import time

from task_signal import *

import settings

def getSignal(stopsignal):
    signals = ["TERM", signal.SIGTERM, "HUP", signal.SIGHUP, "INT", signal.SIGINT, \
        "QUIT", signal.SIGQUIT, "KILL", signal.SIGKILL, "USR1", signal.SIGUSR1, \
        "USR2", signal.SIGUSR2] 

    a = 0
    DG(stopsignal)
    for i in signals:
        
        
        if a == 1:
            return i
        if stopsignal == i:

            DG(i)
            a = 1

def killer(pid, null):

    name = settings.pid2name[pid]
    father = settings.tab_process[name].father
    signal = getSignal(settings.tab_prog[father].stopsignal)
    if settings.tab_process[name].status != "STARTING" and setttings.tab_process[name].status != "STOPPING":
        return 1
    settings.tab_process[name].status = "STOPPING"
    os.kill(pid, signal)
    time.sleep(settings.tab_prog[father].stopwaitsecs)
    if settings.tab_process[name].status != "STOPPED":
        os.kill(pid, signal.SIGKILL)
