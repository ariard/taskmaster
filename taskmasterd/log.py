# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    log.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/07 04:12:39 by ariard            #+#    #+#              #
#    Updated: 2017/04/07 04:21:21 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

class log:
    def __init__(self):
        self.logfile = open("/tmp/logfile" + str(os.getpid()), "w+")
        self.logfile.write("Session begins at :")

    def update(self, event):
        return (self)  
