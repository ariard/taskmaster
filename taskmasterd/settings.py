# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    settings.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/22 19:31:29 by ariard            #+#    #+#              #
#    Updated: 2017/04/23 16:49:30 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def init():
    global tab_prog
    global tab_process
    global lst_pid
    global queue_pid

    tab_prog = dict()
    tab_process = dict()
    lst_pid = list()
    queue_pid = list()

