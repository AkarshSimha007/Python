import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url="http://py4e-data.dr-chuck.net/known_by_Arlo.html"
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')
count=int(input("Enter the count:"))
position=int(input("Enter the position:"))-1

tags=soup("a")
followNamelist=[]

for i in range(0,count):
    #Getting the link to the next person at the position
    nextlink=tags[position].get("href",None)
    print("Retrieving",nextlink)
    #Adding the name to a list just to keep a track of all the names
    followNamelist.append(tags[position].contents[0])
    #opening the newlink related to the new name
    html = urllib.request.urlopen(nextlink, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    nextlink = tags[position].get('href', None)
print(followNamelist[count-1])