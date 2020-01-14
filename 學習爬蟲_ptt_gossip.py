#!/usr/bin/env python
# coding: utf-8

# # ptt_gossip

# In[ ]:


#df的用法及如何增加


# In[55]:


import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
payload= {
'from': '/bbs/Gossiping/index.html',
'yes': 'yes'
}

rs = requests.session()
# .session是用來模擬登入網站
res = rs.post('https://www.ptt.cc/ask/over18', data = payload)
res = rs.get(url)
# print(res.text)
soup = bs(res.text, 'html.parser')
a = soup.find_all(class_ = "r-ent")
nrec=[]
title=[]
date=[]
author=[]
for b in a:
    nrec.append(b.select('.nrec')[0].text)
    title.append( b.select('.title')[0].text)
    date.append(b.select('.date')[0].text)
    author.append(b.select('.author')[0].text)
#     print(b.select('.nrec')[0].text, b.select('.title')[0].text, b.select('.date')[0].text, b.select('.author')[0].text)

ptt = {"nrec":nrec,
      "title":title,
       "date":date,
       "author":author
      }
df = pd.DataFrame(ptt)
print(df)

