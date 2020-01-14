#!/usr/bin/env python
# coding: utf-8

# Selenium實例使用
# 
# XPATH試用

# In[2]:


from selenium import webdriver
import time
from bs4 import BeautifulSoup

url = 'https://www.skyscanner.com.tw/transport/flights/tpet/sela/200113/200120/?adults=2&children=0&adultsv2=2&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home'
driver = webdriver.Firefox() #開啟firefox
driver.get(url) #前往這個網址

time.sleep(3)

cheap_btn = driver.find_element_by_xpath('//*[@id="app-root"]/div[2]/div[2]/div[1]/div[2]/button[2]')
cheap_btn.click()

time.sleep(3)

cheap_btn = driver.find_element_by_xpath('//*[@id="app-root"]/div[2]/div[2]/div[1]/button')
cheap_btn.click()

time.sleep(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')
for ele in soup.select('.Price_mainPriceContainer__1dqsw'):
    print(ele.text)
    
driver.close()

