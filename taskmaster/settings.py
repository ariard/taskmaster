# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    settings.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/22 19:31:29 by ariard            #+#    #+#              #
#    Updated: 2017/05/10 16:13:18 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def init():
    global tab_prog
    global tab_process
    global pid2name
    global lst_pid
    global queue_pid
    global tab_out
    global fds
    global wr_fds
    global fd2realfile
    global process2fd
    global attach_process

    tab_prog = dict()
    tab_process = dict()
    pid2name = dict()
    lst_pid = list()
    queue_pid = list()
    tab_out = dict()
    fds = list()
    wr_fds = list()
    fd2realfile = dict()
    attach_process = 0
