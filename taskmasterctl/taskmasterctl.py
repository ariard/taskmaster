# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    taskmasterctl.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ataguiro <ataguiro@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/13 15:44:17 by ataguiro          #+#    #+#              #
#    Updated: 2017/04/13 15:49:53 by ataguiro         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys
import signal
import socket
#import time

def run_client:
    host = 'localhost'
    port = 2121
    #sys.stdout.write('>')
    #sys.stdout.flush()
    #sys.stdin.readline()
    cs = socket.socket()
    cs.connect((HOST, PORT)) 
    client_socket.send('start')
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    #petit pb : quand un client quitte avec ctrl+c, le serveur ne le sait pas
    while True:
        #sys.stdout.write('>')
        #sys.stdout.flush()
        cmd = input("> ")
        client_socket.send(cmd)
if __name__ == '__main__' :
    run_client()
