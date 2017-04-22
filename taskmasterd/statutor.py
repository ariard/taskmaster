# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    statutor.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/22 16:54:51 by ariard            #+#    #+#              #
#    Updated: 2017/04/22 17:13:27 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def getStatus():
    global table_process
    global prog_to_pid

    tab = str()
    for name in prog_to_pid:
        
        for pid in prog_to_pid[name]:
            tab += name + "    " + str(pid) + "    " + table_process[pid][1] + "\n"
    return tab
