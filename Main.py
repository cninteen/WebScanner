# coding:utf-8
# Author:cteen
# Date:2020/1/7
# File:Main.py.py

import parser
from crtScan import *
from dirScan import *
from CIPscan import *
from optparse import OptionParser

if __name__ == '__main__':
    print('''
    By cteen  Ver:1.0
 __    __     _     __                                 
/ / /\ \ \___| |__ / _\ ___ __ _ _ __  _ __   ___ _ __ 
\ \/  \/ / _ \ '_ \\ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 \  /\  /  __/ |_) |\ \ (_| (_| | | | | | | |  __/ |   
  \/  \/ \___|_.__/\__/\___\__,_|_| |_|_| |_|\___|_|   

    ''')
    parser = OptionParser()
    parser.add_option("-u", "--url", dest="url", help="target url for scan")
    parser.add_option("-f", "--file", dest="ext",
                      help="target url ext")
    parser.add_option("-i", "--ip", dest="ip", help="target ip for scan C")
    parser.add_option("-t", "--thread", dest="count", type="int", default=1, help="count of scan thread")
    parser.add_option("-d","--domain",dest= "domain",help = "target domain for scan")
    (option, args) = parser.parse_args()
    if option.url and option.ext:
        print("[+]Scan for %s will start ! Filetype is %s..."%(option.url,option.ext))
        d = DirScanMain(option)
        d.start()
        print("\n")
        sys.exit(0)
    elif option.ip:
        print("[+]Scan for %s ip scan will start..." % (option.ip))
        c = CIPscanMain(option)
        c.start()
        sys.exit(0)
    elif option.domain:
        cs = crtScan(option.domain)
        result = cs.run()
        print(result)
        sys.exit(0)
    else:
        parser.print_help()
        sys.exit(0)
