# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    keeper.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/22 00:35:20 by ariard            #+#    #+#              #
#    Updated: 2017/04/23 19:05:40 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from debug import *
from launcher import * 
from task_signal import *

import settings

def keeper():

    while 1 :
        while len(settings.queue_pid) > 1:
            pid = settings.queue_pid[0]
            exitcode = settings.queue_pid[1]
            name_prog = settings.tab_process[pid].father
            program = settings.tab_prog[name_prog]
            if ((exitcode not in program.exitcodes and program.autorestart == "unexpected") \
                or (program.autorestart == "true")) and settings.tab_process[pid].status == "RUNNING":
                if settings.tab_process[pid].retries > 0:
                    settings.tab_process[pid].retries -= 1
                    launcher(program, name_prog, settings.tab_process[pid].num, settings.tab_process[pid].retries)
            elif tab_process[pid].status == "RUNNING":
                tab_process[pid].status = "EXITED"
            elif tab_process[pid].status == "STARTING":
                if tab_process[pid].retries > 0:
                    settings.tab_process[pid].retries -= 1 
                    launcher(program, name_prog, settings.tab_process[pid].num, settings.tab_process[pid].retries)
            settings.queue_pid.pop(0)
            settings.queue_pid.pop(0)
        time.sleep(1)
