# coding:utf-8
# Author:cteen
# Date:2020/1/9
# File:crtScan.py

from Common import *
import re


class crtScan():
    def __init__(self,domain):
        self._domain = domain
        self._site = 'https://crt.sh/?q='
        self.result = []
    def run(self):
        url = self._site+self._domain
        try:
            res = http_requests_get(url=url)
            # print(res.text)
            results = re.findall("</TD>\n    <TD>(.*?)</TD>\n    <TD><A",res.text,re.S)
            for result in results:
                if is_domain(result):
                    self.result.append(result)
            return list(set(self.result))
        except:
            return self.result

# if __name__ == '__main__':
#     c = crtScan("ichunqiu.com")
#     print(c.run())

