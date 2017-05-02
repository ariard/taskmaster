# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    keeper.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/22 00:35:20 by ariard            #+#    #+#              #
#    Updated: 2017/05/02 20:42:11 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from debug import *
from launcher import * 
from task_signal import *
from watcher import *
from report import report

import settings
import logging

def guardian(pid):

    for process in settings.tab_process:
        if pid == settings.tab_process[process].pid:
            settings.tab_process[process].status = "UNKNOWN"

def keeper():

    while 1 :
#        DG("wake up with " + str(len(settings.queue_pid)))
        while len(settings.queue_pid) > 1:
            pid = settings.queue_pid[0]
            DG("da pid is: " + str(pid))
            try:
                name = settings.pid2name[pid]
                exitcode = settings.queue_pid[1]
                name_prog = settings.tab_process[name].father
                program = settings.tab_prog[name_prog]
                watcher(name)
                watcher_backoff(name)
                if ((exitcode not in program.exitcodes and program.autorestart == "unexpected") \
                    or (program.autorestart == "true")) and settings.tab_process[name].status == "RUNNING":
#                logging.critical(str(name_prog) + "crashed with exit code " + str(exitcode))
#                report(name_prog)
                    start_launcher(program, name, name_prog, program.startretries)
                elif settings.tab_process[name].status == "RUNNING":
                    settings.tab_process[name].status = "EXITED"
                elif settings.tab_process[name].status == "STOPPING":
                    settings.tab_process[name].status = "STOPPED"

                elif settings.tab_process[name].status == "BACKOFF":
                    if settings.tab_process[name].retries > 0:
                        DG("process put backoff : " + name)
                        settings.tab_process[name].retries -= 1 
                        start_launcher(program, name, name_prog, settings.tab_process[name].retries)
                    elif settings.tab_process[name].retries == 0:
                        DG("process put fatal : " + name)
                        settings.tab_process[name].status = "FATAL"
            except:
                t = threading.Thread(target=guardian, args=(pid, None))
                t.start()
            settings.queue_pid.pop(0)
            settings.queue_pid.pop(0)
        time.sleep(1)
