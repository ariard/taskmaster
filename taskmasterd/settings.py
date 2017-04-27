# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    settings.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/22 19:31:29 by ariard            #+#    #+#              #
#    Updated: 2017/04/26 22:27:58 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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

