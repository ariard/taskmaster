import os
import sys

pid, fd = os.forkpty()

if pid == 0:
    os.execve("/bin/bash", "/bin/bash")
else:
    print(os.read(fd, 1000))

    c = os.read(fd, 1)
    while c:
        c = os.read(fd, 1)
        sys.stdout.write(str(c))
