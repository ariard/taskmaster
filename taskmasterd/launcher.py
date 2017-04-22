# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    launcher.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:57:06 by ariard            #+#    #+#              #
#    Updated: 2017/04/22 01:46:28 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys 
import time

# Table Prog
#   0 : command
#   1 : autostart
#   2 : autorestart
#   3 : exitcodes
#   4 : startsecs
#   5 : startretries
#   6 : stopsignal
#   7 : stopwaitsecs
#   8 : stdout
#   9 : stderr
#   10: env
#   11: dir
#   12: umask
#   13 : program
#   14 : status
#   15 : pid
#   16 : brothers

def launcher(program, name_prog)
    global table_prog
    global table_process
    global prog_to_pid

    pid = os.fork()
    if pid > 0:
        if program.startsecs == 0:
            status = "STARTING"
        else:
            status = "RUNNING"
        table_process[pid] = [name_prog, status, program.startretriesi[:]]
        prog_to_pid[name_prog] += pid

    if pid == 0:
        DG("launch command")
        program.conf()
        try:
            args = program.command.split(' ')
            DG(args[0])
#            log.update("[PROGRAM] - Launch " + str(program.command) + "\n")
#           log start + modify table_prog on shared memory
#            fifo = os.open("/tmp/fifo", os.O_WRONLY | os.O_SYNC)
            fifo = open("/tmp/fifo", "w")
            fifo.write(str(os.getpid()) + ";" + str(time.time()) + "\n")
#            os.close(fifo)
            fifo.close()
            DG("after write FIFO")
            os.execv(args[0], args)
        except
            DG("log : no such program")
            sys.exit(-1)
