import socket
import thread
import sys

num_threads = 0

def new_client(clientsocket, addr):
    while True:
        m = clientsocket.recv(1024)
        m = m.strip()
        if not m:
            print 'That motherfucking client ' + str(addr[1]) + ' sent a SIGINT signal, stopping...'
            break
        if m == 'exit' or m == 'quit':
            print 'exit request received from ' + str(addr[1]) + ' ... stopping'
            break
        print addr, ' >> ', m
        #m = raw_input('> ')
        #clientsocket.send(m + "\n")
    global num_threads
    num_threads -= 1
    print 'debug: [' + str(num_threads) + '] threads are actually running'
    clientsocket.close()

s = socket.socket()
host = "192.168.0.10"
port = 4242

print 'Server started and waiting for clients...'

s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    print 'Connection received from : ', addr
    thread.start_new_thread(new_client, (c, addr))
    num_threads += 1
    print 'debug: [' + str(num_threads) + '] threads are actually running'
s.close()
