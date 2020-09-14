import requests
from bs4 import BeautifulSoup
username=input('Enter Instagram username:')
res=requests.get('http://instagram.com/'+username)
soup_data=BeautifulSoup(res.text,'html.parser')
userInfo=soup_data.find("meta",property="og:description")
print(userInfo.attrs['content'][:40])
