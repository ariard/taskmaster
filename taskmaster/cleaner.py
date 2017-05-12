# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    cleaner.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/05/03 17:28:59 by ariard            #+#    #+#              #
#    Updated: 2017/05/12 15:22:26 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import taskmaster.settings as settings

from taskmaster.debug import *

def cleaner(list_progs):

    to_del = list()

    for name in settings.tab_process:

        if "program:" + name.split('_')[0] not in list_progs \
            and  (settings.tab_process[name].status == "STOPPED" or \
            settings.tab_process[name].status == "EXITED" or \
            settings.tab_process[name].status == "FATAL" or \
            settings.tab_process[name].status == "UNKNOWN"):
                to_del.append(name) 

    for name in to_del:
        settings.tab_process.pop(name, None)
