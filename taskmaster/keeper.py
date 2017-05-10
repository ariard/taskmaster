# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    keeper.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/22 00:35:20 by ariard            #+#    #+#              #
#    Updated: 2017/05/10 22:03:09 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import logging

from taskmaster.debug import *
from taskmaster.launcher import * 
from taskmaster.task_signal import *
from taskmaster.watcher import *
from taskmaster.report import reporter

import taskmaster.settings as settings

def clean_fd(name):

    infd = settings.tab_process[name].process_fd[0]
    outfd = settings.tab_process[name].process_fd[1]
    errfd = settings.tab_process[name].process_fd[2]
    os.close(infd)
    settings.queue_old_fd.append(outfd)
    settings.queue_old_fd.append(errfd)
    DG("old fd are ")
    DG(str(settings.queue_old_fd))

def guardian(pid, null):

    for process in settings.tab_process:
        if pid == settings.tab_process[process].pid:
            settings.tab_process[process].status = "UNKNOWN"

def keeper():

    while 1 :
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
                clean_fd(name)
                DG("old fd")
                if ((exitcode not in program.exitcodes and program.autorestart == "unexpected") \
                    or (program.autorestart == "true")) and settings.tab_process[name].status == "RUNNING":
                    if program.autorestart == "unexpected":
                        start_reporter(name_prog)
                    logging.info("Autorestart %s with status %s", name, program.autorestart)
                    launcher(program, name, name_prog, program.startretries)
                elif settings.tab_process[name].status == "RUNNING":
                    settings.tab_process[name].status = "EXITED"
                elif settings.tab_process[name].status == "STOPPING":
                    settings.tab_process[name].status = "STOPPED"
                elif settings.tab_process[name].status == "BACKOFF":
                    if settings.tab_process[name].retries > 0:
                        DG("process put backoff : " + name) 
                        settings.tab_process[name].retries -= 1 
                        logging.info("Start %s from backoff", name)
                        launcher(program, name, name_prog, settings.tab_process[name].retries)
                    elif settings.tab_process[name].retries == 0:
                        DG("process put fatal : " + name)
                        start_reporter(name_prog)
                        settings.tab_process[name].status = "FATAL"
            except OSError:
                t = threading.Thread(target=guardian, args=(pid, None))
                t.start()
            settings.queue_pid.pop(0)
            settings.queue_pid.pop(0)
        time.sleep(1)
