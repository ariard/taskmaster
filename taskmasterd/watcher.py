# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reporter.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 20:45:20 by ariard            #+#    #+#              #
#    Updated: 2017/05/02 18:57:10 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time

from debug import *

import settings

def watcher(name_process):

        watch_time = time.time()
        secs = watch_time - settings.tab_process[name_process].time
        if secs >= settings.tab_prog[settings.tab_process[name_process].father].startsecs \
            and (settings.tab_process[name_process].status == "STARTING" \
            or settings.tab_process[name_process].status == "BACKOFF"):
            settings.tab_process[name_process].status = "RUNNING"

def watcher_backoff(name_process):

        watch_time = time.time()
        secs = watch_time - settings.tab_process[name_process].time
        if secs < settings.tab_prog[settings.tab_process[name_process].father].startsecs \
            and (settings.tab_process[name_process].status == "STARTING" \
            or settings.tab_process[name_process].status == "BACKOFF"):
            settings.tab_process[name_process].status = "BACKOFF"
