import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import re
import ssl
import re
import requests
import shutil
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE




url1=input("Enter URL:")
count=int(input("Enter No:"))
start=int(input("Enter Starting Point:"))
#counter=int(input("Enter count:"))
def downimage(url,name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
       with open(name, 'wb') as f:
          r.raw.decode_content = True
          shutil.copyfileobj(r.raw, f)




fhandle1=urllib.request.urlopen(url1,context=ctx).read()
soup1=BeautifulSoup(fhandle1,"html.parser")
tags1= soup1("a")
cnt=0
stopage=0
for tag in tags1:    
   u=tag.get('href', None)
   if(re.search("big.php[\S]*",u)):
    if(stopage!=start):
        stopage+=1
    else:
     if u.startswith("big") and re.search(".com/[\S]+",url1) is False:
        url2=url1+u
     elif(re.search("[\S]+.com",url1)):
        st=re.search("[\S]+.com",url1).group(0)+"/"
        url2=st+u
     else:
        url2=tag.get('href', None)
     print(url2)
     fhandle2=urllib.request.urlopen(url2,context=ctx).read()
     soup12=BeautifulSoup(fhandle2,"html.parser")
     tags12= soup12("a")
     for tagger in tags12:
        u1=tagger.get('href', None)
        if(re.search("[\S]*.jpg[\S]*", u1)):
            url3=u1
            n=str(cnt)+".jpg"
            downimage(url3,n)
            cnt+=1
            break
        if(re.search("[\S]*.png[\S]*", u1)):
            url3=u1
            n=str(cnt)+".png"
            downimage(url3,n)
            cnt+=1
            break
        if(re.search("[\S]*.jpeg[\S]*", u1)):
            url3=u1
            n=str(cnt)+".jpg"
            downimage(url3,n)
            cnt+=1
            break
   if(cnt==count):
         break





#print("Retrieving:",url1)    

