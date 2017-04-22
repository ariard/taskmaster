# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    settings.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/22 19:31:29 by ariard            #+#    #+#              #
#    Updated: 2017/04/22 20:01:34 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def init():
    global table_prog
    global table_process
    global prog_to_pid
    global queue_pid

    table_prog = dict()
    table_process = dict()
    prog_to_pid = dict()
    queue_pid = list()

