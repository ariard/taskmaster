# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    settings.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/22 19:31:29 by ariard            #+#    #+#              #
#    Updated: 2017/04/29 16:39:57 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import logging

def init():
    global tab_prog
    global tab_process
    global pid2name
    global lst_pid
    global queue_pid

    tab_prog = dict()
    tab_process = dict()
    pid2name = dict()
    lst_pid = list()
    queue_pid = list()

    LOGFILE='logs'
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s', \
        datefmt='%m/%d/%Y %I:%M:%S %p', filename=LOGFILE, filemode='a')
