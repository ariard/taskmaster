# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    task_signal.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/15 18:50:45 by ariard            #+#    #+#              #
#    Updated: 2017/05/02 17:12:35 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import signal
import settings

from debug import *

def check_exit(number, frame):

    while True:
        try:
            pid = os.waitpid(0, 0)
            settings.queue_pid += pid;
        except:
            break
