#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
payload = {
   'from': 'https://www.ptt.cc/bbs/Gossiping/index.html',
 'yes': 'yes'
 }
headers = {
 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
rs = requests.Session()
rs.post('https://www.ptt.cc/ask/over18', data=payload, headers=headers)
res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
items = soup.select('.r-ent')
for item in items:
    print(item.select('.date')[0].text, item.select('.author')[0].text, item.select('.title')[0].text)


# In[42]:


# import requests
# from bs4 import BeautifulSoup
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
# url = 'https://www.youtube.com/channel/UCFdTiwvDjyc62DBWrlYDtlQ/videos?sort=p&view=0&flow=grid'
# resp = requests.get(url,headers=headers)
# soup = BeautifulSoup(resp.text, 'lxml')
# target=soup.find_all('a')
# for b in target:
#     print(b.text)
    
# txt = open('video-title.txt', 'w', encoding = 'UTF-8')
# for i in target:
#     f=i.get_text().strip() #取得文字、去除左右的空格
#     txt.write(f)           #寫入文字
#     txt.write('\n')        #換行
# txt.close()                #關閉檔案


# In[3]:


import requests
from bs4 import BeautifulSoup
url = "https://www.ptt.cc/bbs/joke/index.html"
for i in range(3): #往上爬3頁
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    sel = soup.select("div.title a") #標題
    u = soup.select("div.btn-group.btn-group-paging a") #a標籤
    print ("本頁的URL為"+url)
    url = "https://www.ptt.cc"+ u[1]["href"] #上一頁的網址
    for s in sel: #印出網址跟標題
        print(s.text)

