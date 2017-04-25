# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    statutor.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/22 16:54:51 by ariard            #+#    #+#              #
#    Updated: 2017/04/25 19:23:03 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import settings

from debug import *

def getStatus():

    tab = list()
    for name in settings.tab_process:
        
        if str(name).isdigit() == False:
            DG(str(name))
            tab.append(name + "    " + str(settings.tab_process[name].pid) + "    " + \
                settings.tab_process[name].status + "\n")
    return tab
