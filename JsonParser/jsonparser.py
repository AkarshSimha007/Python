import json
import urllib.request,urllib.error,urllib.parse
targeturl=input("Enter the URL")
print("Retrieving URL:",targeturl)
uh=urllib.request.urlopen(targeturl)
data=uh.read().decode()
info=json.loads(data)
count=0
for i in info['comments']:
    count+=int(i['count'])
print("Retrieved",len(data),"characters")
print(count)