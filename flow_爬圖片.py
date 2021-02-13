#1.抓人體圖
import requests
import urllib.request
from bs4 import BeautifulSoup
import os
import time


url = 'http://www.posemaniacs.com//blog/sp/?cat='

folder_path ='./photo/'

if (os.path.exists(folder_path) == False): #判斷資料夾是否存在

    os.makedirs(folder_path) #Create folder
      
iii=1

# 下載圖片function
def dlpic(items):
    
    global iii
    
    for index , item in enumerate (items):

            html = requests.get(item.get('src')) # use 'get' to get photo link path , requests = send request

            img_name = folder_path + str(iii) + '.png'

            iii=iii+1

            with open(img_name,'wb') as file: #以byte的形式將圖片數據寫入

                file.write(html.content)

                file.flush()

            file.close() #close file

            print('第 %d 張' % (iii))

# 爬不同種類
for num in range(1,50):
    
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url+str(num),headers = headers) #使用header避免訪問受到限制

    soup = BeautifulSoup(response.content, 'html.parser')

    items = soup.find_all('img')

    dlpic(items)


# 抓下一頁
    next_url_html = soup.select_one('.nextNav a')
    
        
# 判斷有無下一頁，若沒有就跳下一個迴圈
    if next_url_html == None:     
        continue    
    else:
        url2=next_url_html['href']
    
#  爬該種類下的各頁
    for iiii in range(1,200):
    
        response = requests.get(url2, headers = headers)
    
        soup = BeautifulSoup(response.content, 'html.parser')

        items = soup.find_all('img')

        dlpic(items)
        
# 抓下一頁
        next_url_html = soup.select_one('.nextNav a')
         
# 判斷有無下一頁，若沒有就跳出迴圈到上一層繼續
        if next_url_html == None:     
            break    
        else:
            url2=next_url_html['href']
           
            
            
print('Done')
#2.抓動物圖
from bs4 import BeautifulSoup
import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
lista = []
driver = webdriver.Chrome(ChromeDriverManager().install())
url0 = 'https://line-of-action.com'
#driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe") # 如果你沒有把webdriver放在同一個資料夾中，必須指定位置給他
driver.get("https://line-of-action.com/practice-tools/animal-drawing")
def tryclick(driver, selector, count=0): ##保護機制，以防無法定味道還沒渲染出來的元素
    try:
        elem = driver.find_element_by_css_selector(selector)
        # elem = driver.find_element_by_xpath(Xpath)  # 如果你想透過Xpath定位元素
        elem.click() # 點擊定位到的元素
    except:
        time.sleep(2)
        count+=1
        if(count <2):
            tryclick(driver, selector,count)
        else:
            print("cannot locate element" + selector)
tryclick(driver, "#content > div > div:nth-child(3) > div:nth-child(1) > label > input[type=radio]") 
time.sleep(2)
tryclick(driver, "#content > div > div.appform__input.appform--inline > div:nth-child(1) > label > input[type=radio]") 
time.sleep(2)
tryclick(driver, "#content > div > div:nth-child(10) > button") # 使用selector路徑點確認
#tryclick(driver, "#crstime_search") # 點擊「檢索」按鍵
 # 等待javascript渲染出來，當然這個部分還有更進階的作法，關鍵字是implicit wait, explicit wait，有興趣可以自己去找
for num in range(1,5000):
    time.sleep(0.5)
    html = driver.page_source # 取得html文字
    # driver.close()  # 關掉Driver打開的瀏覽器
    soup = BeautifulSoup(html, 'html.parser')
    b_tag = soup.find(class_="overlay--image")
    lista.append(b_tag['style'][23:77])
    print(b_tag['style'][23:77])
    tryclick(driver, "#content > div > div.session-overlay > div > div > div.session-overlay-image-wrapper > div > div.image-toolbar > span:nth-child(5) > i")

import os,re,urllib,uuid 
import urllib.request
#首先定義雲端的網頁,以及本地儲存的資料夾地址 
# urlPath='http://gamebar.com/' 
localPath='C:/Users/user/Documents/抓圖' 


#從一個網頁url中獲取圖片的地址，儲存在 
#一個list中返回 
# def getUrlList(urlParam): 
# urlStream=urllib.urlopen(urlParam) 
# htmlString=urlStream.read() 
# if( len(htmlString)!=0 ): 
# patternString=r'http://.{0,50}\.jpg' 
# searchPattern=re.compile(patternString) 
# imgUrlList=searchPattern.findall(htmlString) 
# return imgUrlList 


#生成一個檔名字串  
# def generateFileName(): 
# return str(uuid.uuid1()) 


#根據檔名建立檔案  
def createFileWithFileName(localPathParam,fileName): 
    totalPath=localPathParam+'\\'+ fileName 
    if not os.path.exists(totalPath): 
        file=open(totalPath,'a') 
        file.close() 
        return totalPath 


#根據圖片的地址，下載圖片並儲存在本地  
# def getAndSaveImg(imgUrl): 
def getAndSaveImg(imgUrl,iii): 
    if( url[-3:]=="jpg"): 
        # fileName=generateFileName() '.jpg' 
        # urllib.urlretrieve(imgUrl,createFileWithFileName(localPath,fileName)) 
        img_name = str(iii)+'.jpg'
        urllib.request.urlretrieve(imgUrl,createFileWithFileName(localPath,img_name)) 
    
    
#下載函式 
# def downloadImg(url): 
# urlList=getUrlList(url) #獲得全部圖片url儲存在一個list



# for urlString in urlList: 
# getAndSaveImg(urlString) 
# downloadImg(urlPath) 
iii = 1
for url_n in lista:
    url = url0+url_n
    getAndSaveImg(url,iii)
    iii+=1
    print(iii)



