# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    drop_root.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: echo <marvin@42.fr>                        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/24 23:02:48 by echo              #+#    #+#              #
#    Updated: 2017/04/24 23:09:13 by echo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import pwd
import grp

def drop_privileges():
    if os.getuid() == 0:
        running_uid = pwd.getpwnam('echo').pw_uid
        running_gid = grp.getgrnam('staff').gr_gid

        os.setgroups([])

        os.setgid(running_gid)
        os.setuid(running_uid)

        # old_umask = os.umask(077)
        print('Privileges dropped !\nRunning with UID : ' + str(os.getuid()))
