# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    statutor.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/22 16:54:51 by ariard            #+#    #+#              #
#    Updated: 2017/04/29 19:26:04 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import settings

from debug import *
from watcher import *

def getStatus():
    
    tab = list()
     
    max_padding = 0
    max_padding_pid = 0
    for name in settings.tab_process:
        if len(name) > max_padding:
            max_padding = len(name)
        if len(str(settings.tab_process[name].pid)) > max_padding_pid:
            max_padding_pid = len(str(settings.tab_process[name].pid))
    
    max_padding += 15
    max_padding_pid += 15

    for name in settings.tab_process:
        watcher(name)
        
        name_padding = max_padding - len(name)
        padone = " " * name_padding

        pid_padding = max_padding_pid - len(str(settings.tab_process[name].pid))
        padtwo = " " * pid_padding
            
        tab.append(name + padone + str(settings.tab_process[name].pid) + padtwo + \
            settings.tab_process[name].status + "\n")
    return tab
