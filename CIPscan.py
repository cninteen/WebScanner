# coding:utf-8
# Author:cteen
# Date:2020/1/8
# File:CIPscan.py

import threading
import queue
from Common import *
from IPy import IP
import sys


class CIPscanMain:
    def __init__(self, option):
        self.ip = option.ip
        self.count = option.count

    class CIPscan(threading.Thread):
        def __init__(self, queue, total):
            threading.Thread.__init__(self)
            self._queue = queue
            self._total = total

        def run(self):
            while not self._queue.empty():
                threading.Thread(target=self.msg).start()
                url = self._queue.get_nowait()
                # print(url)
                try:
                    if http_requests_get(url):
                        print('[*]Web Service Fount! %s' % url)
                except Exception as e:
                    pass

        def msg(self):
            per = 100 - (float(self._queue.qsize()) / float(self._total)) * 100
            ms = "%s Left | %s All | Scan in %1.f %s" % (self._queue.qsize(), self._total, per, "%")
            sys.stdout.write('\r' + '[*]' + ms)
            sys.stdout.flush()
    def create(self, ip):
        que = queue.Queue()
        ips = IP(ip, make_net=True)
        # 端口号问题
        ports = ['80', '8080', '3443']

        for i in ips:
            for p in ports:
                que.put("http://" + str(i) + ":" + str(p))

        return que

    def start(self):
        que = self.create(self.ip)
        threads = []
        threads_count = self.count
        total = que.qsize()
        for i in range(threads_count):
            threads.append(self.CIPscan(que, total))

        for t in threads:
            t.start()

        for t in threads:
            t.join()





