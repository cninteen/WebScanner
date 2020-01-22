# coding:utf-8
# Author:cteen
# Date:2020/1/7
# File:dirScan.py

import queue
import threading
import sys

from Common import *



class DirScanMain:
    def __init__(self, options):
        self.url = options.url
        self.ext = options.ext
        self.count = options.count

    class DirScan(threading.Thread):
        def __init__(self, que, total):
            threading.Thread.__init__(self)
            self._queue = que
            self._total = total

        def run(self):
            while not self._queue.empty():
                url = self._queue.get()
                threading.Thread(target=self.msg).start()
                try:
                    if http_requests_get(url).status_code == 200:
                        print("[+]", url)
                except Exception as e:
                    # print(e)
                    pass

        def msg(self):
            per = 100 - (float(self._queue.qsize()) / float(self._total)) * 100
            ms = "%s Left | %s All | Scan in %1.f %s" % (self._queue.qsize(), self._total, per, "%")

            sys.stdout.write('\r' + '[*]' + ms)
            sys.stdout.flush()
            # time.sleep(1)

    def start(self):
        que = queue.Queue()

        f = open("./dics/%s.txt" % (self.ext), 'r')
        for line in f:
            que.put(self.url + line.rstrip('\n'))
        total = que.qsize()

        threads = []
        threads_count = self.count

        for i in range(threads_count):
            threads.append(self.DirScan(que,total))
        for t in threads:
            t.start()
        for t in threads:
            t.join()


