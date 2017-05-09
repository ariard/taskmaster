# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    cleaner.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/05/03 17:28:59 by ariard            #+#    #+#              #
#    Updated: 2017/05/10 00:02:09 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import settings

from debug import *

def cleaner(list_progs):

    to_del = list()

    for name in settings.tab_process:

        if "program:" + name.strip('_0123456789') not in list_progs \
            and  (settings.tab_process[name].status == "STOPPED" or \
            settings.tab_process[name].status == "EXITED" or \
            settings.tab_process[name].status == "FATAL"):
                to_del.append(name) 

    DG(str(settings.tab_prog))
    for name in to_del:
        DG(name)
        settings.tab_process.pop(name, None)
        settings.tab_prog.pop("program:" + name.strip('_0123456789'), None)
    DG(str(settings.tab_prog))
