# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    task_error.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 21:55:37 by ariard            #+#    #+#              #
#    Updated: 2017/05/06 16:05:04 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def error_msg(msg):
    
    print("taskmasterd: " + msg, file=sys.stderr)
    sys.exit(-1)
