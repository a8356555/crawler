#!/usr/bin/env python
# coding: utf-8

# 一、爬取的資料在DOC找到：
# 
# 直接取得解析HTML即可
# 
# 二、爬取的資料在XHR找到：
# 
# Content-Type: application/json 或者指定charset=UTF-8。
# 
# 使用的是request payload而非form data 
# 
# 需要解析js資料

# In[30]:


import requests
url='https://www.agoda.com/api/zh-tw/Main/GetSearchResultList'
payloadData = {
"SearchMessageID": "d844fb4f-a70d-4891-94a5-f15d9cd7fff9"
IsPollDmc: false
SearchType: 2
ObjectID: 503398
HashId: null
Filters: {HotelName: "", PriceRange: {Min: 0, Max: 0, IsHavePriceFilterQueryParamter: false}, ReviewScoreMin: 0,…}
SelectedColumnTypes: {ProductType: [-1]}
RateplanIDs: null
TotalHotels: 0
PlatformID: 1001
CurrentDate: "2020-01-08T20:54:25.7793484+07:00"
SearchID: 991110108205425800
CityId: 0
Latitude: 0
Longitude: 0
Radius: 0
RectangleSearchParams: null
PageNumber: 1
PageSize: 45
SortOrder: 0
SortField: 1
PointsMaxProgramId: 0
PollTimes: 0
SearchResultCacheKey: "6758c717-d183-423e-ad1e-0282bb47a468"
RequestedDataStatus: 1
MaxPollTimes: 0
CityName: null
ObjectName: ""
AddressName: null
CountryName: null
CountryId: 0
IsAllowYesterdaySearch: false
CultureInfo: "zh-TW"
CurrencyCode: null
UnavailableHotelId: 0
IsEnableAPS: false
SelectedHotelId: 0
IsComparisonMode: false
HasFilter: false
LandingParameters: {SelectedHotelId: 0, LandingCityId: 0}
NewSSRSearchType: 0
IsWysiwyp: false
RequestPriceView: null
FinalPriceView: 0
MapType: 0
IsShowMobileAppPrice: false
IsApsPeek: false
IsRetina: false
IsCriteriaDatesChanged: false
TotalHotelsFormatted: "0"
PreviewRoomFinalPrice: null
ReferrerUrl: null
CountryEnglishName: null
CityEnglishName: null
Cid: -218
Tag: null
ProductType: -1
NumberOfBedrooms: []
ShouldHideSoldOutProperty: false
FamilyMode: false
FlightSearchCriteria: null
PackageToken: null
isAgMse: false
ccallout: false
defdate: false
BankCid: null
BankClpId: null
ShouldShowHomesFirst: false
PropertyMatchResults: null
RequiredPropertyMatch: false
Adults: 2
Children: 0
Rooms: 1
MaxRooms: 9
RoomOccupancy: null
CheckIn: "2020-01-23T00:00:00"
LengthOfStay: 2
ChildAges: []
DefaultChildAge: 8
ChildAgesStr: null
CheckOut: "2020-01-25T00:00:00"
Text: ""
IsDateless: false
CheckboxType: 0
TravellerType: 1   
    
}
res = requests.post(url, json=payloadData)
print(res.text)


# In[26]:


# import requests
# from bs4 import BeautifulSoup as bs
# import pandas as pd
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
# url='https://www.agoda.com/zh-tw/search?area=503398&languageId=20&userId=26567622-9658-4602-9bc1-44da82a24fbf&sessionId=b4e4gnmeqlf5gk53m0xxxcoj&pageTypeId=103&origin=TW&locale=zh-TW&cid=-218&aid=130589&currencyCode=TWD&htmlLanguage=zh-tw&cultureInfoName=zh-TW&ckuid=26567622-9658-4602-9bc1-44da82a24fbf&prid=0&checkIn=2020-01-23&checkOut=2020-01-25&rooms=1&adults=2&children=0&priceCur=TWD&los=2&textToSearch=%E4%BA%94%E7%B5%90%E9%84%89&travellerType=1&familyMode=off&productType=-1&sort=priceLowToHigh'
# res = requests.get(url, headers=headers)
# print(res.text)

