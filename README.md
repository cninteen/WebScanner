# WebScanner
A py3 tool to scan web

# Run
1.C段扫描
`python Main.py -i "127.0.0.1/24" (-t 5)`

2.目录下某种类型文件扫描
`python Main.py -u "www.baidu.com" -f jsp (-t 5)`

3.域名扫描（借助crt.sh)
`python Main.py -d "baidu.com" (-t 5)`

#config
#是否开启https服务器的证书校验
allow_ssl_verify = False

#超时时间
timeout = 10

#是否允许URL重定向
allow_redirects = True

#是否允许继承http 的Requests类的Session支持，在发出的所有请求之间保持cookies
allow_http_session = True

#是否允许随机User-Agent
allow_random_useragent = False

#是否允许随机X-Forwarded-For
allow_random_x_forward = False