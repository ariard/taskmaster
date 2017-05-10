# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    extract.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/25 20:47:11 by ariard            #+#    #+#              #
#    Updated: 2017/05/10 15:54:12 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from taskmaster.debug import *

def extractProg(list_sections):
    prog = list()
    DG("sections " + str(list_sections))
    for sections in list_sections:
        if sections[0:7] == "program":
            prog.append(sections)
    return (prog)
