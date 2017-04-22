# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    configurator.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 19:33:01 by ariard            #+#    #+#              #
#    Updated: 2017/04/22 01:47:02 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from monitor import *

table_prog = dict()
table_process = dict()
prog_to_pid = dict()

def manager(config, list_progs)
    global table_prog
    global table_process

    for name_prog in list_progs: 
        if name_prog in table_prog:
            
        else:
            table_prog[name_prog] = Program(config, name_prog)
            if table_prog[name_prog].autostart == "true"
                and table_prog[name_prog].command:
                numprocs = table_prog[name_prog].numprocs
                while numprocs > 0:
                    launcher(table_prog[name_prog], name_prog)
                    numprocs -= 1
            elif table_prog[name_prog].autostart == "false"
                table_prog[name_prog].autostart == "true" 
            

    for name in monitor.list_programs:
        abstract_program = Program(monitor.config, name) 
        try:
            running_program = table_prog[name]
            if running_program[8] != abstract_program.stdout \
                or running_program[9] != abstract_program.stderr \
                or running_program[10] != abstract_program.env \
                or running_program[11] != abstract_program.dir \
                or running_program[12] != abstract_program.umask:
                monitor.start_killer(running_program)
                launcher(abstract_program)
            elif running_program[16] < abstract_program.numprocs:
                num = abstract_program.numprocs - running_program[16]
                while num > 0
                    launcher(abstract_program, abstract_program.numprocs)
                    num -= 1 
        except: 


