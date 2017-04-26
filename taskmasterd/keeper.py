# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    keeper.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/22 00:35:20 by ariard            #+#    #+#              #
#    Updated: 2017/04/27 00:01:24 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from debug import *
from launcher import * 
from task_signal import *
from watcher import *

import settings

def keeper():

    while 1 :
        while len(settings.queue_pid) > 1:
            pid = settings.queue_pid[0]
            name = settings.pid2name[pid]
            exitcode = settings.queue_pid[1]
            name_prog = settings.tab_process[name].father
            program = settings.tab_prog[name_prog]
            watcher(name)
            DG(str(program.exitcodes))
            if ((exitcode not in program.exitcodes and program.autorestart == "unexpected") \
                or (program.autorestart == "true")) and settings.tab_process[name].status == "RUNNING" \
                and settings.tab_process[name].retries > 0:
                if settings.tab_process[name].retries > 0:
                    settings.tab_process[name].retries -= 1
                    launcher(program, name_prog, settings.tab_process[name].num, settings.tab_process[name].retries)
            elif settings.tab_process[name].status == "RUNNING":
                settings.tab_process[name].status = "EXITED"
            elif settings.tab_process[name].status == "STOPPING":
                settings.tab_process[name].status = "STOPPED"

            elif settings.tab_process[name].status == "STARTING":
                if settings.tab_process[name].retries > 0:
                    settings.tab_process[name].retries -= 1 
                    launcher(program, name_prog, settings.tab_process[name].num, settings.tab_process[name].retries)
                elif settings.tab_process[name].retries == 0:
                    settings.tab_process[name] = "FATAL"
            settings.queue_pid.pop(0)
            settings.queue_pid.pop(0)
        time.sleep(1)
