import json
import urllib.request,urllib.error,urllib.parse
targeturl=input("Enter the URL")
print("Retrieving URL:",targeturl)
uh=urllib.request.urlopen(targeturl)
data=uh.read().decode()
info=json.loads(data)
for i in info['comments']:
    print(info['comments']['name'])
