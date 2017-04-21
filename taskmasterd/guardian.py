# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guardian.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:47:16 by ariard            #+#    #+#              #
#    Updated: 2017/04/21 20:48:22 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from debug import *
from launcher import * 

def guardian():
    global queue_pid
    global table_prog

    while 1 :
        while len(queue_pid) > 1:
            pid = queue_pid[0]
            status = queue_pid[1]
            program = table_prog[pid]
            if program[3] != status and program[2] == "true":
                if program[5] > 0:
                    program[13].startretries -= 1
                    launcher(program[13], program[16])
            queue_pid.pop(0)
            queue_pid.pop(0) 
        time.sleep(1)
