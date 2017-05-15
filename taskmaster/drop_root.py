import os
import pwd
import grp

def drop_privileges():
    if os.getuid() == 0:
        running_uid = 1
        running_gid = 1

        os.setgroups([])

        os.setgid(running_gid)
        os.setuid(running_uid)

        print('Privileges dropped !\nRunning with UID : ' + str(os.getuid()))
