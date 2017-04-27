# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    statutor.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/22 16:54:51 by ariard            #+#    #+#              #
#    Updated: 2017/04/26 22:32:08 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import settings

from debug import *
from watcher import *

def getStatus():

    tab = list()
    for name in settings.tab_process:
        
        DG(str(name) + "is " + settings.tab_process[name].status)
        watcher(name)
        tab.append(name + "    " + str(settings.tab_process[name].pid) + "    " + \
            settings.tab_process[name].status + "\n")
    return tab
