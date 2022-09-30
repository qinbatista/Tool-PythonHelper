#!/usr/bin/env python3
import os
from socket import *
import sys
if __name__ == "__main__":
    if len(sys.argv)>=2:
        if sys.argv[1].find(".")!=-1:
            this_ip = gethostbyname(sys.argv[1])
        else:
            this_ip = sys.argv[1]
    if len(sys.argv)>=2:
        os.system('curl http://www.cip.cc/'+this_ip)
    else:
        os.system('curl http://www.cip.cc')