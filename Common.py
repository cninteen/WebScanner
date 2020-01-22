# coding:utf-8
# Author:cteen
# Date:2020/1/7
# File:Common.py
import requests
import re
from Config import *
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def http_requests_get(url, allow_redirects=allow_redirects):
    try:
        result = requests.get(
            url=url,
            headers=headers,
            timeout=timeout,
            allow_redirects=allow_redirects,
            verify=allow_ssl_verify
        )
        return result
    except Exception as e:
        return requests.models.Response()


def http_requests_post(url, payload, allow_redirecs=allow_redirects):
    try:
        result = requests.post(
            url=url,
            headers=headers,
            data=payload,
            timeout=timeout,
            allow_redirecs=allow_redirecs,
            verify=allow_ssl_verify
        )
        return result
    except Exception as e:
        return requests.models.Response()


def is_domain(domain):
    # domain_reginx = re.compile(
        # r'(?:[A-Z0-9_](?:[A-Z0-9-_]{0,247}[A-Z0-9])？\.)+(?:[A-Z]{2,6}|[A-Z0-9-]{2,}(?<!-))\Z', re.IGNORECASE)
    domain_reginx = re.compile('^(?=^.{3,255}$)[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+$')
    return True if domain_reginx.match(domain) else False
