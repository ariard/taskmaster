# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    settings.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/22 19:31:29 by ariard            #+#    #+#              #
#    Updated: 2017/04/22 19:32:39 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def init():
    global table_prog
    global table_process
    global prog_to_pid

    table_prog = dict()
    table_process = dict()
    prog_to_pid = dict()
