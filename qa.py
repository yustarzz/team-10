#-*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup
url = 'http://admission.ewha.ac.kr/enter/doc/rolling/faq.asp'
response= requests.get(url)
source = response.text

soup = BeautifulSoup(source, 'html.parser')

top_list = soup.findAll('a',{"class":"tit"}) 


#print(top_list)
for i in top_list:
 #  print(i)
    if i.find("자기소개서")==True:
        print(i)
    
#if '자기소개서' in i:
 #       print(i)
  #  s=i
   # if s.find("자기소개서"):
    #    print (i.text.strip())
	
