# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    manager.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/22 15:42:41 by ariard            #+#    #+#              #
#    Updated: 2017/04/22 17:50:27 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from monitor import *

table_prog = dict()
table_process = dict()
prog_to_pid = dict()

def manager(config, list_progs, server):
    global table_prog
    global table_process
    global prog_to_pid

    for name_prog in list_progs: 
        numprocs = table_prog[name_prog].numprocs                 

        if name_prog in table_prog:
            new_prog = Program(config, name_prog)
            old_prog = table_prog[name_prog]

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

                while numprocs > 0:
                    launcher(table_prog[name_prog], name_prog)
                    numprocs -= 1

            elif table_prog[name_prog].autostart == "false":
                table_prog[name_prog].autostart == "true" 
