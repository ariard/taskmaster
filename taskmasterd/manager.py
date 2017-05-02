# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    manager.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/22 15:42:41 by ariard            #+#    #+#              #
#    Updated: 2017/05/02 21:55:29 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from launcher import *
from debug import *
from execute import *

import settings

def manager(config, list_progs, server):

    for name_prog in list_progs: 
        DG(name_prog)

        if name_prog in settings.tab_prog:
            new_prog = Program(config, name_prog)
            old_prog = settings.tab_prog[name_prog]
            numprocs = settings.tab_prog[name_prog].numprocs
            if new_prog.stdout != old_prog.stdout or new_prog.stderr != old_prog.stderr \
                or new_prog.env != old_prog.env or new_prog.dir != old_prog.dir \
                or new_prog.umask != old_prog.umask:
                settings.tab_prog.pop(name_prog, None)
                settings.tab_prog[name_prog] = new_prog

                for process in tab_process:

                    if process.father == name_prog:
                        server.start_killer(process.pid)
 
                while numprocs > 0:
                    if settings.tab_prog[name_prog].numprocs > 1:
                        name_process = name_prog[8:] + "_" + str(numprocs)
                    else:
                        name_process = name_prog[8:]
                    launcher(settings.tab_prog[name_prog], name_process, name_prog, \
                        copy.copy(settings.tab_prog[name_prog].startretries))
                    numprocs -= 1

            else:

                if numprocs < new_prog.numprocs:
                    new_num = numprocs
            
                    while gap_num != new_prog.numprocs:
                        name_process = name_prog[8:] + "_" + str(gap_num)
                        launcher(settings.tab_prog[name_prog], name_process, name_prog, \
                            copy.copy(settings.tab_prog[name_prog].startretries))
                        gap_num += 1

                if new_prog.autorestart != old_prog.autorestart or new_prog.exitcodes != old_prog.exitcodes \
                    or new_prog.startsecs != old_prog.startsecs or new_prog.startretries != old_prog.startretries \
                    or new_prog.stopsignal != old_prog.stopsignal or new_prog.stopwaitsecs != old_prog.stopwaitsecs:
                    settings.tab_prog.pop(name_prog, None) 
                    settings.tab_prog[name_prog] = new_prog
 
        else:
            settings.tab_prog[name_prog] = Program(config, name_prog)
            numprocs = settings.tab_prog[name_prog].numprocs

            if settings.tab_prog[name_prog].autostart == "true" \
                and settings.tab_prog[name_prog].command:

                while numprocs > 0:
                    if settings.tab_prog[name_prog].numprocs > 1:
                        name_process = name_prog[8:] + "_" + str(numprocs)
                    else:
                        name_process = name_prog[8:]
                    launcher(settings.tab_prog[name_prog], name_process, name_prog, \
                        copy.copy(settings.tab_prog[name_prog].startretries))
                    numprocs -= 1
            elif settings.tab_prog[name_prog].autostart == "false" \
                and settings.tab_prog[name_prog].command:
                
                while numprocs > 0:
                    if settings.tab_prog[name_prog].numprocs > 1:
                        name_process = name_prog[8:] + "_" + str(numprocs)
                    else:
                        name_process = name_prog[8:]
                    process = Process(name_process, "Not Started", "STOPPED", \
                        settings.tab_prog[name_prog].startretries, name_prog)
                    settings.tab_process[name_process] = process
                    numprocs -= 1

