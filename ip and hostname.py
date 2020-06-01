from socket import *
import time
import requests
import urllib.parse
import httpx
print("1.checking with hostname ")
print("2.checking with ip address ")
choice=int(input('enter the choice '))
url='https://ipinfo.io/'
if choice==2:
    s = input('enter the ip address ')
    a=requests.get(url+s)
    print("The ip-geolocation of the ip address is ",a.text)
    h=getfqdn(s)
    print("The domain of the ip address is ",h)
    I=gethostbyaddr(s)
    print('The host address of the particular ip address ',I)
    t = time.time()
    for i in range(50, 500):
        g = socket(AF_INET, SOCK_STREAM)
        t = g.connect_ex((s, i))
        if t == 0:
            print('port opened ', i)
        g.close()
    print(time.time() - t)
elif choice==1:
    print('www.example.com <----------- Like this')
    URL=input(str('enter the name of the website '))
    h = getfqdn(URL)
    print("The domain of the ip address is ", h)
    j=gethostbyname(URL)
    print('the ip address of the URL is ',j)
    abc=input("Enter the URL of the  above given website ")
    o=httpx.get(abc)
    print('The source of the webpage of the the Url ',o.text)
    print('The character-set encoding of the Url ',o.charset_encoding)
    print('The https version of the Url ',o.http_version)
    print('The links in the webiste ',o.links)
    print('The apparent-encoding of the website ',o.apparent_encoding)
    print('The status-code of the url if its ets it replies true ',o.status_code)
    print('The history about the website ',o.history)
    g = urllib.parse.urlparse(abc)
    print(g.netloc)
    print('The fully qualified domain name is ', getfqdn(URL))
    print(gethostbyname(g.netloc))
    print(gethostbyname_ex(g.netloc))
    ip=gethostbyname(URL)
    s1 = 'https://ipinfo.io/' + j
    t = requests.get(s1)
    print('the location of the ip address', t.text)
    print('This shows the information of domain and ip address',gethostbyaddr(gethostbyname(g.netloc)))
    print('this checks the the opened ports of the website')
    t = time.time()
    for i in range(50, 500):
        g = socket(AF_INET, SOCK_STREAM)
        t = g.connect_ex((j, i))
        if t == 0:
          print('port opened ', i)
        g.close()
    print(time.time() - t)
    print('''''''''''THANK YOU''''''''')
