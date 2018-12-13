#-*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup
url = 'http://admission.ewha.ac.kr/enter/doc/rolling/faq.asp'
response= requests.get(url)
source = response.text

soup = BeautifulSoup(source, 'html.parser')

top_list = soup.findAll('a',{"class":"tit"}) 
from flashtext import KeywordProcessor
keyword_processor=KeywordProcessor()
for i in range(0,len(top_list)):
    print(top_list[i])
    print(type(top_list[i]))

#for i in top_list:
#for i in range (0, len(top_list)):
    
   # keyword_processor.add_keyword('자기소개서')
   # keywords_found=keyword_processor.extract_keywords()
    
   # if (keywords_found):
     #     print(top_list[i])
    

#print(top_list)
#for i in top_list:
  #  print(i)
   # if match("자기소개서", i):
       # print(i)
        #print (i.text.strip())
