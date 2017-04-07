# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/07 04:23:04 by ariard            #+#    #+#              #
#    Updated: 2017/04/07 04:27:26 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class execute:
    def __init__(self, parse, program):
        if parse.get(program, "command"):
            self.command = parse.get(program, "command")
            self.numprocs = int(parse.get(program, "numprocs"))
            self.autostart = parse.get(program, "autostart")
            self.autorestart = parse.get(program, "autorestart")
            self.startsecs = parse.get(program, "startsecs")
            self.startretries = parse.get(program, "startretries")
            self.stopsignal = parse.get(program, "stopsignal")
            self.stopwaitsecs = parse.get(program, "stopwaitsecs")
            self.stdout = parse.get(program, "stdout_logfile")
            self.stderr = parse.get(program, "stderr_logfile")
            self.env = parse.get(program, "environnement")
            self.dir = parse.get(program, "directory")
            self.umask = parse.get(program, "umask")

    def set_command(self):
        return (self)

    def exe_command(self):
        return (self)

    def post_exe(self):
        return (self)
