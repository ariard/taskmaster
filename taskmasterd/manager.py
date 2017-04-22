# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    manager.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/22 15:42:41 by ariard            #+#    #+#              #
#    Updated: 2017/04/22 19:58:49 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from launcher import *
from debug import *
from execute import *

import settings

def manager(config, list_progs, server):
    table_prog = settings.table_prog
    table_process = settings.table_process
    prog_to_pid = settings.prog_to_pid

    DG(str(list_progs))
    for name_prog in list_progs: 
        DG(name_prog)

        if name_prog in table_prog:
            new_prog = Program(config, name_prog)
            old_prog = table_prog[name_prog]
            numprocs = table_prog[name_prog].numprocs                 
            if new_prog.stdout != old_prog.stdout or new_prog.stderr != old_prog.stderr \
                or new_prog.env != old_prog.env or new_prog.dir != old_prog.dir \
                or new_prog.umask != old_prog.umask:
                table_prog.pop(name_prog, None)
                table_prog[name_prog] = new_prog

                while numprocs > 0:
                    server.start_killer(prog_to_pid[name_prog])
                    prog_to_pid[name_prog] = prog_to_pid[name_prog][1:]
                    numprocs -= 1
                numprocs = table_prog[name_prog].numprocs
 
                while numprocs > 0:
                    launcher(table_prog[name_prog], name_prog)
                    numprocs -= 1

            else:

                if numprocs < new_prog.numprocs:
                    new_num = new_prog - numprocs

                    while new_num > 0:
                        launcher(table_prog[name_prog], name_prog)
                        numprocs -= 1

                if new_prog.autorestart != old_prog.autorestart or new_prog.exitcodes != old_prog.exitcodes \
                    or new_prog.startsecs != old_prog.startsecs or new_prog.startretries != old_prog.startretries \
                    or new_prog.stopsignal != old_prog.stopsignal or new_prog.stopwaitsecs != old_prog.stopwaitsecs:
                    table_prog.pop(name_prog, None) 
                    table_prog[name_prog] = new_prog
 
        else:
            table_prog[name_prog] = Program(config, name_prog)

            if table_prog[name_prog].autostart == "true" \
                and table_prog[name_prog].command:
                numprocs = table_prog[name_prog].numprocs                 
                prog_to_pid[name_prog] = list()

                while numprocs > 0:
                    launcher(table_prog[name_prog], name_prog)
                    numprocs -= 1

            elif table_prog[name_prog].autostart == "false":
                table_prog[name_prog].autostart == "true" 
