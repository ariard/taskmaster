# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    too_much_process.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/05/11 19:31:10 by ariard            #+#    #+#              #
#    Updated: 2017/05/11 23:14:41 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import configparser

import taskmaster.settings as settings

def protect_stackoverflow(list_progs, config):
    
    count = 0
    for programs in list_progs:
        try:
            count += int(config.get(programs, "numprocs"))
            if count > 200:
                return True
        except configparser.NoOptionError:
            count += 1

    return False
