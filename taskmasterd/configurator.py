# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    configurator.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/21 19:33:01 by ariard            #+#    #+#              #
#    Updated: 2017/04/21 23:32:38 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from monitor import *

# Table Prog
#   0 : command
#   1 : autostart
#   2 : autorestart
#   3 : exitcodes
#   4 : startsecs
#   5 : startretries
#   6 : stopsignal
#   7 : stopwaitsecs
#   8 : stdout
#   9 : stderr
#   10: env
#   11: dir
#   12: umask
#   13 : program
#   14 : status
#   15 : pid

table_prog = list()

def configurater(config, list_progs)
    global table_prog
    global pid_to_prog

    for name_prog in list_progs: 
        if name_prog in table_prog:
            
        else:
            table_prog[name_prog] = Program(config, name_prog)

            


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


