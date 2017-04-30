# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    drop_root.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: echo <marvin@42.fr>                        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/24 23:02:48 by echo              #+#    #+#              #
#    Updated: 2017/04/30 14:58:26 by echo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import pwd
import grp

def drop_privileges():
    if os.getuid() == 0:
        running_uid = 1
        running_gid = 1

        os.setgroups([])

        os.setgid(running_gid)
        os.setuid(running_uid)

        print('Privileges dropped !\nRunning with UID : ' + str(os.getuid()))
