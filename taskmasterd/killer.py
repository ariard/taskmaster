# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    killer.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:54:34 by ariard            #+#    #+#              #
#    Updated: 2017/04/21 20:55:07 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import signal

from task_signal import *

def killer(running_program)
    global queue_pid

    signal = get_signal(running_program[6])
    os.kill(running_program[15], signal)
    time.sleep(running_program[7]) + 1)
    if running_program[15] not in queue_pid:
        os.kill(running_program[15], signal.SIGKILL)
