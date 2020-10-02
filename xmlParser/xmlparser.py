import urllib.request,urllib.parse,urllib.error
import ssl
import xml.etree.ElementTree as ET

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

sum=0
url=input("Enter URL of Web Page")
xml=urllib.request.urlopen(url,context=ctx).read()
tree=ET.fromstring(xml)
lst=tree.findall('comments/comment')
print("Count:",len(lst))
for i in lst:
    sum+=int(i.find('count').text)
print("Sum:",sum)
