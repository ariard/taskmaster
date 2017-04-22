# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    debug.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/12 16:47:39 by ariard            #+#    #+#              #
#    Updated: 2017/04/22 17:47:29 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import inspect
import re
import random
import threading

BG_DEF="\033[49m"
BG_RED="\033[41m"
BG_GREEN="\033[42m"
BG_YELLOW="\033[43m"
BG_BLUE="\033[44m"
BG_MAGENTA="\033[45m"
BG_CYAN="\033[46m"

FG_WHITE="\033[97m"

pid_color = 0

def DG_init():
    global pid_color
    dbg_colors = [BG_RED, BG_BLUE, BG_MAGENTA, BG_YELLOW]
    pid_color = random.choice(dbg_colors)
    print(BG_GREEN + "START", file=open("/tmp/STDBUG", "a+"), flush=True)

def DG(message):
    stdbug = open("/tmp/STDBUG", "a+")
    frame = inspect.stack()[1]
    info =  inspect.getframeinfo(frame[0])
    list_path = re.split('/', info.filename)
    filename = list_path[len(list_path) - 1]
    pid = str(os.getpid())
    thread = str(threading.get_ident())
    align = 40 - (len(pid) + len(filename) + len(thread))
    space = str()
    while align > 0:
        space += ' '
        align -= 1
    print(pid_color + FG_WHITE + pid, thread, filename, space,
        ":" + BG_DEF + "  " + message, file=open("/tmp/STDBUG", "a+"), flush=True)

