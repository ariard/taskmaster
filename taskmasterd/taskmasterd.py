# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    __main__.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/04/04 21:57:30 by ariard            #+#    #+#              #
#    Updated: 2017/04/06 21:45:11 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import os
import sys
import signal
import time
import socket

def daemon_success(number, frame):
    file = open("/tmp/daemon.log", 'w+')
    file.write(str(os.times()) + "\n")
    file.write("Your daemon has been successfully created !")
    file.close()
    sys.exit()

def daemonize():

#   Close all non standard fd
#   Restore default signal handler
#   Sanitize environnement variable
#   Check .pid to ensure non-daemon

    fatherpid = os.getpid()
    status = os.fork()

    if status > 0:
       signal.signal(signal.SIGUSR1, daemon_success)   
       os.wait()
    
    if status == 0:
        os.setsid()
        status = os.fork()
        
        if status > 0:
            sys.exit()

        fd = open('/dev/null')
        os.dup2(fd.fileno(), 0)
        os.dup2(fd.fileno(), 1)
        os.dup2(fd.fileno(), 2)

        os.umask(0)
        os.chdir('/')
        
        pidfile = open('/tmp/taskmasterd.pid', 'w+')
        pid = os.getpid() 
        pidfile.write(str(pid))

        os.kill(fatherpid, signal.SIGUSR1) 


def server():
# Change HOST value    
    HOST = ''
    PORT = 2121
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, \
                    socket.getprotobyname("tcp"))
    if server_socket.bind((HOST, PORT)) == False:
        sys.exit(-1)
    server_socket.listen(42)
    client_socket, client_addr = server_socket.accept()
    while True:
        data = client_socket.recv(1024)
        print("Received", repr(data))

if __name__ == '__main__' :
    daemonize()
    server()


#server.init #server.listen #server.deploy #server.exit
