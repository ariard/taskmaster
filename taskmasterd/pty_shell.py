import os
import pty
import time
import tty
from select import select

STDIN_FILENO=0
STDOUT_FILENO=1


def _writen(fd, data):

    while data:
        n = os.write(fd, data)
        data = data[n:]

def _read(fd):
    return os.read(fd, 1024)

def my_copy(master_fd, master_read=_read, stdin_read=_read):

    fds = [master_fd, STDIN_FILENO]
    while True:
        rfds, wfds, xfds = select(fds, [], [])
        if master_fd in rfds:
            data = master_read(master_fd)
            if not data:
                fds.remove(master_fd)
            else:
                os.write(STDOUT_FILENO, data)
        if STDIN_FILENO in rfds:
            data = stdin_read(STDIN_FILENO)
            if not data:
                fds.remove(STDIN_FILENO)
            else:
                _writen(master_fd, data)

if __name__ == '__main__':

    pid, master_fd = pty.fork()
    print("pid is :" + str(pid))
    if pid == 0:
        os.execv("/bin/bash", ["/bin/bash"])

    if pid > 0:
        time.sleep(1)
        try:
            mode = tty.tcgetattr(STDIN_FILENO)
            tty.setraw(STDIN_FILENO)
            restore = 1
        except tty.error:
            restore = 0
        try:
            my_copy(master_fd)
        except:
            if restore:
                tty.tcsetattr(STDIN_FILENO, tty.TCSAFLUSH, mode)
