# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    keeper.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/22 00:35:20 by ariard            #+#    #+#              #
#    Updated: 2017/04/22 17:30:23 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from debug import *
from launcher import * 
from task_signal import *

def keeper():
    global queue_pid
    global table_prog
    global table_process

    while 1 :
        while len(queue_pid) > 1:
            pid = queue_pid[0]
            exitcode = queue_pid[1]
            program = table_prog[table_process[pid]]
            if ((exitcode not in program.exitcodes and program.autorestart == "unexpected") \
                or (program.autorestart == "true")) and table_process[pid][1] == "RUNNING":
                if table_process[pid][2] > 0:
                    launcher(program, name_prog)
                    table_process[pid][2] -= 1
            elif table_process[pid][1] == "RUNNING":
                table_process[pid][1] = "EXITED"
            elif table_process[pid][1] == "STARTING":
                if table_process[pid][2] > 0:
                    launcher(program, name_prog)
                    table_process[pid][2] -= 1 
            queue_pid.pop(0)
            queue_pid.pop(0) 
        time.sleep(1)
