import getpass
import os
import socket

username = getpass.getuser()
homedir = os.environ  # ['HOME']
hostname = socket.gethostname()
print username
print os.environ['HOME']
for k in homedir:
    print k, ":", homedir[k]
print hostname
